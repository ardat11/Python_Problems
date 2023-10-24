#Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

#The resulting number indicates one of the following categories:

#Underweight = less than 18.5
#Normal = more or equal to 18.5 and less than 25
#Overweight = more or equal to 25 and less than 30
#Obesity = 30 or more

weight = input(input("Enter your weight"))

height = int(input("Enter your height"))

BMI = weight / height**2

if BMI < 18.5:
    print("Underweight")

if 18.5 <= BMI <= 25 :
    print("Normal")

if 25 <= BMI <= 30:
    print("Overweight")

if 30 < BMI:
    print("Obesity")

    