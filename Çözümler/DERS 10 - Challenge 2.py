albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

SONGS_LIST_INDEX = 3 # albüm tupleları içerisinde şarkı tupleları listesi 3. indexte buluyor
SONG_TITLE_INDEX = 1  # ornegin (1, "Psycho") 'dan 1. index yani şarkı ismini almak için const oluşturduk

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))  # Albüm listesini yazdırıyor

    choice = int(input())  # albüm listesinden sonra input alıyoruz
    if 1 <= choice <= len(albums):  # görülen sayılardan biri girilmişse
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]  # index o sayının bir eksiği oluyor, o albümün indexindeki tupleı ilk [] ile bulup ikinci [] ile de şarkı listesine ulaşıyoruz (aşağıda kullanacağız)
    else: # albüm listesinden albüm seçimine ordaki sayılardan girilmezse program sonlanır
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song)) # şarkı listesini yazdırıyor

    song_choice = int(input())  # şarkı seçimi istiyor
    if 1 <= song_choice <= len(songs_list): # görülen sayılardan biri girilmişse
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX] # index o sayının bir eksiği oluyor, şarkı listesinde seçilen şarkının indexindeki şarkı tupleını ilk [] ile bulup ikinci [] ile de şarkı ismine ulaşıyoruz
        print("Playing {}".format(title))
        print("=" * 40)
    else:
        continue # şarkı seçininde orada görünen sayılardan farklı bir şey girilmişse while döngüsüne devam ediyor (tekrardan albüm listesi seçimi isteyecek yani başa dönüyor)