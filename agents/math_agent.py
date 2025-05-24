from sympy import symbols, Eq, solve, sympify
import re

class MathAgent:
    def solve(self, query: str) -> str:
        try:
            # Clean up input: replace ^ with ** for power, insert * between digit and variable
            query = query.lower().replace('^', '**')
            query = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', query)

            # Dynamically detect variables in the query
            variables = list(set(re.findall(r'[a-zA-Z]', query)))
            symbols_map = {var: symbols(var) for var in variables}

            if '=' in query:
                # Algebraic equation
                lhs, rhs = query.split('=')
                lhs_expr = sympify(lhs.strip(), locals=symbols_map)
                rhs_expr = sympify(rhs.strip(), locals=symbols_map)

                equation = Eq(lhs_expr, rhs_expr)
                solution = solve(equation, list(symbols_map.values()))

                if not solution:
                    return "No solution found."
                # Return solution as comma-separated values if multiple
                return ', '.join([str(s) for s in solution])

            else:
                # Arithmetic expression only
                expr = sympify(query, locals=symbols_map)
                result = expr.evalf()
                # Remove trailing .0 for integers
                if result == int(result):
                    return str(int(result))
                return str(result)

        except Exception as e:
            return f"MathAgent error: {str(e)}"
