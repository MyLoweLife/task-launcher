from pywinauto.application import Application

notepad = Application(backend="uia").start('notepad.exe')

# whatsapp = Application(backend="uia").start('whatsapp.exe')
