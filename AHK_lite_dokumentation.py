from ahk import AHK # Importiere die AHK-Bibliothek

def Funktion(): # Definiert eine Funktion namens "Funktion"
    if ahk.active_window.pid == 20088: # Überprüft, ob das aktive Fenster die Prozess-ID (PID) 20088 hat (Funktion wird nur im Pycharm-Prozess ausgeführt)
        ahk.key_press("F8") # Drückt die Taste "F8" in der AutoHotkey-Skriptsprache

ahk = AHK() # Erzeugt eine Instanz der AHK-Klasse
ahk.add_hotkey("XButton2", callback=Funktion) # Füge einen Hotkey für die XButton2-Maustaste hinzu, der die Funktion "Funktion" aufruft
ahk.start_hotkeys() # Starte die Ausführung der Hotkeys
ahk.block_forever() # Blockiere das Programm und führe es unendlich lange aus
