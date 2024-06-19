import time
import sys

#Delay Printing

def delay_print(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05) #the time between the characters
    print()
        
print("SETTINGS:")
setting = input('\nTEXT SPEED\nBACK\n')
if setting == 'text speed':
    printSpeed = input('Slow, medium or fast text speed?\n')
    if printSpeed == 'slow':
        def delay_print(s):
            for c in s :
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.075)
    elif printSpeed == 'medium':
        def delay_print(s):
            for c in s :
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.03)
    elif printSpeed == 'fast':
        def delay_print(s):
            for c in s :
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.008)
    pass
elif setting == 'back':
    delay_print("Welcome to Soccer Career 2024.")
    delay_print("In this text-based game, you will play as a football player in the Irish first league. This is a developing game so apologies for any bugs. Please report these bugs on my github MrMao10 so I can fix them. I would also appreciate any recommendations to improve the game. Thanks!")