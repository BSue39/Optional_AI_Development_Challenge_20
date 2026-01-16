# Main Loop
# Ties everything together

from student import Student
from emotion_engine import detect_emotion
from adaptive_engine import adapt_content
from tutor import tutor_response
from analytics import generate_report

student = Student("Alex")

print("Starting VR Learning Session...\n")

for step in range(5):
    emotion_data = detect_emotion()
    strategy = adapt_content(student, emotion_data)
    response = tutor_response(student, strategy)

    student.update_performance(0.05)
    student.log_event({
        "emotion": emotion_data,
        "strategy": strategy
    })

    print(f"Step {step + 1}")
    print("Emotion:", emotion_data)
    print("Strategy:", strategy)
    print("Tutor:", response)
    print("-" * 40)

print("\nSession Complete")
print("Analytics:", generate_report(student))