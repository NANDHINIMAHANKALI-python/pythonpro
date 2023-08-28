def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ")

if unit == "C":
    temperatureIs = celsius_to_fahrenheit(temperature)
    print(f"Converted temperature: {temperatureIs:.2f}°F")
elif unit == "F":
    temperatureIs = fahrenheit_to_celsius(temperature)
    print(f"Converted temperature: {temperatureIs:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' or 'F' for Celsius or Fahrenheit.")