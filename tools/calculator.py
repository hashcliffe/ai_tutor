def calculate_expression(expr: str) -> float:
    try:
        return eval(expr)
    except Exception:
        raise ValueError("Invalid math expression.")
