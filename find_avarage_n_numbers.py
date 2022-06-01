#How do you find the avarage of N numbers in python?
num = int(input("How many numbers? "))
total = 0

for n in range(num):
    numbers = float(input("Enter any number: "))
    total += numbers

avarage = total /num

print("Avarage is: ", avarage)