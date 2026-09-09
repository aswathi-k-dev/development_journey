from abc import ABC,abstractmethod
class Car(ABC):

    @abstractmethod
    def start(self):pass

    @abstractmethod
    def accelerate(self):pass

    @abstractmethod
    def  stop(self):pass

class Baleno(Car):

    def start(self):
        print("baleno car starts")
    def accelerate(self):
        print("baleno car accelerates")
    def stop(self):
        print("baleno car stop")
        

baleno_instance = Baleno()
baleno_instance.start()
baleno_instance.stop()
baleno_instance.accelerate()