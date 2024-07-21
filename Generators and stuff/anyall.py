entries=[1,2,3,4,5]

print('all:{}'.format(all(entries)))
print('any:{}'.format(any(entries)))

print('iterables wit a false value')
entries_with_zero=[1,2,3,0]

print('all:{}'.format(all(entries_with_zero)))
print('any:{}'.format(any(entries_with_zero)))
