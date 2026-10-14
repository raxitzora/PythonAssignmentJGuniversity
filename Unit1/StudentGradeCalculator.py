'''
8. Write a Python program to input marks of the three subjects. Calculate the
percentage and grade according to the following:

Percentage &gt;= 90% : Grade O
Percentage &gt;= 80% : Grade A
Percentage &gt;= 70% : Grade B
Percentage &gt;= 60% : Grade C
Percentage &gt;= 50% : Grade D
Percentage &gt;= 40% : Grade E
Percentage &lt; 40% : Grade F
'''



# Calculate Percentage and Grade

print("----- Percentage Calculation -----")

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("=" * 25)
print("Subject 1 =", marks1)
print("Subject 2 =", marks2)
print("Subject 3 =", marks3)
print("Total =", total)
print("Percentage = {:.2f}%".format(percentage))
print("Grade =", grade)
print("=" * 25)