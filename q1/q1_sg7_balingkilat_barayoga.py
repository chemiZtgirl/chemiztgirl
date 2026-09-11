class Glassware:
    def __init__(self, capacity, full, holding):
        self.capacity = 60
        self.full = False
        self.holding = 0
 
        
class Beaker(Glassware):
    def __init__(self, capacity, full, holding, liquid):
        super().__init__(capacity, full, holding)
        self.liquid = liquid
    
    def fill_beaker(self, substance, amount):
        if self.full == True:
            print("This beaker is full, you cannot fill it anymore.")
            
        self.liquid = substance
        self.holding += amount
        
        if amount > self.capacity:
            print("Oh no, you added too much substance to the beaker and it overflowed!")
            self.full = True
            
        if self.holding == self.capacity:
            self.full = True

        
class Tray:
    def __init__(self, designation ,contents):
        self.designation = designation
        self.contents = []
    
    def add_beaker(self, beaker):
        if len(self.contents) >= 5:
            print("This tray is full, make another one.")
        else:
            self.contents.append(beaker)
            
    def __del__(self):
        print(f"Tray {designation} and its beakers are being disposed of.")
        
        del self.contents
        
         

