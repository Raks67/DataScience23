import numpy as np
number = np.random.randint(1, 101) # загадываем число
count = 0
while True:
    count+=1
    predict_number=int(input("guess the mumber:"))
    if predict_number>number:
        print("The Number must be lower")
    elif predict_number<number:
        print("The Number must be higher")
    else:
        print(f"You guessed the right number. This is the number {number} for {count} tries")
        break