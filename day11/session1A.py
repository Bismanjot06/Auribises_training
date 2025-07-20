def linear_search(data=[], element= None):
    flag=False
input_data = int(input("enter the number to search:"))
for i in range(len(input_data)):
     if input_data [i]== input_data:
         print("number found at index",i)
         flag=True
         break
      
if flag==False:
    print("number not found")