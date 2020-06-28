# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\asa\\PycharmProjects\\pyupdatermywx\\run.py'],
             pathex=['C:\\Users\\asa\\PycharmProjects\\pyupdatermywx', 'C:\\Users\\asa\\PycharmProjects\\pyupdatermywx\\.pyupdater\\spec'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\program files (x86)\\microsoft visual studio\\shared\\python37_64\\lib\\site-packages\\pyupdater\\hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='win',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='win')
