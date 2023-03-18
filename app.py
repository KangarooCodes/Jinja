from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story



app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

app.static_folder = 'static'
debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    madlib = story.madlib

    return render_template("base.html", madlib=madlib)


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)