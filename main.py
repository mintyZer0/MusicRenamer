from tinytag import TinyTag
from pathlib import Path
import configparser
from naming_template import NamingTemplate

tag: TinyTag = TinyTag.get('/media/Secondary/Music/sombr - I Barely Know Her/sombr - I Barely Know Her - 09 we never dated.flac')
config = configparser.ConfigParser()

def is_first_run() -> bool:
    config_file = Path("config.ini")
    if config_file.exists():
        return False
    else:
        config_file.touch()
        return True

def get_directory_path(type: str) -> str:
    path = input(f"Input {type} path:")
    return path

def get_list_of_files(path: str) -> list:
    valid_files = (
    '.mp3', '.wav', '.flac', '.aac', '.ogg', '.oga', '.opus', '.m4a', '.m4b', 
    '.m4p', '.wma', '.aiff', '.alac', '.ape', '.wv', '.tta', '.mpc', '.webm',
    '.3gp', '.aa', '.aax', '.act', '.amr', '.awb', '.au', '.dss', '.dvf', 
    '.gsm', '.iklax', '.ivs', '.mmf', '.movpkg', '.mp1', '.mp2', '.msv', 
    '.nmf', '.mogg', '.ra', '.rm', '.raw', '.rf64', '.sln', '.voc', '.vox', 
    '.8svx', '.cda')
    directory = Path(path)
    list_of_files = [i for i in directory.iterdir() if i.is_file() and i.suffix in valid_files]
    return list_of_files

def _rename_indiv_file(file : Path, naming_template: NamingTemplate) -> None:
        tag : TinyTag = TinyTag.get(file)
        tagged_name : list = [getattr(tag,i) if i in naming_template.metadata_available else i for i in naming_template.get_template()]
        new_name : str = " ".join(tagged_name) + file.suffix
        new_path : Path = file.with_name(new_name)
        file.rename(new_path) 
 
def rename(path: str, type: str, naming_template: NamingTemplate) -> None:
    if type == "album":
        list_of_files = get_list_of_files(path)
        for file in list_of_files:
            _rename_indiv_file(file, naming_template) 

    if type == "track":
        file = Path(path)
        _rename_indiv_file(file, naming_template) 

def create_naming_template(template_input) -> NamingTemplate:
        naming_template : NamingTemplate = NamingTemplate(template_input)
        naming_template_string : str = " ".join(naming_template.get_template())
        config["NamingTemplate"] = {
            'template': naming_template_string
        }
        write_to_config('config.ini')
        return naming_template
        
def write_to_config(config_file_path: str) -> None:
    with open (config_file_path, 'w') as configfile:
        config.write(configfile)
        
def read_config(config_file_path: str) -> None:
    config.read(config_file_path)

while True:
    print("-"*5 + "Music Renamer" + "-"*5)
    if is_first_run():
        print("Please create a naming template")
        template_input = input("")
        naming_template = create_naming_template(template_input)
    else:
        read_config('config.ini')
        naming_template = NamingTemplate(config.get("NamingTemplate", "template"))
    

    print("(1) Create naming template")
    print("(2) Change file names")
    print("(3) See current naming template")
    command : str = str(input().lower())
    
    if command == "q" or command == "quit":
        break

    elif command == "1":
        while True:
            print("Create your naming template: ", end="")
            template_input = input("")
            if template_input == ("?"):
                print(NamingTemplate.metadata_available)
                print("Example: albumartist - track title")
                continue
            naming_template = create_naming_template(template_input)         
            break
        
    elif command == "2": 
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
            
    elif command == "3":
        read_config('config.ini')
        print(config.get('NamingTemplate', "template"))


