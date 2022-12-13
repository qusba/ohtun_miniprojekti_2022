class Bookref:
    def __init__(self, key: str, author_first_name: str, author_last_name: str, title: str, year: int, publisher: str):
        self.type = "book"
        self.key = key
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.title = title
        self.year = year
        self.publisher = publisher
        self.tags = []

    def set_tags(self, tags):
        self.tags = tags

    def get_key(self):
        return self.key

    def get_author_first_name(self):
        return self.author_first_name

    def get_author_last_name(self):
        return self.author_last_name

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher
    
    def get_tags(self):
        return self.tags

    def __str__(self):
        return (f"\033[0;33mkey\033[0m: \033[1;31m{self.key}\033[0m, \033[0;33mauthor\033[0m: \033[1;32m{self.author_first_name}\033[0m, \033[1;32m{self.author_last_name}\033[0m, \033[0;33mtitle\033[0m: \033[1;34m{self.title}\033[0m, \033[0;33myear\033[0m: \033[1;35m{str(self.year)}\033[0m, \033[0;33mpublisher\033[0m: \033[1;36m{self.publisher}\033[0m")

    def __lt__(self, other):
        return self.author < other.author
