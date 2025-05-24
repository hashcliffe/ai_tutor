physics_constants = {
    "speed of light": "299,792,458 m/s",
    "gravitational constant": "6.674 × 10^-11 N·m²/kg²",
    "planck's constant": "6.626 × 10^-34 Js"
}

def get_physics_constant(query: str) -> str:
    for name in physics_constants:
        if name in query.lower():
            return physics_constants[name]
    return None
