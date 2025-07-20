''''
search
linear search
applying in:
1. simple list
2. list of Dictionaries
3. list of objects
4. linked list
 
'''

#applying search on simople list
data = [10,20,30,40,50,60,70]
names= ["sai","ram","hari","sita","gita"]

flag=False
input_data = int(input("enter the number to search:"))
for i in range(len(data)):
     if data [i]== input_data:
         print("number found at index",i)
         break
    
if flag==True:
    print("number not found")

'''
flag=False
name= input("enter the name to search:")
for name in range(len(names)):
    if names[name]==name:
        print("name found at index",name)
        break

if flag==True:
    print("name not found")
    '''
#doing the same program using while loop

