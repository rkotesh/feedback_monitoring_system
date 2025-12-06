class SentimentAnalyzer:
    positive_words = {"good", "great", "excellent", "love", "happy", "amazing"}
    negative_words = {"bad", "worst", "delay", "poor", "angry", "issue", "problem"}


    def analyze(self, message):
        msg = message.lower()


        if any(word in msg for word in self.negative_words):
            return -1, "Negative"
        elif any(word in msg for word in self.positive_words):
            return 1, "Positive"
        return 0, "Neutral"