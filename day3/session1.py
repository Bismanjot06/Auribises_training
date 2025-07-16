# followers=['Bisman', 'Karan', 'Anshul', 'Ankush', 'Bisman', 'Ankush']
# print(followers, type(followers), id(followers))

followers= {'Bisman', 'Karan', 'Anshul', 'Ankush', 'Bisman', 'Ankush'}
print(followers, type(followers),id(followers))
# print(followers[0]) we cannot access elements by index in a set

sahil_followers = {'Shail', 'Ankush', 'Anshul', 'Karan', 'Bisman'}

# mutual_followers = followers.intersection(shail_followers)
mutual_followers = followers & sahil_followers
# to find the mutual followers we csn use the intersection method or the & operator
print(mutual_followers, type(mutual_followers), id(mutual_followers))

for name in sahil_followers:
    print(name)