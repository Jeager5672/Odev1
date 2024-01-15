import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\rPlease Wait: {timer}', end='', flush=True)
        time.sleep(1)
        t -= 1

t = 5




