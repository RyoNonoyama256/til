from typing import List

class Human(object):
    def __init__(self, name):
        self.name = name

class Patient(Human):
    current_id = 100

    def __init__(self, name):
        super().__init__(name)
        self.symptom = None
        self.patient_id = Patient.current_id
        Patient.current_id += 1

class Clinic(object):
    def __init__(self):
        self.patients_list: List[Patient] = []

    def show_waiting_count(self):
        print(f"Num of people waiting: {len(self.patients_list)}")

    def reserve(self, patient: Patient):
        if not self._check_reserved(patient):
            self.patients_list.append(patient)
        else:
            print(f"{patient.name} has already made a reserveation.") 

    def diagnosis(self, patient: Patient=None):
        if len(self.patients_list) == 0:
            print("There are no patients to examine.")
            return
        if patient is not None and not self._check_reserved(patient):
            print(f"{patient.name} is not on the reservation list.")
            return
        
        target_patient = patient if patient else self.patients_list[0]
        print(f"=======\nID: {target_patient.patient_id}")
        print(f"Name: {target_patient.name}")
        target_patient.symptom = input("Symptom: ")
        self._remove_patient(target_patient)

    def _check_reserved(self, patient: Patient):
        return any(p.patient_id == patient.patient_id for p in self.patients_list)

    def _remove_patient(self, patient: Patient):
        self.patients_list = [p for p in self.patients_list if p.patient_id != patient.patient_id]

if __name__ == "__main__":
    myclinic = Clinic()
    # 患者を作成
    patient_list = [Patient(name) for name in ["佐藤", "田中", "鈴木", "山田"]]
    # 診察を予約
    for patient in patient_list:
        myclinic.reserve(patient)
    # 待ち人数の表示
    myclinic.show_waiting_count()
    # 予約済み患者の予約
    myclinic.reserve(patient_list[0])
    # 患者の診察（患者指定あり）
    myclinic.diagnosis(patient_list[2])
    # 待ち人数の表示
    myclinic.show_waiting_count()
    # 患者の診察（患者指定なし）
    myclinic.diagnosis()
    # 待ち人数の表示
    myclinic.show_waiting_count()
