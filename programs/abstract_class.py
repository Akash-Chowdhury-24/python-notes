from abc import ABC, abstractmethod
class Vehical(ABC):
  def __init__(self,type):
    self.type = type
  @abstractmethod
  def start(self):
    pass
class Car(Vehical):
  def start(self):
    print(f"{self.type} car is starting with a key.")
    
c = Car("Sedan")
c.start()