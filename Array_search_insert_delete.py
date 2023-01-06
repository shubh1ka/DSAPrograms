def search(arr,x):
    cnt=0
    for i in range(0,len(arr)):
        if arr[i]==x:
            cnt=cnt+1
    if cnt>0:
        return("The element is at index : ",i)
    else:
        return("element not found")

def insert(arr,y,yi):
    arr.insert(yi,y)
    return("The element is inserted and the new list is :",arr)
def delete(arr,ele):
    arr.remove(ele)
    return("Array after deletion is : ",arr)


if __name__ == '__main__':
    print("Enter an array :")
    arr= list(map(int, input().split()))
    print("Enter the element you want to search:")
    x=int(input())
    print("Enter the element you want to insert and the index")
    y=int(input())
    yi=int(input())
    print("Enter the element you want to delete:")
    ele = int(input())
    print(search(arr,x))
    print(insert(arr,y,yi))
    print(delete(arr,ele))








