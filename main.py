from tinytag import TinyTag

tag: TinyTag = TinyTag.get('/media/Secondary/Music/sombr - I Barely Know Her/sombr - I Barely Know Her - 09 we never dated.flac')


while True:
    print("Input the file type: (album, track)")
    command : str = input()
    if command == "track":
        directory = input("Input track directory: ") 
        print(TinyTag.get(directory).artist)


