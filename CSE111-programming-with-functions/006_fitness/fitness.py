import datetime
def main():
  gender = False
  while gender!="m" and gender!="f":
    gender = input("Enter your gender (m / f): ")
  birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
  weight = pouds_to_kg(float(input("Enter your weight in U.S. pounds: ")))
  height = inches_to_centimeters(float(input("Enter your height in U.S. inches: ")))
  age = compute_age(birthdate)
  print(f"Your age is {age}")
  print(f"Your weight is {weight:.2f} kg")
  print(f"Your height is {height:.2f} cm")
  bmr = calculate_bmr(gender, weight, height, age)
  print(f"Your BMR is {bmr:.2f} calories")
  bmi = calculate_bmi(weight, height)
  print(f"Your BMI is {bmi:.2f}")

def compute_age(birth_str):
  birthdate = datetime.datetime.strptime(birth_str, "%Y-%m-%d")
  today = datetime.date.today()
  age = today.year - birthdate.year
  if today.month > birthdate.month:
    age -= 1
  return age

def pouds_to_kg(pounds):
  return pounds * 0.45359237

def inches_to_centimeters(inches):
  return inches * 2.54359237

def calculate_bmi(weight, height):
  return 10000*weight / (height**2)


def calculate_bmr(gender,weight, height, age):
  if gender == "m":
    return 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
  elif gender == "f":
    return 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
  else:
    return 0

  
main()