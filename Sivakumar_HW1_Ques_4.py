# Namrata Sivakumar


color1 = input("Enter first color: ")
color2 = input("Enter second color: ")

if color1 == "red" and color2 == "blue":
    print("Purple")
elif color1 == "red" and color2 == "yellow":
    print("Orange")
elif color1=="blue" and color2=="yellow":
    print("Green")
else:
    print("Error message: Enter primary colors: red,blue or yellow only!")
