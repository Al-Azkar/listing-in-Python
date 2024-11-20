#array exercise
arr=[]
for i in range(5):
    arr.append(i*2)
    i+=1


for j in range(5):
    print(arr[j],end=" ")
    #print("\\n")
    j+=1

def find_min_max(arr):
    if len(arr)==0:
        return None,None
    lowest=arr[0]
    highest=arr[0]
    for  num in arr:
        if num<lowest:
            lowest=num
        if num>highest:
            highest=num
    return lowest,highest

lowest,highest=find_min_max(arr)
#print(end="\n")
print("\nHighest:",highest,"Lowest:",lowest)
