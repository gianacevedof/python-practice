# you use default arguments when you're creating a function
# and you want one of the arguments to have a default value

import time

def count(end, start=1):
    for x in range(start, end+1):
        print (x)
        time.sleep(1)
    print("Time's up!")

i = input("How much time do you want to count?")
i = int(i)
print(count(20, 10))