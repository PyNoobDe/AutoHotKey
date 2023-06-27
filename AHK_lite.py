from ahk import AHK

def Funktion():
    if ahk.active_window.pid == 20088:
        ahk.key_press("F8")

ahk = AHK()
win = ahk.windows
ahk.add_hotkey("XButton2", callback=Funktion)

ahk.start_hotkeys()
ahk.block_forever()
