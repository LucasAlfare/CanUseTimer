from winConf import window
from keyboard import is_pressed
from time import time, sleep
from lib.Shufflers import *
import os

modalities = {'3x3': Salete(size=20),
              '2x2': Salete(size=10),
              'pyra': Cida(size=9, corner=4)}

def consoleClear() -> None:
    if os.name in ('nt', 'dos'): os.system('cls')
    else: os.system('clear')

def Console(text='>>: ', size=2) -> int:
    while True:
        try:
            read = int(input(text))
            if 0 < read <= size: return read
            else: print(f'Digit a value in range of 1 to {size}')
        
        except KeyboardInterrupt: exit()
        except: print('Digit a valid value')

def timeFormat(time):
    x = int(time // 60)
    y = time % 60
    if y < 10:
        y = '0' + f'{y:.2f}'
        return f'{x}:{y}' 
    else: return f'{x}:{y:.2f}'

def defModality(modality) -> str:
    print('All modalities:', end='')
    for m in modalities.keys(): print(f' {m}', end=' ')

    print()
    x = input('Digit the modality name: ')

    if x in modalities.keys():
        consoleClear()
        window('Modality changed!')
        return x
    else:
        consoleClear()
        window('this modality doesn\'t exist.')
        return modality

def startTimer(modality) -> None:
    print(f'The actual modality is: {modality}\n'
          'Scrable: ', end='')
    for move in modalities[modality]: print(move ,end=' ')

    print('\nPress spacebar to start timer... (Press escape to exit)')
    while True:
        if is_pressed('space'):
            print('Continue pressing...')
            sleep(0.85)
            if is_pressed('space'):
                while is_pressed('space'): timer = time()

                print('Timer start...\n')
                while True:
                    if is_pressed('space'): break

                consoleClear()
                totalTime = time() - timer
                if totalTime >= 60:
                    totalTime = timeFormat(totalTime)
                    window(f'Time: {totalTime}', 'double_line')
                else: window(f'Time: {totalTime:.2f}', 'double_line')

                break
            else: print('The timer not start, you need press until 0.85secs.')
        
        if is_pressed('escape'): consoleClear(); break
    
if __name__ == '__main__': print('You need to open: Main.py!')