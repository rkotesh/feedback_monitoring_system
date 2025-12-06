class Categorizer:
    categories = {
        "Service Issue": ["service", "support", "staff"],
        "Delivery Delay": ["delay", "late", "slow"],
        "Billing Problem": ["bill", "payment", "charge"],
        "App/Website Issue": ["app", "website", "error", "bug"],
        "General Appreciation": ["good", "love", "excellent", "amazing"]
    }

    def categorize(self, message):
        msg = message.lower()
        for category, keywords in self.categories.items():
            if any(word in msg for word in keywords):
                return category
        return "Uncategorized"