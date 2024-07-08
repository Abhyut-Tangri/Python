class Player(object):
    
    def __init__(self,name):
        self.name=name
        self._lives=3
        self._level=1
        self._score=0
    
    def _get_lives(self):
        return self._lives
    
    def _set_lives(self,lives):
        if lives >= 0:
            self._lives=lives
        else:
            print('lives cannot be negative')
            self._lives=0
            
    def _get_levels(self):
        return self._level
    
    def _set_levels(self,level):
        if level>0:
            delta=level-self._level
            self.score+=delta*1000
            self._level=level
        else:
            print('level cannot be less that 1')
            
    
    lives=property(_get_lives,_set_lives)

    level=property(_get_levels,_set_levels)

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        self._score=score
    
    def __str__(self):
        return 'Name: {0.name}, Lives: {0.lives}, Level {0.level}, Score{0.score}'.format(self)
    