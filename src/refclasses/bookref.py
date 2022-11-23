class Bookref:
    def __init__(self, author: str, title: str, year: int, publisher: str ):
        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher

    def get_author(self):
        return self.author

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def __str__(self):
        return "author: "f"{self.author}" + ", title: " + f"{self.title}" + ", year: " + f"{str(self.year)}" + ", publisher: " + f"{self.publisher}"

    def __lt__(self, other):
         return self.author < other.author