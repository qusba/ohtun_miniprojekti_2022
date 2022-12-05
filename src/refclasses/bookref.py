class Bookref:
    def __init__(self, key: str, author: str, title: str, year: int, publisher: str ):
        self.type = "book"
        self.key = key
        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher

    def get_key(self):
        return self.key

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def __str__(self):
        return f"\033[0;33mkey\033[0m: \033[1;31m{self.key}\033[0m, \033[0;33mauthor\033[0m: \033[1;32m{self.author}\033[0m, \033[0;33mtitle\033[0m: \033[1;34m{self.title}\033[0m, \033[0;33myear\033[0m: \033[1;35m{str(self.year)}\033[0m, \033[0;33mpublisher\033[0m: \033[1;36m{self.publisher}\033[0m"

    def __lt__(self, other):
         return self.author < other.author