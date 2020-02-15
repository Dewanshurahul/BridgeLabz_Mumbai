# Taking the input from user as temperature(in Fahrenheit) and wind speed(in miles per hour) and printing back WindChill
temperature = int(input("Enter the temperature (in Fahrenheit)"))
windSpeed = int(input("Enter the temperature (in miles per hour)"))
if abs(temperature) <= 50 and (windSpeed >= 3 and windSpeed <= 120):
    windChill = 35.74 + (0.6215 * temperature) + (0.4275 * temperature - 35.75) * pow(windSpeed, 0.16)
else:
    print("Either Wind_Speed OR Temperature is out of range.")
print(windChill)
