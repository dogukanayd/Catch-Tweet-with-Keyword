#!/usr/bin/python
# -*- coding: utf-8 -*-
import oauth2
import json
import time
import sys
import csv
import os.path
from termcolor import colored
import datetime
from time import gmtime, strftime

reload(sys)
sys.setdefaultencoding('utf8')


def main(KEY_WORD, day):
    CONSUMER_KEY = 'xxx'
    CONSUMER_SECRET = 'xxx'
    KEY = 'xxx'
    SECRET = 'xxx'
    date = datetime.datetime.now()
    for i in range(day):
        url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + KEY_WORD + '&lang=tr&count=100&until=' + str(date.strftime("%Y-%m-%d")) 
        respond = oauth_req(url, KEY, SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        respond_json = json.loads(respond)
        try:
            while respond_json["search_metadata"]["next_results"]:
                url = 'https://api.twitter.com/1.1/search/tweets.json' + respond_json["search_metadata"]["next_results"]
                print colored("SUCCESS! ", "green") + colored("for selected date: ", "yellow") + colored("{0}".format(date), "green")
                respond = oauth_req(url, KEY, SECRET, CONSUMER_KEY, CONSUMER_SECRET)
                respond_json = json.loads(respond)
                filename = 'outputs/json/' + str(date) + '-' + KEY_WORD + '_' + str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))  + '.json'
                write_to_json(respond_json, filename)
                write_to_csv(respond_json, KEY_WORD)
        except KeyError:
            print colored("WARN!", "red") + \
            colored("There is nothing any data for selected date or completed for selected day", "yellow") + \
            colored(":{}".format(date), "green")
        date -= datetime.timedelta(days=1)


def oauth_req(url, key, secret, CONSUMER_KEY, CONSUMER_SECRET, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


def write_to_csv(data, KEY_WORD):
    file_exists = os.path.isfile('data.csv')
    filename = 'outputs/csv/' + KEY_WORD + '.csv'
    with open(filename, 'ab') as csvfile:
        fieldnames = ['keyword', 'date', 'name' ,'tweets', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for i in range(len(data["statuses"])):
            writer.writerow({'keyword': KEY_WORD ,
                             'date': data["statuses"][i]["created_at"] ,
                             'name': data["statuses"][i]["user"]["screen_name"],
                             'tweets': data["statuses"][i]["text"], 
                             'url': 'test'})


def write_to_json(data, filename):
    with open(filename, 'w') as fp:
        json.dump(data, fp, ensure_ascii=False)


def test_api(respond_json):
    for key in respond_json["statuses"]:
        print key["user"]["screen_name"]
        print key["entities"]["urls"]["expanded_url"]

main('btc', 7)
