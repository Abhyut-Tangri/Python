from medalsdata import medals_table


def sort_key(d:dict)->str:
    return d['country']


medals_table.sort(key=lambda d:d['country'])
print(medals_table)
