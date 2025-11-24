from Patient import Patient
from Device import Device
from Doctor import Doctor
from AlertSystem import AlertSystem


patient = Patient(1, "John Doe", 45, "Hypertension")
doctor = Doctor(101, "Dr. Smith")
alert_system = AlertSystem()


device1 = Device("D100", "Smart Watch", patient)
device2 = Device("D200", "BP Monitor", patient)

patient.add_device(device1)
patient.add_device(device2)


data = patient.get_latest_data()

alerts = alert_system.check_abnormalities(data)

if alerts:
    alert_system.generate_alert(patient, alerts)
    doctor.review_alert(alerts)
    doctor.give_recommendation(patient)
else:
    print("All vitals normal.")