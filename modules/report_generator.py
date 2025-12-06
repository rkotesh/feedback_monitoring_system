from collections import Counter
import os


class ReportGenerator:
    def generate(self, entries):
        # Count sentiments
        pos = sum(1 for e in entries if e['sentiment_score'] == 1)
        neu = sum(1 for e in entries if e['sentiment_score'] == 0)
        neg = sum(1 for e in entries if e['sentiment_score'] == -1)

        # Count categories
        categories = Counter(e['category'] for e in entries)
        most_common_category = categories.most_common(1)[0][0] if categories else "None"

        # Ensure output folder exists
        os.makedirs("output", exist_ok=True)

        # Write report
        with open("output/daily_feedback_report.txt", "w", encoding="utf-8") as f:
            f.write("DAILY FEEDBACK REPORT\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Positive Feedback: {pos}\n")
            f.write(f"Neutral Feedback: {neu}\n")
            f.write(f"Negative Feedback: {neg}\n\n")
            f.write(f"Most Common Category: {most_common_category}\n")
