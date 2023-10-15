class vehicles:
    def __init__(self,name,milage,capacity):
        self.name=name
        self.milage=milage
        self.capacity=capacity
class bus (vehicles):
    pass
school_bus=bus("g.g.h.s" ,123,67)
print(isinstance(school_bus,vehicles))