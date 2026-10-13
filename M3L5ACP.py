a = int(input("Enter Largest number : "))
b = int(input("Enter Smallest number : "))

if a > b:
    largest = a
else:
    largest = b

while True:
    if largest % a == 0 and largest % b == 0:
        print("LCM is : ", largest)
        break
    largest += 1
