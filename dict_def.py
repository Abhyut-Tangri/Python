from contents import pantry


chicken_quantity=pantry.setdefault('chicken',0)
print(f'chicken: {chicken_quantity}')

bean_quantity=pantry.setdefault('bean',0)
print(f'beans: {bean_quantity}')

ketchip_quantity=pantry.get('ketchup',0)
print(f'ketchup:{ketchip_quantity}')

z_quantity=pantry.setdefault('zucchini','eight')
print(f'zucchini:{z_quantity}')

print()
print('"pantry" now contains...')

for key, value in sorted(pantry.items()):
    print(key,value)
    