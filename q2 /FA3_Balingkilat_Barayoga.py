from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        print("[phSensor] Reading: 7.2 PH (Neutral) ")

class TempSensor(Sensor):
    def get_reading(self):
        print("[tempSensor] Reading:24.5 degrees Celsius")
        
msens = PHSensor()
qsens = TempSensor()

msens.get_reading()
qsens.get_reading()
