import keyboard
import pyperclip


def foo():
    x = pyperclip.paste().upper()
    pyperclip.copy(x)
    keyboard.send('Ctrl + v')


keyboard.add_hotkey('Ctrl + 3', foo)
keyboard.wait()
