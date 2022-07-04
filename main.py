from pytube import YouTube
import os

print('Jesli chesz pobrac piosenke wklej link i wcisnij ENTER, jesli chcesz zakonczyc wpisz "1" i wcisnij ENTER')

# pobranie linka od uzytkownika
link = input('Wklej link: ')
while link != "1":
    # tworzenie obiektu YouTube
    yt = YouTube(link)
    # pobranie filmu
    print('Pobieram: ', yt.title)
    plik = yt.streams.filter(only_audio=True).first().download('audio')
    # zapisanie pliku
    nazwa, rozsz = os.path.splitext(plik)
    nowy_plik = nazwa + '.mp3'
    os.rename(plik, nowy_plik)
    print("Pobieranie zakonczone!")
    # ponowne pobranie linku od uzytkownika
    link = input('Wklej link: ')

