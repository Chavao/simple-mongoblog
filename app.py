from bottle import route, run, template
from pymongo import MongoClient

connection = MongoClient('precise64', 27017)
db = connection.tests


@route('/')
def post_index():
    posts = [post for post in db.posts.find()]
    return template('view/index', posts=posts, title='simple-mongoblog')


@route('/post/:slug')
def post_single(slug):
    post = db.posts.find_one({'slug': slug})
    return template('view/single', post)

run(server='gunicorn', host='0.0.0.0', port=8864)
