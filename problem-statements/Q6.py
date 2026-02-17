def convert_temperature(value: float, unit: str) -> float | str:
 
    unit = unit.upper()

    if unit == 'C':
       
        result = (value * 9/5) + 32
        return round(result, 1)

    elif unit == 'F':
        
        result = (value - 32) * 5/9
        return round(result, 1)

    else:
      
        return "Invalid Unit"


if __name__ == "__main__":
    temp_value = float(input("Enter temperature value: "))
    temp_unit = input("Enter unit (C/F): ")

    converted = convert_temperature(temp_value, temp_unit)
    print("Converted Temperature:", converted)
