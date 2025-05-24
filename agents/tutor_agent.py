from agents.math_agent import MathAgent
from agents.physics_agent import PhysicsAgent
from agents.gemini_helper import classify_query, get_gemini_response

class TutorAgent:
    def __init__(self):
        self.math_agent = MathAgent()
        self.physics_agent = PhysicsAgent()

    def handle_query(self, query: str) -> str:
        subject = classify_query(query)

        if subject == "math":
            return self.math_agent.solve(query)
        elif subject == "physics":
            return self.physics_agent.solve(query)
        else:
            # Use Gemini API for general questions
            return get_gemini_response(query)


