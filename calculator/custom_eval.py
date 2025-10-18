
def custom_eval(expression):
    # This function evaluates an expression with addition having priority over multiplication
    expression = expression.replace(" ", "")
    parts = expression.split("*")
    results = []
    for part in parts:
        add_parts = part.split("+")
        add_result = sum(float(x) for x in add_parts)
        results.append(add_result)
    final_result = 1.0
    for res in results:
        final_result *= res
    return final_result

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        expression = sys.argv[1]
        result = custom_eval(expression)
        print(result)
    else:
        print("No expression provided.")
