firstname = input("enter first name: ")
lastname = input("enter last name: ")

score1 = float(input("enter first score: "))
score2 = float(input("enter second score: "))
score3 = float(input("enter third score: "))

average = (score1 + score2 + score3) / 3

if average >= 17:
    status = "daneshjoie momtaz"
elif average >= 12:
    status = "daneshjoie adi"
else:
    status = "daneshjoie mashrot"

print(f"{firstname} {lastname} - {status}")

#محاسبه معدل 