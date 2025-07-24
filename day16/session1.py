'''
single value container (which hold one value)
int, float, bool

multi value container (which can hold multiple data)
objects-. tuples, list, string, set, dictionary

sequences
  tuple
  list
  string 
  storage of the data is sequential or linear
  
  set
  dictionary 
   storage of the data is non sequential or non linear

  properties:
  indexing 
  negitive indexing 
  slicing 
  concatination
  multiplicity
  membership testng

'''
 
'''
data = (10,20,30)
print(data[0])

#list of lists
# 2-D list
number= [
         #   0   1  2
            [10,20,30],  #0
            [40,50,60],  #1
            [70,80,90],  #2
        ]

print(number[0][1])

#list of list of list
numbers = [
             #   0   1  2
            [10,20,30],  
            [40,50,60],  
            [70,80,90],  
            
               #   0   1  2
            [10,20,30],  #0
            [40,50,60],  #1
            [70,80,90],  #2
        ]

'''

message=  """
this is majak ni
 welcome to jindagi
   ab tum gaye
       
          """
          
print('message') 
print(message)         

print('lenght of message:', len(message))
print('length of message in -1',message[len(message)-1])

# 3. slicing
data= list(range(10,101,10))
print(data)

print(data[0:3])
print(data[-5:-2])

email='john@chotu.com'
name= email[:4]
domain=email[5:]
print('name:',name)
print('domain:',domain)

#concatenation
data1=[10,20]
data2=[30,40]
data3=data1+data2

name='You are '
name2='\u2764'
data=name+name2
print(data)

# 4. multiplicity
names= name*3
print(names)

#6. membership testing
 