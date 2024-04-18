


num = int(input("Enter four digit number:"))

#Display face value
def facevalue():
    print("Print face value")    
    num1 = int(num/1000)
    num2 = int((num/100)%10)
    num3 = int((num/10)%10)
    num4 = int(num%10)
    
    print(f"Face Value = {num1} {num2} {num3} {num4}")

def placevalue():
    placeValue = 1000
    num1 = int(num/1000)*placeValue
    placeValue/=10
    num2 = int(int(num/100)%10*placeValue)
    placeValue/=10
    num3 = int(int(num/10)%10*placeValue)
    placeValue/=10
    num4 = int(int(num%10)*placeValue)

    print(f"Place Value: {num} = {num1} + {num2} + {num3} + {num4}")

facevalue()
placevalue()

