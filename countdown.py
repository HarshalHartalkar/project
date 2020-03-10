import time
clear = "\n" * 100000
count = 30
for seconds in range(count):
    print(count)
    time.sleep(1)
    count -= 1
print(clear)