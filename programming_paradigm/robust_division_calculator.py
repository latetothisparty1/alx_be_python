def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors:
    - Division by Zero: catches ZeroDivisionError
    - Non-numeric Input: catches ValueError for non-numeric inputs
    Returns appropriate messages for errors or the result for successful division.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."  # Updated error message
        result = numerator / denominator
        return f"Result: {result:.2f}"
    except ValueError:
        return "Error: Non-numeric input. Please enter valid numbers."


