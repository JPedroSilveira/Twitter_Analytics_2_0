from Twitter.TwitterCore import TwitterCore
from Database.TableManeger import TableManeger
from Data.Tweet import Tweet
from Data.User import User
# import nltk


def main():
    # nltk.download('punkt')

    #twitter = TwitterCore()

    #twitter.stream('Trump', 'en')

    maneger = TableManeger(Tweet)

    maneger.find_by_id(0)

    #maneger.delete_by_id(1)


main()
