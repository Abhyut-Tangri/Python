import random

class Enemy(object):
    
    def __init__(self,name='Enemy',hit_point=0,lives=1) :
        self._name=name
        self._hit_point=hit_point
        self._lives=lives
        self._alive=True
        
    def take_damage(self,damage):
        remaining_points=self._hit_point-damage
        if remaining_points >=0:
            self._hit_point=remaining_points
            print('OW! I took {} points damage and have {} left '.format(damage,remaining_points))
        else:
            self._lives-=1
            if self._lives>0:
                print('{0._name} lost a life'.format(self))
            else:
                print('{0._name} is dead :('.format(self))
                self._alive=False
                self._hit_point=0
        
    
    def __str__(self):
        return 'Name:{0._name}, Lives {0._lives}, Hit points:{0._hit_point}'.format(self)


class Troll(Enemy):
    def __init__(self, name):
        #super(Troll,self).__init__(self,name=name,lives=1,hit_point=23)
        super().__init__(name=name,lives=1,hit_point=23)
        
    
    def grunt(self):
        print('Me {0._name}. {0._name} stomp you'.format(self))

class Vampire(Enemy):
    def __init__(self,name):
        super().__init__(name=name,lives=3,hit_point=15)
        
    def scary_line(self):
        print('The great {0._name} will send you to the grave!!! Ready to get your blood sucked?'.format(self))
     
     
    def dodges(self):
        if random.randint(1,3)==3:
            print('******* {0._name} dodges*******'.format(self))
            return True
        else:
            return False
    
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)

class VampKing(Vampire):
    
    def __init__(self, name):
        super().__init__(name)
        self._hit_point=140
        
    def take_damage(self, damage):
        return super().take_damage(damage//4)
    
    def thesuperscaryline(self):
        print('{0._name} is the king of all vampires! Fear my wrath as i avenge my fallen subjects'.format(self))
        
    
    
        