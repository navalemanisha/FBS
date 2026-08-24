# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

no = int(input("Enter the No you want to get ticket for "))
totalAmount = 0

while 1 <= no:
    age1=int(input("enter the age of 1st person= "))
    tkp1=float(input("Enter the Price of 1st person= "))

    if age1<12:
        disco=tkp1*(30/100)
        print(f"Pasenger get discount of rs{disco}")
        totalAmount=totalAmount+(tkp1-disco)

    elif age1>59:
        disco=tkp1*(50/100)
        print(f"Pasenger get discount of rs{disco}")
        totalAmount=totalAmount+(tkp1-disco)

    else:
        totalAmount=totalAmount+tkp1

print(totalAmount)