from Vitalsign import VitalSignData

class Patient:
    def __init__(self, patient_id, name, age, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def get_latest_data(self):
        data_records = []
        for device in self.devices:
            data_records.append(device.record_data())
        return data_records