albums=[('Honestly Nevermind', 'Drake',2022), 
        ('Whole lotta red', 'Playboi Carti', 2019), 
        ('Graduation', 'Kanye West', 2007), 
        ('Melodic Blue', 'Baby Keem', 2015), 
        ('Heroes and Villains','Metro Boomin', 2023)]
name, artist, year= albums[0], albums[1], albums[2]

for album in albums:
    print('Album:{} Artist:{} Year:{}'.format(name,artist,year))