class AccessibilityAgent:
    def make_accessible(self, context):
        needs = context.get("accessibility", "none")
        if needs == "dyslexia":
            return "Accessible version: Text is formatted with OpenDyslexic font and extra spacing."
        elif needs == "audio":
            return "Accessible version: Click for audio (mock link)."
        else:
            return "Standard accessible content provided."
