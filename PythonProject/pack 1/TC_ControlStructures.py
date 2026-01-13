from unittest import case

num = 4
if num % 2 == 0:
    print("even number")
else:
    print("odd number")
marks=80

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")
for i in range(1,11):
    print(i)


    j = 1
while j <= 10:
        print(j)
        j += 1;
j = 1
while j <= 10:
    print(j)
    j += 1
    if j==2:
        break;

day=2
match day:
    case 1:
        print("1st day")
    case 2:
        print("2nd day")
    case 3:
        print("3rd day")
    case 4:
        print("4th day")
    case 5:
        print("5th day")
    case 6:
        print("6th day")
    case 7:
        print("7th day")