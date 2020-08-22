# BubbleSort.py by End

list1 = []

# Input
while True:
    try:
        num = int(input("Enter how many numbers you want sorted:"))
        print("Please enter values of your numbers:")
        for k in range(num):
            list1.append(int(input()))

        print("unsorted list:",list1)

        # Sorting def
        for j in range(len(list1)-1):
            for i in range(len(list1)-1-j):
              if list1[i] > list1[i+1]:
                list1[i],list1[i+1] = list1[i+1],list1[i]

        # This part of the code can show how the machine sorts each number
        # by default its off
                #print(list1)
              #else:
                #print(list1)
            #print()

        # End result
        print("sorted list:",list1)
        
    except:
        print("The value you have entered is not a number!")
        print("Please try again")
        
    else:
        break
