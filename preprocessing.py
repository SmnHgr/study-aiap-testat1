import os

path = './raw/'
files = os.listdir(path)

count = 0

for file in files:
    if 'L.png' in file:
        os.remove(path + file)
