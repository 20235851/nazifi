class AlertSystem:
    def check_abnormalities(self, data):
        alerts = []
        for record in data:
            if (
                record.heart_rate < 60 or record.heart_rate > 100 or
                record.blood_pressure > 140 or
                record.temperature > 37.5
            ):
                alerts.append(record)
        return alerts

    def generate_alert(self, patient, alerts):
        print(f"\n⚠ ALERT: Abnormal vitals detected for {patient.name}:")
        for alert in alerts:
            print("  ->", alert)