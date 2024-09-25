import math

def sine_of_angle(degrees):
    radians = math.radians(degrees)
    sine_value = math.sin(radians)
    return sine_value

angle = 30  
result = sine_of_angle(angle)
print(f'The sine of {angle} degrees is {result:.4f}')
