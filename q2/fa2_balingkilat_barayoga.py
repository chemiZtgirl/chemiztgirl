class Patient():
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = float(0)
        self.set_bill_amount(bill_amount)
    
    
    def set_name(self, name):
        self.name = name
    
    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.bill_amount = bill_amount
        
    
    def get_name(self):
        print(f"Patient name: {self.name}")
    
    def get_bill(self):
        print(f"Patient bill: {self.bill_amount}")
        
    
    def calc_bill(self):
        print(f"Original Bill: {self.bill_amount}\nFinal Bill: {self.bill_amount}\n")
        

class Senior(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        
    def calc_bill(self):
        print(f"Original Bill: {self.bill_amount}\nFinal Bill: ", (self.bill_amount - (self.bill_amount*0.20)), "\n")
        
    

class Philhealth(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)
        
    def calc_bill(self):
        print(f"Original Bill: {self.bill_amount}\nFinal Bill: ", (self.bill_amount - (self.bill_amount*0.15)), "\n")
        
p1 = Patient("Ate", 1300)
p1.get_name()
p1.get_bill()
p1.calc_bill()


p2 = Senior("Lola", 1500)
p2.get_name()
p2.get_bill()
p2.calc_bill()


p3 = Philhealth("Kuya", 1550)
p3.get_name()
p3.get_bill()
p3.calc_bill()

    