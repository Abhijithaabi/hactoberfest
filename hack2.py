 num=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,num):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/num
print("Average of elements in the list",round(avg,2))
