try:
    from pytube import YouTube
except:
    import os
    os.system('pip install pytube')
    from pytube import YouTube

while True:
    link = input('- Introduce la URL del vídeo: ')
    yt = YouTube(link)

    descargar = input('- ¿Cómo lo quieres descargar (música o vídeo)? Escribe m/v: ')
    
    if descargar == 'm':
        audios = yt.streams.filter(only_audio = True)
        for i in audios:
            print(i)

        elegir = input('- Elige el itag: ')
        guardar = input('- ¿Dónde lo quieres guardar? ')
        yt.streams.filter(only_audio = True).get_by_itag(elegir).download(guardar)
        print('''- Descargado con exito.
    - Recuerda cambiar el formato a .wav para que funcione correctamente.''')

    elif descargar == 'v':
        videos = yt.streams.filter(only_video = True)
        for i in videos:
            print(i)

        elegir = input('- Elige el itag: ')
        guardar = input('- ¿Dónde lo quieres guardar? ')
        yt.streams.filter(only_video = True).get_by_itag(elegir).download(guardar)

