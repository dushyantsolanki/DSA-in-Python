LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Linear Seach

user = int(input(" Enter your number : "))

for i in range(10):

    if(user == LIST[i]):
        print(" Your number in the list")
        break
else:
    print("your number is not in list")
