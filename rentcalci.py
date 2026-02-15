
#inputs we need from the user
#total rent
#total food ordered
#elctricity units spend
#charge per unit
#no of person living

#output
#total amount you have to pay is.

rent=int(input("enter ur hostel rent: "))
food=int(input("enter ur amount of food ordered: "))
electricity=int(input("enter the total of electricity spend: "))
charge_per_unit=int(input("enter the charge per unit: "))
person=int(input("enter the number of person living in room: "))

total_bill= electricity * charge_per_unit

total_expense= total_bill+food+rent
if person > 0:
    per_person = total_expense / person
    print("Each person will pay:", per_person)
else:
    print("Number of persons must be greater than 0")
