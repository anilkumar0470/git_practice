from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config["SECRET_KEY"]="4c11cce0d2e09bba976c87a6b78c4e8a"

posts = [
    {
        'author': "anil kumar",
        'title': "blog post1",
        'content': 'first post content',
        'date_posted': 'April 20, 2022'
    },
    {
        'author': "anil kumar pathapati",
        'title': "blog post2",
        'content': 'second post content',
        'date_posted': 'April 21, 2022'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('regsiter.html', title='register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('regsiter.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)