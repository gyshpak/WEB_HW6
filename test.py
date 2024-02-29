import random

spisok = [1,2,3,4,5,6,7,8,9,10,11,12]
weights_ = [1,2,3,4,5,10,10,20,20,15,5,5]

for i in range(30):
    print(*random.choices(spisok, weights_))