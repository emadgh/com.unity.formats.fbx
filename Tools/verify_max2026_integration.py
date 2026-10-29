"""Source-only preflight checks for the Unity 6.7 / 3ds Max 2026 fork.

Run: python Tools/verify_max2026_integration.py
This does not replace an actual Unity/Max round-trip test.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "com.unity.formats.fbx"
SCRIPTS = Path("Integrations/Autodesk/max/scripts")
NAMES = (
    "UnityFbxForMaxPlugin.ms",
    "configureUnityFbxForMax.ms",
    "unityFbxExportSettings.ms",
    "unityFbxImportSettings.ms",
)


def check() -> None:
    bundled = PACKAGE / "Editor/Integrations~" / SCRIPTS
    for name in NAMES:
        source = ROOT / SCRIPTS / name
        target = bundled / name
        assert target.is_file(), f"Package is missing {target}"
        assert source.read_bytes() == target.read_bytes(), f"Out-of-sync MaxScript: {name}"

    plugin = (bundled / NAMES[0]).read_text(encoding="utf-8")
    assert "if (maxVersion())[1] >= 27000 then" in plugin
    assert "else if (maxVersion())[1] >= 20000 then" in plugin
    assert "#cuiRegisterMenus unityFbxRegisterMenus" in plugin
    for action in ("UnityImport`Unity", "UnityExport`Unity", "UnityExportModel`Unity"):
        assert action in plugin, f"Missing 2025+ menu action: {action}"

    installer = (PACKAGE / "Editor/InstallIntegration.cs").read_text(encoding="utf-8")
    assert "PackageInfo.FindForAssetPath" in installer
    assert '"Editor", "Integrations~"' in installer
    manifest = json.loads((PACKAGE / "package.json").read_text(encoding="utf-8"))
    assert manifest["version"] == "5.1.6-max2026.1"
    assert manifest["unity"] == "6000.0"

    print("PASS: bundled scripts, Max 2025+ menus, package path and manifest")
    print("NOT TESTED: 3ds Max 2026 startup/UI and Unity 6.7 FBX round-trip")


if __name__ == "__main__":
    check()
