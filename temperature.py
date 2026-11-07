direction = input("Convert to (C/F): ").upper()

temperature = float(input("Temperature: "))

if direction == "F":
    result = temperature * 9 / 5 + 32
    print(f"{temperature:.1f}°C = {result:.1f}°F")

elif direction == "C":
    result = (temperature - 32) * 5 / 9
    print(f"{temperature:.1f}°F = {result:.1f}°C")

else:
    print("Unknown direction")
