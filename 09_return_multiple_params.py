def calculate_numbers(a, b):
    return a + b, a * b, a / b

def calculate_numbers_b(a, b):
    return {
        "add_result": a + b, 
        "multiply_result": a * b, 
        "divide_result": a / b
        }

result = calculate_numbers_b(10, 20)
print(result["add_result"])