from agents.gemini_helper import get_gemini_response
from tools.constants import get_physics_constant

class PhysicsAgent:
    def solve(self, query: str) -> str:
        try:
            constant_value = get_physics_constant(query)
            if constant_value:
                return f"PhysicsAgent found the constant: {constant_value}"
            else:
                return get_gemini_response(query)
        except Exception as e:
            return f"PhysicsAgent error: {str(e)}"
