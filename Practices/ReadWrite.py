import random

with open("test.txt", "a") as f:
    f.write(str(random.randint(100, 999)) + "\n")
    f.close
