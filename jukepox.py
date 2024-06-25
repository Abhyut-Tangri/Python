from nested_looops import albums
INDEX_LIST_SONGS=3
SONG_TITLE_INDEX=1
while True:
    print('please choose your album(if not displayed program will exit):')
    for index, (title, artist, year, songs) in enumerate(albums):
        print('{}: {}'.format(index+1,title))
    choice=int(input())
    if 1<=choice<=len(albums):
        songs_list=(albums[choice-1][3])
    
    else:   
        break
    print('choose a song ')
    for index,(track_number,song) in enumerate(songs_list):
        print('{}:{}'.format(index+1,song))
    song_choice=int(input())
    if 1<=song_choice<=len(songs_list):
        title=songs_list[song_choice-1][SONG_TITLE_INDEX]
    else:
        continue
    print('playing {}'.format(title))
    print('='*40)
          

    