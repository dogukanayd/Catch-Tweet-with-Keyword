#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import os.path


def main():
    keywords = ["dump", "pump"] # keywords you want to search for
    tweet = []
    date = []
    name = []
    path = 'outputs/csv/btc.csv'
    with open(path) as csvfile: # path you want to search for
        reader = csv.DictReader(csvfile)
        for row in reader:
            tweet.append(row["tweets"])
            date.append(row["date"])
            name.append(row["name"])
            
    for sentence in tweet:
        for word in sentence.split():
            for keyword in keywords:
                    if word == keyword:
                        file_exists = os.path.isfile('keyword_analysis.csv')
                        with open('keyword_analysis.csv', 'ab') as csvfile:
                            fieldnames = ["date", "name","tweets", "keyword"]
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            if not file_exists:
                                writer.writeheader()
                            writer.writerow({'date': 'date', 'name':'name' ,'tweets': sentence, 'keyword': keyword})

main()