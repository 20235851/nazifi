from datetime import datetime

class VitalSignData:
    def __init__(self, heart_rate, blood_pressure, temperature):
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.temperature = temperature
        self.timestamp = datetime.now()

    def _str_(self):
        return (
            f"HR: {self.heart_rate} bpm, "
            f"BP: {self.blood_pressure}, "
            f"Temp: {self.temperature}°C "
            f"at {self.timestamp}"
        )