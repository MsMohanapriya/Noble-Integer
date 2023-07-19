def NobleInteger(array):
    array.sort(reverse=True)
    count=0
    for i in range(len(array)):
        if i==array[i]:
            return 1
    return -1
array=list(map(int,input("enter array elements: ").split()))
print(NobleInteger(array))