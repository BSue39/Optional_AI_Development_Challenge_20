# Tutor Logic
# Simulates an emotion-aware tutor

def tutor_response(student, strategy):
    responses = {
        "Provide guided example and slow pace":
            "Let's walk through this step together.",
        "Switch to interactive 3D demonstration":
            "Let me show you a visual example.",
        "Increase difficulty and reduce hints":
            "You're doing great! Try this harder challenge.",
        "Continue normal instruction":
            "You're on track. Keep going!"
    }

    return responses.get(strategy, "Let's continue.")