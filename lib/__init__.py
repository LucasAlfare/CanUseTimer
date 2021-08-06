from winConf import window
from keyboard import is_pressed
from time import time, sleep
from lib.Shufflers import *

modalities = {'3x3': Salete(size=20)}
modality = '3x3'

def Console(text='>>: ', size=2):
    while True:
        try:
            read = int(input(text))
            if 0 < read <= size: return read
            else: print(f'Digit a value in range of 1 to {size}')
        
        except KeyboardInterrupt: exit()
        except: print('Digit a valid value')

def defModality(): print('Not done...')

def startTimer():
    print(f'The actual modality is: {modality}\n'
          f'Scrable: {Salete(20)}')

    print('Press spacebar to start timer...')
    while True:
        if is_pressed('space'):
            print('Continue pressing...')
            sleep(1)
            if is_pressed('space'):
                while is_pressed('space'): timer = time()

                print('Timer start...\n')
                while True:
                    if is_pressed('space'): break

                window(f'Time: {time() - timer:.2f}', 'double_line')
                break
            else: print('The timer not start, you need press until 1sec.')
    
if __name__ == '__main__': print('You need to open: main.py!')
