# Emotion Recognition (Simulated)
# Later this would connect to camera/microphone AI models

import random

def detect_emotion():
    emotions = {
        "engagement": round(random.uniform(0, 1), 2),
        "frustration": round(random.uniform(0, 1), 2),
        "confidence": round(random.uniform(0, 1), 2)
    }
    return emotions