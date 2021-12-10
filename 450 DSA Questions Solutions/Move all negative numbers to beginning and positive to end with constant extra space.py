def rearrange(arr,n):
    j = 0
    for i in range(0, n):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j+1
    print(arr)

arr = []
n = int(input("Enter size of an array"))
input("Enter array elements")
for i in range(0,n):
    num = int(input())
    arr.append(num)
rearrange(arr,n)
