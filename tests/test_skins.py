"""
Tests for skin discovery and metadata loading.

Run with: pytest tests/ -v
"""

import json
import re
from pathlib import Path

import pytest

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from openloci.skins import list_skins, get_skin_path, get_skin_info


# ── list_skins ─────────────────────────────────────────────────────────────────

class TestListSkins:
    def test_returns_list(self):
        result = list_skins()
        assert isinstance(result, list)

    def test_xfiles_skin_present(self):
        assert "xfiles" in list_skins()

    def test_sv_skin_present(self):
        assert "sv" in list_skins()

    def test_result_is_sorted(self):
        result = list_skins()
        assert result == sorted(result)

    def test_no_hidden_dirs(self):
        for name in list_skins():
            assert not name.startswith(".")


# ── get_skin_path ──────────────────────────────────────────────────────────────

class TestGetSkinPath:
    def test_xfiles_path_exists(self):
        assert get_skin_path("xfiles").is_dir()

    def test_sv_path_exists(self):
        assert get_skin_path("sv").is_dir()

    def test_invalid_skin_raises(self):
        with pytest.raises(FileNotFoundError):
            get_skin_path("nonexistent_skin_xyz")

    def test_all_skins_have_cookiecutter_json(self):
        for skin in list_skins():
            cc = get_skin_path(skin) / "cookiecutter.json"
            assert cc.exists(), f"Missing cookiecutter.json for: {skin}"
            data = json.loads(cc.read_text())
            assert "palace_name" in data


# ── get_skin_info ──────────────────────────────────────────────────────────────

class TestGetSkinInfo:
    def test_returns_dict(self):
        assert isinstance(get_skin_info("xfiles"), dict)

    def test_required_keys_present(self):
        for skin in list_skins():
            info = get_skin_info(skin)
            for key in ("name", "description", "room_map", "characters"):
                assert key in info, f"Skin '{skin}' missing key: {key}"

    def test_ten_rooms(self):
        for skin in list_skins():
            info = get_skin_info(skin)
            assert len(info["room_map"]) == 10, \
                f"Skin '{skin}' has {len(info['room_map'])} rooms, expected 10 (9 + Vestibule)"

    def test_six_characters(self):
        for skin in list_skins():
            info = get_skin_info(skin)
            assert len(info["characters"]) == 6, \
                f"Skin '{skin}' has {len(info['characters'])} characters, expected 6"

    def test_room_map_fields(self):
        for skin in list_skins():
            for room in get_skin_info(skin)["room_map"]:
                for key in ("clue", "name", "prefix", "function"):
                    assert key in room, f"[{skin}] room missing '{key}': {room}"

    def test_invalid_skin_raises(self):
        with pytest.raises(FileNotFoundError):
            get_skin_info("nonexistent_xyz")


# ── character prefix convention ────────────────────────────────────────────────

class TestCharacterPrefixes:
    """
    Characters follow the functional prefix convention: cro_, ceo_, cto_, etc.
    Files are named {prefix}{slug}.md and frontmatter declares prefix.
    """

    PREFIX_PATTERN = re.compile(r'^[a-z]+_')

    def _char_files(self, skin_name: str) -> list[Path]:
        skin_path = get_skin_path(skin_name)
        template_dirs = [d for d in skin_path.iterdir()
                         if d.is_dir() and "cookiecutter" in d.name]
        assert template_dirs, f"No template dir in skin: {skin_name}"
        chars_dir = template_dirs[0] / "The Vestibule" / "Characters"
        return [f for f in chars_dir.glob("*.md") if f.name != "README.md"]

    def test_xfiles_character_files_have_prefix(self):
        for f in self._char_files("xfiles"):
            assert self.PREFIX_PATTERN.match(f.name), \
                f"[xfiles] character file missing prefix: {f.name}"

    def test_sv_character_files_have_prefix(self):
        for f in self._char_files("sv"):
            assert self.PREFIX_PATTERN.match(f.name), \
                f"[sv] character file missing prefix: {f.name}"

    def test_skin_json_characters_have_prefix_field(self):
        for skin in list_skins():
            for char in get_skin_info(skin)["characters"]:
                assert "prefix" in char, \
                    f"[{skin}] character missing 'prefix' field: {char.get('skin', '?')}"
                assert char["prefix"].endswith("_"), \
                    f"[{skin}] prefix should end with '_': {char['prefix']}"

    def test_character_frontmatter_declares_prefix(self):
        for skin in list_skins():
            for f in self._char_files(skin):
                content = f.read_text()
                assert "prefix:" in content, \
                    f"[{skin}] {f.name} frontmatter missing 'prefix:' field"

    def test_filename_prefix_matches_frontmatter(self):
        for skin in list_skins():
            for f in self._char_files(skin):
                filename_prefix = f.name.split("_")[0] + "_"
                content = f.read_text()
                fm_match = re.search(r'^prefix:\s*(\S+)', content, re.MULTILINE)
                if fm_match:
                    fm_prefix = fm_match.group(1)
                    assert fm_prefix.startswith(filename_prefix), \
                        f"[{skin}] {f.name}: filename prefix '{filename_prefix}' " \
                        f"doesn't match frontmatter '{fm_prefix}'"


# ── template structure ─────────────────────────────────────────────────────────

class TestTemplateStructure:
    def _template_root(self, skin_name: str) -> Path:
        skin_path = get_skin_path(skin_name)
        candidates = [d for d in skin_path.iterdir()
                      if d.is_dir() and "cookiecutter" in d.name]
        assert len(candidates) == 1
        return candidates[0]

    def test_has_vestibule(self):
        for skin in list_skins():
            assert (self._template_root(skin) / "The Vestibule").exists()

    def test_has_palace(self):
        for skin in list_skins():
            assert (self._template_root(skin) / "The Palace").exists()

    def test_vestibule_has_readme(self):
        for skin in list_skins():
            assert (self._template_root(skin) / "The Vestibule" / "README.md").exists()

    def test_vestibule_has_master_prompt(self):
        for skin in list_skins():
            assert (self._template_root(skin) / "The Vestibule" / "Rules" / "master_prompt.md").exists()

    def test_vestibule_has_characters(self):
        for skin in list_skins():
            chars = list((self._template_root(skin) / "The Vestibule" / "Characters").glob("*.md"))
            assert len(chars) >= 4, f"[{skin}] expected ≥4 character files, found {len(chars)}"
