arr=[8,56,2,6,9,80,72]
def B_sort(arr:list,x:int):
    for i in range(1,len(arr)):
        r=arr[i]
        j=i-1
        while j>=0 and r<arr[j]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j-=1
    l=0
    r = len(arr) - 1

    print(arr)
    while l<=r:
        m = (r + l) // 2
        if x>arr[m]:
            l=m+1
        elif x<arr[m]:
            r=m-1
        else:
            return arr[m]
    return "not found"

print(B_sort(arr,2))
