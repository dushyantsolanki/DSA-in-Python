LIST = [2, 6, 1, 7, 4, 2, 3, 9, 8, 10, 100, 92, 78, 36, 50]
LIST.sort()


# Binary search
INPUT = int(input("Enter your number : "))
beg = 0
end = len(LIST)-1
mid = int((beg + end)/2)


if(INPUT == LIST[mid]):
    print(" your number is in the list", INPUT)

for mid in range(15):
    if(INPUT > LIST[mid]):
        mid = mid+1
        if(INPUT == LIST[mid]):
            print("your number is in the List ", INPUT)

    else:
        if(INPUT < LIST[mid]):
            mid = mid-1
            if(INPUT == LIST[mid]):
                print(" your number is in the list ", INPUT)

            else:
                print("Your given number is not yet!!!")
                break
