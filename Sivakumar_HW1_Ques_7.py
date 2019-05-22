# Namrata Sivakumar

vegetarian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten_free = input("Is anyone in your party gluten-free? ")

print("Here are the restaurant choices:")

if vegetarian == "yes" and vegan == "yes" and gluten_free=="yes":
    print("\tCorner Cafe")
    print("\tThe Chef's Kitchen")

elif vegetarian == "yes" and vegan == "no" and gluten_free=="yes":
    print("\tMain Street Pizza Company")
    print("\tCorner Cafe")
    print("\tThe Chef's Kitchen")

elif vegetarian == "yes" and vegan == "no" and gluten_free=="no":
    print("\tMama's Fine Italian ")


elif vegetarian == "no" and vegan == "no" and gluten_free=="no":
    print("\tJoe's Gourmet Burgers")

else:
    print("\tSorry, no choices!")
