class AssessmentAgent:
    def generate(self, context):
        topic = context.get("topic", "Science")
        return f"Quiz:\n1. Name one fact about {topic}.\n2. Why is {topic} important?"

