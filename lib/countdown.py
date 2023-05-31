
import time

def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(n):
    while n > 0 :
        print(f"{n} SECOND(S)!")
        n -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
    