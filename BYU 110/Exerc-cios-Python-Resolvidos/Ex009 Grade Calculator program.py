import random

value = list(range(101))
probability = [1 if 70 <= valor <= 80 else 0.5 for valor in value]
ramdom_number = random.choices(value, weights=probability)[0]

print(ramdom_number)

if ramdom_number >= 90:
    grade = "A"
elif ramdom_number >= 80:
    grade = "B"
elif ramdom_number >= 70:
    grade = "C"
elif ramdom_number >= 60:
    grade = "D"
else:
    grade = "F"

grade_post = ramdom_number%10
if ramdom_number >= 60:
    if grade_post >= 7:
        post = "+"
    elif grade_post >=3:
        post = ""
    else:
        post = "-"
else:
    post = ""

print (f"{grade} {post}")
if ramdom_number >= 70:
    print ("Congratulations! We're so very proud of you!")
else:
    print ("Sorry, you need to study more...")

