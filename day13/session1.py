#bubble sort

values=[23,45,24,78,23,6,73,13,2,53]

for i in range(len(values)-1):
    for j in range(len(values)-i-1): 
        if values[j]>values[j+1]:
            values[j],values[j+1]= values[j+1],values[j]
# Bubble sort implementation in Python
    
print(values)    

'''
how it works 

numbers: [10, 30, 50, 20, 40]

outer  : 0, 1, 2, 3
outer  : 0
numbers: 10, 30, 50, 20, 40
----------
inner  : 5-0-1 -> 4, 0 to 3
inner  : 0, 10 > 30 ?
         10, 30, 50, 20, 40
inner  : 1, 30 > 50 ?
         10, 30, 50, 20, 40
inner  : 2, 50 > 20 ?
         10, 30, 20, 50, 40
inner  : 3, 50 > 40 ?
         10, 30, 20, 40, 50

----------
outer  : 1
numbers: 10, 30, 20, 40, 50
---------
inner  : 5-1-1 -> 3, 0 to 2
inner  : 0, 10 > 30 ?
        10, 30, 20, 40, 50
inner : 1, 30 > 20 ?
        10, 20, 30, 40, 50
inner : 2, 30>40 ?
        10, 20, 30, 40, 50
        inner : 3, 40 >50 ?
        10, 20, 30, 40, 50

----------
outer : 2
numbers: 10, 20, 30, 40, 50
----------
inner : 5-2-1 -> 2
inner  : 0, 10 > 20 ?
        10, 20, 30, 40, 50
inner : 1, 20 > 30 ?
        10, 20, 30, 40, 50  
        
outer : 3
numbers: 10, 20, 30, 40, 50
----------
inner : 5-3-1 -> 1
inner  : 0, 10 > 20 ?
        10, 20, 30, 40, 50

        
'''

