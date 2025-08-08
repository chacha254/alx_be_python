# FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# def convert_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# def convert_to_fahrenheit(celsius):
#     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)

# def main():
#     temperature = int(input("Enter the temperature to convert:"))
#     temp_in = input("Is the temperature in Celsius or Fahrenheit? (C/F)")

#     if temperature == "fahrenheit":
#         converted = convert_to_celsius(temperature)
#         print(f"{temperature}°F is  {converted:.2f}°C")
#     elif temperature == "celsius":
#         converted = convert_to_fahrenheit(temperature)
#         print(f"{temperature}°C is {converted:.2f}°F")
#     else:
#         print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
# if __name__ == "__main__":
#     main()

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature value: ").strip()
        unit_input = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        # Validate that temperature is a numeric value
        temperature = float(temp_input)

        if unit_input == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted:.2f}°C")
        elif unit_input == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        # Handle non-numeric temperature or wrong unit
        if "could not convert string to float" in str(ve):
            print("Invalid temperature. Please enter a numeric value.")
        else:
            print(ve)

if __name__ == "__main__":
    main()
