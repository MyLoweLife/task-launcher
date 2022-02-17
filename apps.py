from email.mime import application
from pywinauto.application import Application

app = Application(backend="uia").start('notepad.exe')