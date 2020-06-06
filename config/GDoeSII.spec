# -*- mode: python -*-

block_cipher = None
added_files = [('E:/myenv/GDoeSII/logo.ico','data'),
			 ('E:/myenv/GDoeSII/Instructions.png','data'),
			 ('E:/myenv/GDoeSII/Aboutme.png','data'),
			 ('E:/myenv/GDoeSII/Triangle.png','data'),
			 ('E:/myenv/GDoeSII/Rectangle.png','data'),
			 ('E:/myenv/GDoeSII/saveIcon.png','data'),
			 ('E:/myenv/GDoeSII/Circle.png','data')]


a = Analysis(['GDoeSII.py'],
             pathex=['E:\\myenv\\GDoeSII'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='GDoeSII',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='logo.ico')
