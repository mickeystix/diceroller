import random

d = int(input("How many sides on the die?: ")) # Die type
rc = int(input("Roll how many times?: ")) # Number of rolls

def roll(d, rc):
    i = 1 # Incrementor for roll count
    rt = 0 # Roll total
    while rc != 0:
        x = random.randint(1, d)
        rc -= 1
        print("Roll #" + str(i) + ": " + str(x))
        i += 1
        rt += x
    print("Total: " + str(rt))
        
roll(d, rc)