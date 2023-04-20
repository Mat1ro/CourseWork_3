from flask import Flask, render_template, request, redirect, jsonify
from utils import *
import logging

app = Flask(__name__, template_folder='templates')
logging.basicConfig(level=logging.INFO, filename='logs/api.log', format='%(asctime)s [%(levelname)s] %(message)s')
app.config["JSON_AS_ASCII"] = False


@app.route('/')
def main_page():
    posts = get_posts_all()
    bookmarks = get_bookmarks_all()
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@app.route('/posts/<int:postid>')
def post_page(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search')
def search_page():
    query = request.args.get('query')
    posts = search_for_posts(query)
    return render_template('search.html', posts=posts)


@app.route('/users/<username>')
def user_page(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


@app.route('/bookmarks/add/<int:postid>', methods=["GET", "PUT"])
def add_bookmark_page(postid):
    post = get_post_by_pk(postid)
    add_to_bookmarks(post)
    return redirect('/', code=302)


@app.route('/bookmarks/remove/<int:postid>', methods=["GET", "DELETE"])
def delete_bookmark_page(postid):
    remove_bookmark(postid)
    return redirect('/', code=302)


@app.route('/bookmarks')
def bookmarks_page():
    posts = get_bookmarks_all()
    return render_template('bookmarks.html', posts=posts)


@app.route('/tag/<word>')
def tag_page(word):
    posts = get_tag(word)
    return render_template('tag.html', posts=posts, word=word.upper())


@app.route('/api/posts')
def api_posts_page():
    logging.info('Зашел на api по всем пользователям')
    posts = get_posts_all()
    return jsonify(posts)


@app.route('/api/posts/<int:postid>')
def api_post_page(postid):
    logging.info(f'Зашел на api по {postid} пользователю')
    post = get_post_by_pk(postid)
    return jsonify(post)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Странички не существует</h1>", 404


@app.errorhandler(500)
def page_not_fond(e):
    return "<h1>Internal Server Error</h1>", 500


if __name__ == "__main__":
    app.run()
