from apis import spotify
from apis import twilio

user_selections = {
    'genres': [],
    'artists': []
}


def print_menu():
    print('''
---------------------------------------------------------------------
Settings / Browse Options
---------------------------------------------------------------------
1 - Select your favorite genres
2 - Select your favorite artists
3 - Discover new music
4 - Quit
---------------------------------------------------------------------
    ''')


def handle_genre_selection():
    print('Handle genre selection here')
    # 1. Allow user to select one or more genres using the
    #    spotify.get_genres_abridged() function
    # 2. Allow user to store / modify / retrieve genres
    #    in order to get song recommendations


def handle_artist_selection():
    print('Handle artist selection here...')
    # 1. Allow user to search for an artist using
    #    spotify.get_artists() function
    # 2. Allow user to store / modify / retrieve artists
    #    in order to get song recommendations


def get_recommendations():
    print('Handle retrieving a list of recommendations here...')
    # 1. Allow user to retrieve song recommendations using the
    #    spotify.get_similar_tracks() function
    # 2. List them below

genres=[]
artists=[]
counter=1
singers={}



# Begin Main Program Loop:
while True:


    
    print_menu()
    choice = input('What would you like to do? ')
    if choice == '1':
        
        for genre_names in spotify.get_genres_abridged():
            print(genre_names)
        genre=input("Pick a genre! ")
        print("To clear your genres, type 'clear'!")
        genres.append(genre)
        if genre == "clear":
            genres=[]
        print("Your genres: ", genres)
        clear_list_option= input("Do you want to clear your list? Say 'yes' or 'no' ")
        if clear_list_option=="yes":
            genres=[]
            print("Your genres: ", genres)
        if clear_list_option=="no":
            continue


        
    elif choice == '2':
        artist=input("Search for an artist! ")
        for name in spotify.get_artists(artist):
            singers[counter] = name.get('name')
            print(counter, name.get('name'))
            counter = counter + 1
        
        artist_number=int(input("Pick the number corresponding with the artist! "))
        artists.append(singers.get(artist_number))
        print("Your artists: ", artists)
        clear_list_option= input("Do you want to clear your list? Say 'yes' or 'no' ")
        if clear_list_option=="yes":
            artists=[]
            print("Your artists: ", artists)
        if clear_list_option=="no":
            continue


        
    elif choice == '3':
        track=input("Name a song! ")
        for ids in spotify.get_tracks(track):
           track_ids=ids.get('id')
        for IDs in spotify.get_artists(artist):
            artist_id=IDs.get('id')
        results = spotify.get_similar_tracks(track_ids=[track_ids],artist_ids=[artist_id],
                                             genres=[genre])
        print(spotify.get_formatted_tracklist_table(results))
        answer=input("Do you want to send these cool tracks to someone? Type 'yes' or 'no' ")
        if answer=="yes":
            email=input("What's they're email adress? ")
            twilio.send_mail(
                email,"Cool songs",spotify.get_formatted_tracklist_table_html(results))
        else:
            continue


 
    elif choice == '4':
        print('Quitting...')
        break
    else:
        print(choice, 'is an invalid choice. Please try again.')
    print()
    input('Press enter to continue...')
