second = 0
from time import sleep
while True:
    sleep(1)
    second += 1
    if second % 7 == 0:
        print("hop")
    else:
        print(second)
