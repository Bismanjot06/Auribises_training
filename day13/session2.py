# sort function
#applying bubble sort on list function 
def sort(data, low_to_high=0):
    if low_to_high==0:
       for i in range(len(data)-1):
            for j in range(len(data)-i-1): 
                if data[j]>data[j+1]:
                    temp=data[j]
                    data[j]=data[j+1]
                    data[j+1]=temp
            
    else:
        for i in range(len(data)-1):
            for j in range(len(data)-i-1):
                if data[j]<data[j+1]:
                    temp=data[j]
                    data[j]=data[j+1]
                    data[j+1]=temp
                    
number=[23,3,78,56,23,45,8,4,23,56] 
print(' numbers:')                   
print(number)                    

sort(data=number)
print('ascending order:')
print(number)

sort(data=number,low_to_high=1)
print('descending order:')
print(number)