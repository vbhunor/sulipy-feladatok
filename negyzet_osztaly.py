class Negyzet:
    def __init__(self, oldal):
        self.oldal = oldal
        
    def kerulet(self):
        return self.oldal * 4
    
    def terulet(self):
        return self.oldal ** 2
    
