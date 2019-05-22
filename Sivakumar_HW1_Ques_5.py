#Namrata Sivakumar



selling_price = 99.00

quantity = int(input("Enter the number of packages purchased: "))


discount = 0.00
total = 0.00


if quantity >9 and quantity<20:
    discount = 0.10
    total = selling_price*quantity - discount*selling_price
    print('Your discount is {:.0f}%'.format(discount*100))
    print('The total amount after discount is ${}'.format(total))

elif quantity>19 and quantity<50:
    discount = 0.20
    total = selling_price * quantity - discount * selling_price
    print('Your discount is {:.0f}%'.format(discount * 100))
    print('The total amount after discount is ${}'.format(total))

elif quantity>49 and quantity<100:
    discount=0.30
    total = selling_price * quantity - discount * selling_price
    print('Your discount is {:.0f}%'.format(discount * 100))
    print('The total amount after discount is ${}'.format(total))

elif quantity>99:
    discount=0.40
    total = selling_price * quantity - discount * selling_price
    print('Your discount is {:.0f}%'.format(discount * 100))
    print('The total amount after discount is ${}'.format(total))

else: print("Sorry, no discount!")



