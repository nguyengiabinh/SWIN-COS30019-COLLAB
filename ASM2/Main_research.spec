# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Main_research.py'],
    pathex=[],
    binaries=[],
    datas=[('test.txt', '.'), ('test2.txt', '.'), ('test3.txt', '.'), ('test4.txt', '.'), ('test5.txt', '.'), ('test6.txt', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Main_research',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
