import pymongo
from flask import request, redirect
from functools import wraps
import config

mongo_client = pymongo.MongoClient(config.MONGO_SERVER, 27017, connect=False)
mongo_db = mongo_client[config.MONGO_DB]


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('token', None)

        if not token:
            return redirect('/auth/login', 302)

        user_collection = mongo_db['auth_users']
        user = user_collection.find_one({'token': token})

        if user is None:
            return redirect('/auth/login', 302)

        return f(*args, **kwargs)

    return decorated_function
