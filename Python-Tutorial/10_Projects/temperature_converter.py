# Temperature Converter 

unit = input("Is this temperature in Celsius or Fahreheit:")

temperature = float(input("Enter the temperature: ")) 

if unit == "C":
    temperature = round((9 * temperature)/5+32,1)
    print("Celsius to fahrenheit:",temperature)

elif unit == "F":
    temperature = round((temperature - 32)* 5/9,1)
    print("Fahreheit to Celsius: ",temperature)

else:
    print("Ente the valid unit")
