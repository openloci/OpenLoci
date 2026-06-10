"""
Tests for skin discovery and metadata loading.

Run with: pytest tests/ -v
"""

import json
import re
from pathlib import Path

import pytest


from openloci.skins import list_skins, get_skin_path, get_skin_info


# ── list_skins ─────────────────────────────────────────────────────────────────

class TestListSkins:
    def test_returns_list(self):
        result = list_skins()
        assert isinstance(result, list)

    def test_xfiles_clue_present(self):
        assert "clue" in list_skins()

    def test_xfiles_skin_present(self):
        assert "xfiles" in list_skins()

    def test_siliconvalley_skin_present(self):
        assert "siliconvalley" in list_skins()

    def test_muppets_skin_present(self):
        assert "muppets" in list_skins()

    def test_digitalcircus_skin_present(self):
        assert "digitalcircus" in list_skins()

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

    def test_siliconvalley_path_exists(self):
        assert get_skin_path("siliconvalley").is_dir()

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
                f"Skin '{skin}' has {len(info['room_map'])} rooms, expected 10 (9 + Garden)"

    def test_core_cast(self):
        """skin.json must define exactly 6 core characters — one per Clue suspect
        (Miss Scarlett, Col. Mustard, Mrs. White, Mr. Green, Mrs. Peacock, Prof. Plum).
        These are the structural chassis roles. The Characters/ directory may hold
        any number of additional ensemble members beyond this core six."""
        for skin in list_skins():
            info = get_skin_info(skin)
            assert len(info["characters"]) == 6, \
                f"Skin '{skin}' has {len(info['characters'])} core cast members in skin.json, expected 6 (one per Clue suspect)"

    def test_room_map_fields(self):
        for skin in list_skins():
            for room in get_skin_info(skin)["room_map"]:
                for key in ("clue", "name", "prefix", "function"):
                    assert key in room, f"[{skin}] room missing '{key}': {room}"

    def test_invalid_skin_raises(self):
        with pytest.raises(FileNotFoundError):
            get_skin_info("nonexistent_xyz")




# ── template structure ─────────────────────────────────────────────────────────

class TestTemplateStructure:
    def _template_root(self, skin_name: str) -> Path:
        skin_path = get_skin_path(skin_name)
        candidates = [d for d in skin_path.iterdir()
                      if d.is_dir() and "cookiecutter" in d.name]
        assert len(candidates) == 1
        return candidates[0]

    def test_has_mansion(self):
        for skin in list_skins():
            assert (self._template_root(skin) / "the-mansion").exists(), \
                f"[{skin}] missing the-mansion/"

    def test_has_graveyard(self):
        for skin in list_skins():
            graveyard = self._template_root(skin) / "the-graveyard"
            assert graveyard.exists(), f"[{skin}] missing the-graveyard/"
            assert (graveyard / "README.md").exists(), f"[{skin}] missing the-graveyard/README.md"

    def test_has_garden(self):
        for skin in list_skins():
            garden = self._template_root(skin) / "the-garden"
            assert garden.exists(), f"[{skin}] missing the-garden/"
            assert (garden / "TODO.md").exists(), f"[{skin}] missing the-garden/TODO.md"

    def test_garden_has_readme(self):
        for skin in list_skins():
            assert (self._template_root(skin) / "the-garden" / "README.md").exists(), \
                f"[{skin}] missing the-garden/README.md"

    def test_garden_has_master_prompt(self):
        for skin in list_skins():
            assert (self._template_root(skin) / "the-garden" / "Rules" / "master_prompt.md").exists(), \
                f"[{skin}] missing the-garden/Rules/master_prompt.md"

    def test_garden_has_characters(self):
        for skin in list_skins():
            chars = list((self._template_root(skin) / "the-garden" / "Characters").glob("*.md"))
            assert len(chars) >= 4, f"[{skin}] expected ≥4 character files, found {len(chars)}"

    def test_mansion_has_nine_rooms(self):
        for skin in list_skins():
            info = get_skin_info(skin)
            mansion_dir = self._template_root(skin) / "the-mansion"
            actual_rooms = [d for d in mansion_dir.iterdir() if d.is_dir()]
            assert len(actual_rooms) == 9, \
                f"[{skin}] expected 9 room dirs in the-mansion, found {len(actual_rooms)}"

    def test_mansion_rooms_match_skin_json(self):
        """Room directory names in the-mansion must match the skin.json room_map."""
        for skin in list_skins():
            info = get_skin_info(skin)
            expected = {r["name"] for r in info["room_map"] if r["clue"] != "Vestibule"}
            mansion_dir = self._template_root(skin) / "the-mansion"
            actual = {d.name for d in mansion_dir.iterdir() if d.is_dir()}
            assert actual == expected, \
                f"[{skin}] room dir mismatch.\n  Expected: {sorted(expected)}\n  Actual:   {sorted(actual)}"

    def test_mansion_rooms_use_gerund_prefixes(self):
        """Every room dir must start with its skin.json prefix (no old-style intake_/build_/etc)."""
        old_prefixes = {"intake_", "build_", "ops_", "collab_", "meet_", "think_", "priv_", "pitch_", "retro_", "social_"}
        for skin in list_skins():
            mansion_dir = self._template_root(skin) / "the-mansion"
            for room_dir in mansion_dir.iterdir():
                if room_dir.is_dir():
                    for old in old_prefixes:
                        assert not room_dir.name.startswith(old), \
                            f"[{skin}] room '{room_dir.name}' still uses old prefix '{old}'"

    def test_garden_readme_uses_gerund_prefixes(self):
        """Garden README room map must reference new gerund prefixes and contain none of the old-style prefixes."""
        old_prefixes = ["intake_", "build_", "ops_", "collab_", "meet_", "think_", "priv_", "pitch_", "retro_", "social_"]
        new_prefixes = ["communicating_", "synthesizing_", "iterating_", "releasing_",
                        "deliberating_", "researching_", "brainstorming_", "pitching_", "planning_"]
        for skin in list_skins():
            readme = self._template_root(skin) / "the-garden" / "README.md"
            content = readme.read_text()
            for old in old_prefixes:
                assert f"`{old}`" not in content, \
                    f"[{skin}] garden README still references old prefix `{old}`"
            assert any(p in content for p in new_prefixes), \
                f"[{skin}] garden README contains no gerund prefixes — room map may be missing entirely"
