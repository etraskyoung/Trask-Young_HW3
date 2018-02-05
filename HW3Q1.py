

class Patient:
    """ base Patient class """
    def __init__(self, name):
        self.name = name

    def discharge(self):
        """abstract metod to be overidden in derived classes
        :returns discharge type for patient derived classes"""
        raise NotImplementedError("This is an abstract metod and needs to be "
                                  "implemented in derived classes.")
class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.ExpectedCost = 2000

    def discharge(self):
        print(self.name, "Emergency")

class HospitalPatient(Patient):
    def _init_(self, name):
        Patient.__init__(self, name)
        self.ExpectedCost = 1000

    def discharge(self):
        print(self.name, "Admission")

class Hospital:
    def _init(self):
        self.cost = 0
        self.patients = []
        
    def admit(self, patients):
        self.patients.append(patients)

    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost += patients.ExpectedCost

    def get_total_cost(self):
      return self.cost


# Create Patients
P1 = EmergencyPatient('P1')
P2 = EmergencyPatient('P2')
P3 = EmergencyPatient('P3')
P4 = HospitalPatient('P4')
P5 = HospitalPatient('P5')


#Create Hospital
H1 = Hospital()

H1.admit(P1)
H1.admit(P2)
H1.admit(P3)
H1.admit(P4)
H1.admit(P5)

H1.discharge_all()


print(H1.get_total_cost())

