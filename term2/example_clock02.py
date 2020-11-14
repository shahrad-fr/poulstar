second = 0
minute = 0
hour = 0
x = 0
from time import sleep
while True:
    sleep(0.0004)
    print(hour,":" ,minute,":" , second)
    second += 1
    if second == 59:
        minute += 1
        second = 0
        if minute == 59:
            hour += 1
            minute = 0



