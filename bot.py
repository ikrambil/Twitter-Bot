import tweepy
import tkinter
from tkinter import *

#Credentials
consumer_key = 'consumer key'
consumer_secret = 'consumer secrets'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Authentication Check
user = api.me()
print(user.name)
print(user.location)


#Loop through and follow everyone you are following
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print("Followed everyone that is following " + user.name)



#Creating the Gui
root = Tk()

label1 = Label(root, text="Search")
Search = Entry(root, bd=5)

label2 = Label(root, text="Number of Tweets")
numTweets = Entry(root, bd=5)

label3 = Label(root, text="Response")
Response = Entry(root, bd=5)

label4 = Label(root, text="Reply?")
Reply = Entry(root, bd=5)

label5 = Label(root, text="Retweet?")
Retweet = Entry(root, bd=5)

label6 = Label(root, text="Favorite?")
Fav = Entry(root, bd=5)

label7 = Label(root, text="Follow?")
Follow = Entry(root, bd=5)


#Helper functions to store and use user input
def getSearch():
    return Search.get()


def getnumTweets():
    return numTweets.get()


def getResponse():
    return Response.get()


def getReply():
    return Reply.get()


def getRetweet():
    return Retweet.get()


def getFav():
    return Fav.get()


def getFollow():
    return Follow.get()


#Main function to connect everything
def mainFunction():
    #Get all the responses from the user =
    getSearch()
    search = getSearch()

    getnumTweets()
    numberOfTweets = getnumTweets()
    numberOfTweets = int(numberOfTweets)

    getResponse()
    phrase = getResponse()

    getReply()
    reply = getReply()

    getRetweet()
    retweet = getRetweet()

    getFav()
    favorite = getFav()

    getFollow()
    follow = getFollow()


    #Loop through and reply with phrase
    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                # Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
                print("Replied with " + phrase)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    #Loop through and retweet
    if retweet == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                # Retweet
                tweet.retweet()
                print('Retweeted the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    # Loop through and favorite
    if favorite == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                # Favorite
                tweet.favorite()
                print('Favorited the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    # Loop through and follow
    if follow == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                # Follow
                tweet.user.follow()
                print('Followed the user')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break


submit = Button(root, text="Submit", command=mainFunction)

#Packing each label
label1.pack()
Search.pack()

label2.pack()
numTweets.pack()

label3.pack()
Response.pack()
label4.pack()

Reply.pack()
label5.pack()

Retweet.pack()
label6.pack()

Fav.pack()
label7.pack()

Follow.pack()
submit.pack(side=BOTTOM)

root.mainloop()
