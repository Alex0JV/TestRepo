import time
import random
import string
print("Hello!")

def randomGibberish()->str:
    text = ""
    for i in range(1, 40):
        text += random.choice(string.hexdigits)
    return text

i = 0
while(i < 100):
    time.sleep(random.randint(10,50) * 0.01)
    print(" " + str(i) + "% #" + randomGibberish() + "\r", end="")
    i += random.randint(1,3)

print("100%")    