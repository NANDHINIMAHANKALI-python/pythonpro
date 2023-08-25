def celsius_to_fahrenheit(celsius):
    return (celsius*9/5) +32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32)*5/9
temperature = float(input("Enter temperature"))
unit = input("enter unit (c for celsius , f for fahrenheit)")

if unit == "c": 25

  converted_temperature = celsius_to_fahrenheit(temperature)

  print("converted temperature:{converted temperature :2f}}°F")
elif unit == "f":
    converted_temperature=fahrenheit_to_celsius(temperature)
    print("converted temperature:{converted temperature :2f}°C")
else:
    print ("invalid unit")