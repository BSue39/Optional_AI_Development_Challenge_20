# Adaptive Learning Engine
# This changes teaching strategy in real time

def adapt_content(student, emotion_data):
    if emotion_data["frustration"] > 0.7:
        return "Provide guided example and slow pace"
    
    if emotion_data["engagement"] < 0.3:
        return "Switch to interactive 3D demonstration"
    
    if student.skill_level > 0.8:
        return "Increase difficulty and reduce hints"
    
    return "Continue normal instruction"