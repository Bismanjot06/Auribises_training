 

num=list(range(10,101,10))
print('number',num)

num.append(99)
num.append(92)
num.append(29)
num.append(11)

print('number',num)


print('length of numbers', len(num))
print('sum of numbers', sum(num))
print('max of numbers', max(num))
print('avg o numbers', sum(num)/len(num))

data= tuple(num)

name= 'majaki','chotu','tanu','manu'
name.sort()
print('name:', name)