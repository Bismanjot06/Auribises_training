#coupon_code = "DISCOUNT20"
#billing_amount = int(input("Enter your billing amount: "))


#if statement
"""
if billing_amount > 449:
    print("You are eligible for the coupon")
    print("Your coupon code is: ", coupon_code)
else:
    print("Sorry, you are not eligible for the coupon")
    """
    
    
#nested if-else
coupon_code = input('Enter Coupon Code: ')
billing_amount = int(input('Enter Billing Amount:'))
if coupon_code== "chotubadmos@124":
    print("coupon code is valid")
    if billing_amount >449:
        billing_amount-=150
        print('please pay:', billing_amount)
        print('thank you')
    else:
        print('sorry, applied coupon is not available')
        print('add items worth', (450-billing_amount),'more')
else:
    print('coupon invalid. Please check and apply again')    