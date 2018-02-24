import praw
import NickysFirstBot_config
import time
import os


def bot_login():
    print("Logging in...")
    lgn = praw.Reddit(username=NickysFirstBot_config.username,
                      password=NickysFirstBot_config.password,
                      client_id=NickysFirstBot_config.client_id,
                      client_secret=NickysFirstBot_config.client_secret,
                      user_agent="Nicky's first bot v0.1")
    print("logged in")

    return lgn


def run_bot(lgn, commentsReplied):
    print("checking 25 comments for \"Marco\"")
    for comment in lgn.subreddit('test').comments(limit=25):
    	if "Marco" in comment.body and comment.id not in commentsReplied and comment.author != lgn.user.me():
            print("Found a \"Marco\" in comment " + comment.id)
            comment.reply("Polo!")
            print("Replied to coment " + comment.id)

            commentsReplied.append(comment.id)
            with open("commentsReplied.txt", "a") as Replied:
                Replied.write(comment.id + "\n")


def getCommentsReplied():
    if not os.path.isfile("commentsReplied.txt"):
        commentsReplied = []
    else:
        with open("commentsReplied.txt", "r") as Replied:
            commentsReplied = Replied.read()
            commentsReplied = commentsReplied.split("\n")
    return commentsReplied


lgn = bot_login()
commentsReplied = getCommentsReplied()

while True:
    run_bot(lgn, commentsReplied)
    # sleeping for 15 sec
    print("sleeping 15 sec...")
    time.sleep(15)
