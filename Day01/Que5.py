

m1 = int(input("Enter marks of subject 1:"))
m2 = int(input("Enter marks of subject 2:"))
m3 = int(input("Enter marks of subject 3:"))

avg = (m1+m2+m3)/3

print(f"Average = {avg}")

if avg >= 90 and avg <= 100:
    print("A")
elif avg >= 80 and avg <= 89:
    printf("B")
elif avg >= 70 and avg <= 79:
    print("C")
elif avg >= 60 and avg <= 69:
    print("D")
elif avg >= 0 and avg <=59:
    print("F")
else:
    print("Invalid Average")



