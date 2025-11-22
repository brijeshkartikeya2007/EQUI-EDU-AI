class EquityAgent:
    def check_fairness(self, context):
        demographics = context.get("demographics", {})
        # Simulate a check
        if demographics.get("SES") == "low":
            return "EquityAgent: Extra learning tips for low SES learners provided!"
        return "EquityAgent: Content and assessment fair for all."

