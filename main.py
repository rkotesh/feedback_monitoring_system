import os
from modules.data_loader import DataLoader
from modules.sentiment_analyzer import SentimentAnalyzer
from modules.categorizer import Categorizer
from modules.alert_system import AlertSystem
from modules.report_generator import ReportGenerator
from modules.dashboard import Dashboard


def main():
    print("🔍 Running Real-Time Customer Feedback Analyzer...")

    os.makedirs("data", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    loader = DataLoader()
    feedback_entries = loader.load_all()

    analyzer = SentimentAnalyzer()
    categorizer = Categorizer()
    alert_system = AlertSystem()

    processed_entries = []

    for entry in feedback_entries:
        sentiment_score, sentiment_type = analyzer.analyze(entry['message'])
        category = categorizer.categorize(entry['message'])

        entry.update({
            "sentiment_score": sentiment_score,
            "sentiment_type": sentiment_type,
            "category": category
        })

        if sentiment_score == -1:
            alert_system.log_negative(entry)

        processed_entries.append(entry)

    report = ReportGenerator()
    report.generate(processed_entries)

    dashboard = Dashboard()
    dashboard.show(processed_entries, alert_system.alert_count)

    print("Processing Complete. Check 'output/' and 'logs/' folders.")


if __name__ == "__main__":
    main()
