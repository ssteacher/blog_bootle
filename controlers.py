# -*- coding: utf-8 -*-
"""
This is controler for web application
"""

#import sys
import bottle
from models import Message
from models import User
import cgi
import re

@bottle.get("/login")
def include_header():
    
    return bottle.template("login.html", dict(username="", passwd=""))
    
@bottle.post("/newpost")
def press_login():
               
    username = bottle.request.forms.get("username")
    passwd = bottle.request.forms.get("password")
    print dict(username=username, subject="", body="", tags="")
    user = User()
    if user.is_user(username, passwd):
        return bottle.template("addpost.html", dict(username=username, subject="",
                                                body = "", tags=""))

@bottle.post("/tohome")
def go_home_page():
    username = bottle.request.forms.get("username")
    title = bottle.request.forms.get("title")
    
    tags = bottle.request.forms.get("tags")    
    tags = cgi.escape(tags)
    tags_array = extract_tags(tags)

    new_post = Message()
    new_post.add_new_message(message=title, user=username, tags=tags_array)
    return bottle.redirect("/")


@bottle.route("/")
def run_index_page():
    """
    Return index page on bottle freamework
    """
    some_post = Message()
    new_dict = some_post.get_message_by_key()
    
    return bottle.template("index.html", {"message_list": new_dict})


@bottle.route("/post")    
@bottle.route("/post/<tag>")
def view_post(tag=[]):
    some_post = Message()
    new_dict = some_post.get_message_by_key(tags=tag)
    return bottle.template("posts.html", {"message_list":new_dict})
    
    
@bottle.route("/userlist")
def view_users():
    """
    """
    user = User()
    return bottle.template("users.html", {"description": user.get_description(),
                                          "users":user.get_list_all_users()})



def extract_tags(tags):

    whitespace = re.compile('\s')

    nowhite = whitespace.sub("",tags)
    tags_array = nowhite.split(',')

    # let's clean it up
    cleaned = []
    for tag in tags_array:
        if tag not in cleaned and tag != "":
            cleaned.append(tag)

    return cleaned
#sessions = sessionDAO.SessionDAO(database)
bottle.debug(True)
bottle.run(host="localhost", port="8081")