import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
from HendlerPoke import HandlerPoke

from utils import get_loot, move_and_click


PLAYER_POSITION = (953, 483)
BP_LOOT_POSITION = (1750, 1013)
LIST_ATTACK = ['f1' 'f2', 'f3', 'f4', 'f5']
BATTLE_POSITION = (1777, 129)

handler_poke = HandlerPoke()
auto_cast = True

def key_code(key):
    global auto_cast
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.space:
        move_and_click(BATTLE_POSITION, 'left')
        for attack in LIST_ATTACK:
            pyautogui.press(attack)
        pyautogui.press('f10')
    if hasattr(key, 'char') and key.char == 'e':
        handler_poke.next()
    if hasattr(key, 'char') and key.char == 'q':
        handler_poke.previous()
    if hasattr(key, 'char') and key.char == '2':
        get_loot(PLAYER_POSITION, BP_LOOT_POSITION)
        pyautogui.press('f10')
    if hasattr(key, 'char') and key.char == '1':
        if auto_cast:
            for attack in LIST_ATTACK:
                pyautogui.keyDown(attack)
            auto_cast = False
        else:
            for attack in LIST_ATTACK:
                pyautogui.keyUp(attack)
            auto_cast = True
    if hasattr(key, 'char') and key.char == '3':
        pyautogui.write('oi')
        pyautogui.press('enter')

with Listener(on_release=key_code) as f:
    f.join()