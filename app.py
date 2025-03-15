from flask import Flask, render_template
from Books_Class import Book # Importing the Book class from the Book_Class.py file.

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html', bookList=books)

# Route for books page.
# /books will display the title and author attributes from the books list.
# List will be a list of Book objects from the Books class that we imported.
@app.route('/books')
def books():
    books = []

    books.append(Book("The Catcher in the Rye", "J. D. Salinger"))
    books.append(Book("The Handmaid's Tale", "Margaret Atwood"))
    books.append(Book("The Trial", "Franz Kalka"))
    books.append(Book("To Kill a Mockingbird", "Harper Lee"))

    return render_template('books.html',books=books)
 
if __name__ == '__main__':
    app.run(debug=True)