class ContentAgent:
    def generate(self, context):
        style = context.get("style", "simple")
        topic = context.get("topic", "Science")
        learner = context.get("learner", "Student")
        # Simulate validation/loop
        if not topic.strip():
            return "ContentAgent: Please specify a topic."
        msg = f"{learner}, here is a {style} explanation of {topic}."
        if style == "visual":
            msg += " [Imagine a diagram: see photosynthesis as a solar panel!]"
        return msg
