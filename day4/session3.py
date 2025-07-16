"""
zomato:20% off
      :minimum order value: 250
      
jaiveer: 60% off 
       :minimum order value: 500
"""

promo_code = input("Enter your promo code: ")
billing_amount = int(input("Enter your billing amount: "))
if promo_code == "zomato":
    if billing_amount >= 250:
        discount = billing_amount * 0.20
        final_amount = billing_amount - discount
        print("you got a discount of \u20b9", discount)
        print("your final amount is \u20b9", final_amount)
    else:
        print("minimum order value is \u20b9 250")
        print("please add items worth \u20b9", (250 - billing_amount), "more")
elif promo_code == "jaiveer":
    if billing_amount >= 500:
        discount = billing_amount * 0.60
        final_amount = billing_amount - discount
        print("you got a discount of \u20b9", discount)
        print("your final amount is \u20b9", final_amount)
    else:
        print("minimum order value is \u20b9 500")
        print("please add items worth \u20b9", (500 - billing_amount), "more")
        
else:
    print("invalid promo code")
    print("please check and apply again")