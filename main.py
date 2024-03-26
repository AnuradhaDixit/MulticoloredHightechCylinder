height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
BMI = weight / (height ** 2)
if BMI <= 18.5:
  print('you are underweight')
elif BMI <= 25:
  print('you are normal weight')
elif BMI >= 25:
  print('you are overweight')
else :
  print('you are obese'+f'your BMI is {BMI}')
