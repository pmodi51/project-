import random

otp = random.randrange(100000, 1000000)
print(otp)

user = int(input('Enter the otp: '))
if otp == user:
    print("Access granted!!!")
else:
    print("Access Denied")