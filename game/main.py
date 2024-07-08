from players import Player

from enemy import Enemy,Troll,Vampire,VampKing

abhi=Player('Abhi')

# random_monster=Enemy('Basic Enemy',12,1)
# print(random_monster)

# random_monster.take_damage(4)
# print(random_monster)

# random_monster.take_damage(10)
# print(random_monster)

ugly_troll=Troll('Pug')
print('ugly troll -{}'.format(ugly_troll))

another_troll=Troll('ug')
print('another troll - {}'.format(another_troll))

brother=Troll('Urg')
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

brother.take_damage(30)
print(brother)

the_first=Vampire('Russo')
print(the_first)

the_first.scary_line()
print('*'*40)
# while the_first.alive:        
#     the_first.take_damage(1)


the_first._lives=0
the_first._hit_point=1
print(the_first)

vlad=VampKing('Vlad')
print(vlad)

vlad.thesuperscaryline()

vlad.take_damage(4)
    
# print(abhi.name)
# print(abhi.lives)
# abhi.lives-=1
# print(abhi.lives)

# abhi.lives-=1
# print(abhi)

# abhi.lives-=1
# print(abhi)


# abhi.lives-=1
# print(abhi)

# abhi._lives=9
# print(abhi)

# abhi.level+=5
# print(abhi)

print()

print('*'*40)

a=3
b='tom'
c=1,2,3

print(a)
print(b)
print(c)