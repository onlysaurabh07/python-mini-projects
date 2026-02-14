#define the menu of restaurant

Menu={
    'pizza':40,
    'pasta':50,
    'burger':80,
    'salad':90,
    'coffee':90,
}

#greet
print("WELCOME TO OUR HOTEL")
print("pizza:Rs40\npasta:Rs50\nburger:Rs80\nsalad: Rs90\ncoffee: RS90" )

total=0

item_1=input("Enter the name of item you want to order=")
if item_1 in Menu:
    total +=Menu[item_1]
    print(f"your item {item_1} has been added to ur order")

else:
    print(f"ordered item {item_1}is not available yet")


anotherorder=input("do u want to order another item?yes/nope____")

if anotherorder=="yes":
    item_2=input("enter the name of secnd item= ")
    if item_2 in Menu:
        total +=Menu[item_2]
        print(F"item {item_2} haas been added to order")
    else:print(f"ordeered {item_2}is n/ot avialble")

print(f"the total amount  to pay is {total}")        