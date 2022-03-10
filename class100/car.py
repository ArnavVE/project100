class Car():
    def __init__(self,color,name,model):
        self.color=color
        self.name=name
        self.model=model

    def start(self):
        print("car has started")

car1=Car("red",1,"sla")
print(car1.start())
