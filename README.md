# ReTweet.py

A simple bot to retweet everything from a user Twitter account

## Installation
- First you will need to create a Twitter developer account
  - https://developer.twitter.com
- Next you will need to create a Twitter App
  - https://botwiki.org/resource/tutorial/how-to-create-a-twitter-app/
- Save the API Key/Secrete and Access Token/Secret to use in the script
- Clone the repo
- Set up `pipenv`
- Install dependencies
- Copy `creds_demo.json`
- Update `creds.json` with key/secret and token/secret
```
$ git clone git@github.com:techb/ReTweet.py.git
$ cd ReTweet.py/
$ pipenv shell
$ pipenv install
$ cp creds_demo.json creds.json
$ vim creds.json
$ ... update key/secret and twitter account id you wish to retweet
$ python retweet.py
```

## Usage

- To select which Twitter account you want to watch for tweets to retweet
  - Update `who_to_retweet` with the users Twitter Account Id
  - http://gettwitterid.com/
- ctlr+c to exit.
  - **Note** that it might take a second before exiting, really, give it a sec before spamming interrupts

#### Side Notes
- The current Twitter Account Id is for my dev/testing twitter account
  - @DevKB3