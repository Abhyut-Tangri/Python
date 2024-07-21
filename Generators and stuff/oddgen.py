def odds():
    num=1
    while True:
       yield num
       num+=2


def pi_series():
    oddnumners=odds()
    approximation=0
    while True:
        approximation+=(4/next(oddnumners))
        yield approximation
        approximation-=(4/next(oddnumners))
        yield approximation

odd=odds()

for i in range(50):
    print(next(odd))

aprox_pi=pi_series()
for x in range(10):
    print(aprox_pi)