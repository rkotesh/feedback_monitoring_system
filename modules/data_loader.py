import csv
import os


class DataLoader:
    def load_text_file(self, filepath):
        entries = []
        if not os.path.exists(filepath):
            return entries

        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                parsed = line.strip().split(" | ")
                if len(parsed) == 3:
                    timestamp, customer_id, message = parsed
                    entries.append({
                        "timestamp": timestamp,
                        "customer_id": customer_id,
                        "message": message
                    })
        return entries

    def load_csv_file(self, filepath):
        entries = []
        if not os.path.exists(filepath):
            return entries

        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                entries.append({
                    "timestamp": row.get("timestamp", ""),
                    "customer_id": row.get("customer_id", ""),
                    "message": row.get("message", "")
                })
        return entries

    def load_all(self):
        data = []
        data.extend(self.load_text_file("data/feedback_today.txt"))
        data.extend(self.load_text_file("data/chat_logs.txt"))
        data.extend(self.load_csv_file("data/email_feedback.csv"))
        return data
    def save_processed_data(self, entries, output_filepath):
        with open(output_filepath, "w", encoding="utf-8", newline='') as f:
            fieldnames = ["timestamp", "customer_id", "message", "sentiment_score", "sentiment_type", "category"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for entry in entries:
                writer.writerow(entry)