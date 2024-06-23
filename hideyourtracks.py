import random
import pyautogui
import pyperclip
from time import sleep

def type_character(char):
    pyperclip.copy(char)
    pyautogui.hotkey('ctrl', 'v')

def typoer_from_file(file_path, wpm=100, accuracy=1, backspace_duration=0.1, correction_coefficient=0.4, wait_key='', break_key='escape'):
    chars = list('abcdefghijklmnopqrstuvwxyz')

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    spc = 12 / wpm
    spc_range = 0.8
    spc_low = spc * (1 - spc_range)
    spc_high = spc * (1 + spc_range)

    i = 0
    typos = 0

    if wait_key:
        pyautogui.confirm(text='Press OK when you are ready to start typing.', title='Typoer')

    while i < len(text):

        if pyautogui.press(break_key):
            return

        if typos and (i + typos >= len(text) or random.random() < 1 - correction_coefficient ** typos):
            sleep(backspace_duration)
            for _ in range(typos):
                pyautogui.press('backspace')
                sleep(backspace_duration)
            typos = 0

        if random.random() > accuracy:
            type_character(random.choice(chars))
            typos += 1
        else:
            type_character(text[i + typos])
            if typos:
                typos += 1
            else:
                i += 1

        duration = random.uniform(spc_low, spc_high)
        sleep(duration)


if __name__ == '__main__':
    file_path = r'C:\Users\teacher1\desktop\hideyourtracks\loremipsum.txt'  # Replace with your text file path and input your text in loremipsum.txt
    typoer_from_file(file_path, wpm=55, accuracy=0.9, wait_key='') # settings