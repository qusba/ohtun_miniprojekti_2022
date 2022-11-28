class Bookref:
    def __init__(self, key: str, author: str, title: str, year: int, publisher: str ):
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
        return f"author: {self.author}, title: {self.title}, year: {str(self.year)}, publisher: {self.publisher}"

    def __lt__(self, other):
         return self.author < other.author