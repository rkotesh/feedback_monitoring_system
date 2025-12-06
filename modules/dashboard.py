from collections import Counter


class Dashboard:
    def show(self, entries, alert_count):
        sentiments = Counter(e['sentiment_type'] for e in entries)
        categories = Counter(e['category'] for e in entries)

        print("\n📊 DASHBOARD SUMMARY")
        print("=" * 30)
        print(f"Positive: {sentiments.get('Positive', 0)}")
        print(f"Neutral: {sentiments.get('Neutral', 0)}")
        print(f"Negative: {sentiments.get('Negative', 0)}")

        print("\nCategory Distribution:")
        for cat, count in categories.items():
            print(f"- {cat}: {count}")

        print(f"\n🚨 Alerts Triggered Today: {alert_count}")
