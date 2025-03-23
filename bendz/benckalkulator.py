
class kalkulator():

    def __init__(self, reps, weight):
        self.weight = weight
        self.reps = reps
        
    def calculate_1rpm(self):
        
        one_rpm = self.weight * (1 + (self.reps / 30))
        
        return one_rpm
    
