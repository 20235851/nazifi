from Vitalsign import VitalSignData
import random

class Device:
    def __init__(self, device_id, type, patient=None):
        self.device_id = device_id
        self.type = type
        self.patient = patient

    def record_data(self):
        # Generate simulated values
        heart_rate = random.randint(50, 120)
        blood_pressure = random.randint(90, 180)
        temperature = round(random.uniform(35.0, 40.0), 1)

        return VitalSignData(heart_rate, blood_pressure, temperature)