import csv
country_dict={}
country_filename='country_info.txt'

dialect=csv.excel
dialect.delimiter='|'
with open(country_filename, encoding='utf-8', newline='') as country_challenge:
    headings=country_challenge.readline().strip('\n').split(dialect.delimiter)
    for index,heading in enumerate(headings):
        headings[index]=heading.casefold()
    reader=csv.DictReader(country_challenge, delimiter='|')
    country_challenge.readline()
    for row in country_challenge:
        data=row.strip('\n').split('|')
        country,capital,code,code3,dialing,timezone,currency=data
        country_dict={
            'name':country,
            'capital':capital,
            'country_code': code,
            'cc3':code3,
            'dialing_code':dialing,
            'timezone':timezone,
            'currency':currency
        }
