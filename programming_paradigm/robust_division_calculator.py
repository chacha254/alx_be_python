def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator or numerator == 0: 
            print("Cannot divide by zero")
            return None
        else:
            output = numerator / denominator
            print(f"The result of the division is{output}")
            return output

    except ValueError:
        print(f"Please enter numeric values only")
        return None
