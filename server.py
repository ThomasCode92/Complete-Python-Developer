from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/blog/<username>/<int:post_id>')
def blog_post(username=None, post_id=None):
    return render_template('blog.html', name=username, post_id=post_id)
