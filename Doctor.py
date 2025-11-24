class Doctor:
    def __init__(self, doctor_id, name):
        self.doctor_id = doctor_id
        self.name = name

    def review_alert(self, alerts):
        print(f"\nDoctor {self.name} reviewing alerts...")
        for alert in alerts:
            print("  - Abnormal data:", alert)

    def give_recommendation(self, patient):
        print(f"\nRecommendation for {patient.name}:")
        print(" - Schedule a follow-up checkup.")
        print(" - Monitor vitals closely for 24 hours.")