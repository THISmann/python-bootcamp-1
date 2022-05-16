from exo2.py import Dog 

class PetDog(Dog):
    def __init__(self,  name, age, weight ,trained):
        super().__init__(name, age, weight )
        self.trained = False 
        
    def train(self):
        print(self.name.bark())
        
    def play(self, *args):
        print({})
            
        