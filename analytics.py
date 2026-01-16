# Analytics Engine
# Collects post-session insights

def generate_report(student):
    return {
        "Name": student.name,
        "Skill Level": round(student.skill_level, 2),
        "Total Events": len(student.history),
        "Learning Style": student.learning_style
    }