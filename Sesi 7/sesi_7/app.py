from flask import Flask, render_template, request
from author_book import author_book

app = Flask(__name__, template_folder='template')

""" @app.route('/')
def index():    
        return 'Index Page'
@app.route('/movie')
@app.route('/hello')
def hello_world():
    sum = a = 10
    return 'Hello, World! ' + str(sum)

@app.route('/author')
def author():
    return "<h2>Author Bio</h2> <a href='/'> Home Page </a>"

@app.route('/<name>')
def hello(name):
    #return "Hello, {name}"
    return f"Hello, {escape(name)}!"

@app.route('/books')
def books(author_id):
    #html = f"list of books authored by {author_id}:"
    #html += '<ul> <li> intro to lyfe </li> <li>intro to lyfe 2</li> <li>intro to lyfe 3</li>
    #return html
    return render_template('book.html', template_var_author=author_books[author_id])

@app.route('/user/<username>')
def show_user_profile(username):
    #show user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/halo/')
@app.route('/halo/<name>')
def halo():
    return render_template('hello.html')
 """

@app.route('/home')
@app.route('/')
def home():
    # return 'Hello, World!'
    return render_template('index.html')


#4
# @app.route('/author')
@app.route('/author', methods=['GET', 'POST'])
def author():

    if 'author_id' in request.form:
        author_book[request.form['author_id']] = [] #empty list

    # return 'Author Bio'
    # # return '<h2> Author Bio </h2> <a href="/"> Home page </a>'
    return render_template('author.html', author_book = author_book)


# @app.route('/books/<author_id>')
@app.route('/books/<int:author_id>')
def books(author_id):
    # html = f'List of Books authored by {author_id}:'
    # html += '<ul> <li>intro to lyfe</li> <li>intro to lyfe 2</li> <li>intro to lye3</li></ul>'
    # return html
    # return render_template('book.html', template_var_author=author_id)
    # if author_id != 400:
    if len(author_book[author_id]) == 0:
        return render_template('book.html', author_id=author_id)
    else:
        return render_template('book.html', author_id=author_id, book_list=author_book[author_id])
    
    # return render_template('book.html', author_id=author_id, book_list=author_book[author_id])
    # return render_template('book.html', author_id=author_id)

if __name__ == '__main__':
    app.run(debug=True)