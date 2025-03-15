class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def setTitle(self, title):
        self.title = title

    def setAuthor(self, author):
        self.author = author

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author