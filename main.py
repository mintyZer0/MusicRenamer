from tinytag import TinyTag
from pathlib import Path
from naming_template import NamingTemplate

tag: TinyTag = TinyTag.get('/media/Secondary/Music/sombr - I Barely Know Her/sombr - I Barely Know Her - 09 we never dated.flac')

def is_first_run():
    config_file = Path("config.ini")
    if config_file.exists():
        return False
    else:
        config_file.touch()
        return True

def get_directory_path(type: str):
    path = input(f"Input {type} path:")
    return path

def get_list_of_items(path: str):
    valid_files = (
    '.mp3', '.wav', '.flac', '.aac', '.ogg', '.oga', '.opus', '.m4a', '.m4b', 
    '.m4p', '.wma', '.aiff', '.alac', '.ape', '.wv', '.tta', '.mpc', '.webm',
    '.3gp', '.aa', '.aax', '.act', '.amr', '.awb', '.au', '.dss', '.dvf', 
    '.gsm', '.iklax', '.ivs', '.mmf', '.movpkg', '.mp1', '.mp2', '.msv', 
    '.nmf', '.mogg', '.ra', '.rm', '.raw', '.rf64', '.sln', '.voc', '.vox', 
    '.8svx', '.cda')
    directory = Path(path)
    list_of_items = [i for i in directory.iterdir() if i.is_file() and i.suffix in valid_files]
    return list_of_items

def rename(path: str, type: str, naming_template: NamingTemplate):
    list_of_items = get_list_of_items(path)
    if type == "album":
        for file in list_of_items:
            tag : TinyTag = TinyTag.get(file)
            tag_list = [getattr(tag,i) if i in naming_template.metadata_available else i for i in naming_template.get_template()] # type: ignore
            new_name : str = " ".join(tag_list)
            file.rename(f"{new_name}") 
            

def create_naming_template(template_input):
        naming_template : NamingTemplate = NamingTemplate(template_input)
        return naming_template
        
    

while True:
    print("-"*5 + "Music Renamer" + "-"*5)

    if is_first_run():
        print("Please create a naming template")
        template_input = input("")
        naming_template = create_naming_template(template_input)

    print("(1) Create naming template")
    print("(2) Change file names")
    command : str = str(input().lower())
    
    if command == "q" or command == "quit":
        break

    elif command == ("1"):
        while True:
            print("Create your naming template: ", end="")
            template_input = input("")
            if template_input == ("?"):
                print(NamingTemplate.metadata_available)
                print("Example: albumartist - track title")
                continue
            naming_template = create_naming_template(template_input)         
            break
        
    elif command == ("2"): 
        while True:
            print("Choose type:(album, track)")
            command = input()
            if command == "album":
                path = get_directory_path(command)
                rename(path, command, naming_template)
                break

            elif command == "track":
                path = get_directory_path(command)
                rename (path, command, naming_template)
                break

