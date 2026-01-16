# This stores learning preferences and performance

class Student:
    def __init__(self, name):
        self.name = name
        self.skill_level = 0.5   # 0-1 scale
        self.engagement = 0.5
        self.frustration = 0.0
        self.learning_style = "visual"
        self.history = []

    def update_performance(self, score):
        self.skill_level = min(1.0, max(0.0, self.skill_level + score))

    def log_event(self, event):
        self.history.append(event)