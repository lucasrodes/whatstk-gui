# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None


a = Analysis(
    ['test.py'],
    pathex=['/Users/lucasrodes/repos/whatstk-gui/releases/macOS-10.13'],
    binaries=[('/System/Library/Frameworks/Tk.framework/Tk', 'tk'), ('/System/Library/Frameworks/Tcl.framework/Tcl', 'tcl')],
    datas=[('/Users/lucasrodes/repos/whatstk-gui/py37/lib/python3.7/site-packages/plotly', 'plotly')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False , icon='assets/favicon.icns'
)

app = BUNDLE(
    exe,
    name='WhatsTK.app',
    icon='assets/favicon.icns',
    bundle_identifier=None
)

DISTPATH='dist/test/'