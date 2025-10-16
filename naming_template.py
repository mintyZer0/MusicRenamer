from tinytag import TinyTag
import string
class NamingTemplate:
    metadata_available : list = ["album", "albumartist", "artist", "comment", "composer", "disc", "disk_total", "genre", "title", "track", "track_total", "year"]
    valid_characters : list = list(string.ascii_letters + "-_().',!")

    def __init__(self, template: str) -> None:
        parts = template.strip().split(" ")
        self.template_list = [i for i in parts if i in self.metadata_available or i in self.valid_characters]

    def __str__(self):
        return str(self.template_list)

    def get_template(self):
        return self.template_list


if __name__ == "__main__":
    name : NamingTemplate = NamingTemplate("album - albumartist") 
    print(name)