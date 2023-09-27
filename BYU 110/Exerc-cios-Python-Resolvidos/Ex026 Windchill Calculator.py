#I add a while True to play again the program

def windchill_calculate (temperature,wind_speed):
    return  35.74 + 0.6215 * float(temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * float(temperature) * (wind_speed ** 0.16) 

def celcius_to_fahrenheit (celsius):
    return celsius * (9/5) + 32

wind_speed = list(range(5,61,5))

while True:
    temperature = float(input("what is the temperature? "))
    measures_temperature = input("Fahrenheit or Celsius (F/C)?\n ")

    if measures_temperature == "f":

        for speed in wind_speed:
            print(f"At temperature {temperature:.1f}F, and wind speed {speed} mph, the windchill is: {windchill_calculate(temperature,speed):.2f}F")

    elif measures_temperature == "c":
        
        celsius_temperature = celcius_to_fahrenheit(temperature)

        for speed in wind_speed:
            print(f"At temperature {celsius_temperature:.1f}F, and wind speed {speed} mph, the windchill is: {windchill_calculate(celsius_temperature,speed):.2f}F")


