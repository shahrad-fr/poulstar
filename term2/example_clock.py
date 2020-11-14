second = 0
minute = 0
hour = 0
from time import sleep
for i in range(1000):
    sleep(0.001)
    print(hour,":" ,minute,":" , second)
    second += 1
    if second == 59:
        minute += 1
        second = 0
        if minute == 59:
            hour += 1
            minute = 0

