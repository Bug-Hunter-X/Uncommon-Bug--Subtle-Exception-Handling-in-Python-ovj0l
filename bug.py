def function_with_uncommon_bug(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"

print(function_with_uncommon_bug(10, 0))
print(function_with_uncommon_bug(10, 2))