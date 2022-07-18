from pynput.keyboard import Key, Controller
from time import sleep

class Macro:
    def __init__(self):
        self.create_macro = open("macro.txt", "a")
        with open("macro.txt", "r") as macrofile:
            self.macro_keys = macrofile.read()
        self.macro_keys = self.macro_keys.split(",", -1)
        self.special_keys = (
            "SPACE"," ", "LCTRL","LALT","LSHIFT","RCTRL","RALT","RSHIFT", "TAB", "ESC", "ESCAPE"
            )
            
            
    def run_macro(self):
        for character in self.macro_keys:
            if character.startswith("delay"):
                # will remove delay and get the number after (in s)
                character = character.replace("delay", "")
                sleep_time = int(character)
                sleep(sleep_time)
            elif character in self.special_keys:
                self.special_character = character
                self.macro_special_keys()
            elif character == ",":
                pass
            else:
                keyboard.press(Key.character)

    def macro_special_keys(self):
        if self.special_character == "SPACE" or " ":
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif self.special_character == "LCTRL":
            keyboard.press(Key.ctrl_l)
            keyboard.release(Key.ctrl_l)
        elif self.special_character == "LALT":
            keyboard.press(Key.alt_l)
            keyboard.release(Key.alt_l)
        elif self.special_character == "LSHIFT":
            keyboard.press(Key.shift_l)
            keyboard.release(Key.shift_l)
        elif self.special_character == "RCTRL":
            keyboard.press(Key.ctrl_r)
            keyboard.release(Key.ctrl_r)
        elif self.special_character == "RALT":
            keyboard.press(Key.alt_r)
            keyboard.release(Key.alt_r)
        elif self.special_character == "RSHIFT":
            keyboard.press(Key.shift_r)
            keyboard.release(Key.shift_r)
        elif self.special_character == "TAB":
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        elif self.special_character == "ESC" or "ESCAPE":
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)

    
keyboard = Controller()

macro = Macro()
macro.run_macro()

