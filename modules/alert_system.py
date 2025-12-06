import logging


class AlertSystem:
    def __init__(self):
        logging.basicConfig(
            filename="logs/negative_alerts.log",
            level=logging.INFO,
            format="%(asctime)s - %(message)s"
        )

        self.customer_complaints = {}
        self.alert_count = 0

    def log_negative(self, entry):
        self.alert_count += 1
        
        cid = entry['customer_id']
        self.customer_complaints[cid] = self.customer_complaints.get(cid, 0) + 1

        urgent = "URGENT" if self.customer_complaints[cid] > 1 else "NORMAL"

        logging.info(f"[{urgent}] Customer {cid}: {entry['message']}")
