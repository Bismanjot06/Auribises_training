# Object Oriented Programming example with the zomato case study
'''
requirement 
Mr. Jhon is my client
He is running a restaurant
He wants to build a system to manage his restaurant

In the application, user should be abe to login.
He can select a restraunt
he can view its menu
add dishes to cart
and place an order.

'''
'''
1.indetify the object, i.e. Think of an object
user-> name, email, password,phone, address,age etc
restaurant -> name, address, phone, menu, photo, rating, reviews, address etc
dish -> name, price, description, photo, category etc
order -> user, restaurant, dishes, total_price, status, order_time etc
menu -> dishes, categories etc

by observing this
1 user can place many orders
2 a restaurant can have many dishes
many users can place many orders...

'''


# Object Oriented Programming example with the youtube case study
'''
requirement
Mr. Jhon is my client
He is running a youtube channel
He wants to build a system to manage his youtube channel
In the application, user should be able to login.
He can view the videos
he can like or dislike the video
he can comment on the video
he can subscribe to the channel
he can view the channel details
'''
'''1.indetify the object, i.e. Think of an object
user-> name, email, password, phone, address, age etc
channel -> name, description, photo, subscribers, videos etc
video -> title, description, photo, likes, dislikes, comments etc
comment -> user, video, text, likes, dislikes, timestamp etc
subscription -> user, channel, timestamp etc
by observing this
1 user can subscribe to many channels
2 a channel can have many videos
3 a video can have many comments
4 a user can like or dislike many videos
'''



