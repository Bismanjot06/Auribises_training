#exlore set 
#set is a collection of unordered and unindexed items

followers = {'majaki', 'chotu', 'tanu', 'manu'}
print('followers:', followers)
print('type of followers:', type(followers))
print('length of followers:', len(followers))
print('max followers:', max(followers))

numbers = list(range(10, 101, 10))
data=set(numbers)
data.add(99)
data.add(92)
data.add(29)

print('data:', data)
data.remove(100)  
print('data after remove:', data)


A= {1, 2, 3, 4, 5}
B= {4, 5, 6, 7, 8}
'''
C=A+B     # This will raise an error because sets do not support addition
print('c', C)
'''
D=A-B
print('D', D)

E=A^B
print('E', E)

F=A|B
print('F', F)

A.clear()
print('A after clear:', A)