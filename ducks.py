class Wing(object):
    
    
    def __init__(self,ratio):
        self.ratio=ratio
    
    
    def fly(self):
        if self.ratio>1:
            print('weee this is fun')
        elif self.ratio==1:
            print('this is hard work but im flying')
        else:
            print('i think i will just fly')   
class Duck(object):
    def __init__(self):
        self._wing=Wing(1.8)
        
        
    def walk(self):
        print('waddle,waddle,waddle')
        
        
    def swim(self):
        print('Come on in the water is lovely')
        
        
    def quack(self):
        print('Quack Quack')
        
    
    def fly(self):
        self._wing.fly()


class Penguin(object):
    def walk(self):
        print('Waddle waddle I waddle too')
    
    
    def swim(self):
        print('Come on in, but its only a bit chilly this far south')


    def quack(self):
        print('are you avin a larf? im a penguin!')
        
    
# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()
    

if __name__ == '__main__':
    donald=Duck()
    donald.fly()

    
    # percy=Penguin()
    # test_duck(percy)