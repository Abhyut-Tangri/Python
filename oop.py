#a=12
#b=3

#print(a+b)
#print(a.__add__(b))

class kettle(object):
    
    power_source='electricity'
    
    def __init__(self,make,price) -> None:
        self.make=price
        self.price=price
        self.on=False
        
    
    def switch_on(self):
        self.on=True
        

kenwood=kettle('Kenwood',8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price=12.75
print(kenwood.price)

hamilton=kettle('Hamilton',14.55)

print('Models:{}={},{}={}'.format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))
#print('Models: {}={0,price},{1,make}= {1,price}'.format(kenwood,hamilton))


"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)


kettle.switch_on(kenwood)
print(kenwood.on)


print('*'*80)

kettle.power=1.5
# or 
kenwood.power=1.5
hamilton.power=1.5
print(kenwood.power)
print(hamilton.power)

print('switching to atomic power')
kettle.power_source='atomic'

print(kettle.power_source)
print('switching kenwood to gas')
kenwood.power_source='gas'
print(kenwood.power_source)
print(hamilton.power_source)
print(kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

