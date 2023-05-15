import pyautogui



def move_and_click(position, side_button, click=1):
    pyautogui.moveTo(position)
    pyautogui.click(button=side_button, clicks=click)

def get_loot(player_position, bp_position):
    move_and_click(player_position, 'right')
    move_and_click(bp_position, 'left', 5)