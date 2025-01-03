def function_with_uncommon_bug(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        if b == 0:
            return "Division by zero"
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return f"Error: {e}"

print(function_with_uncommon_bug(10, 0))
print(function_with_uncommon_bug(10, 2))
print(function_with_uncommon_bug(10, "a"))
print(function_with_uncommon_bug("a", 2))