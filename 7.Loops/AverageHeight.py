Heights = input("Enter the Heights: ")
Heights_List = Heights.split()

total = 0

for Height in Heights_List:
    total += int(Height)
Average = total/len(Heights_List)    
print("Heights List: ",Heights_List)
print("Average of Heights: ",Average)    