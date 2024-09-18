def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_celsius = 25
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")