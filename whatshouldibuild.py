#!/usr/bin/env python

import sys
import json
from random import randint

with open('ideas.json') as data_file:
  data = json.load(data_file)

for index, item in enumerate(data):
  print index, item['category']

argument = raw_input('Please choose a topic: ')

available_topics = data[int(argument)]['topics']

topic_index = randint(0, len(available_topics) - 1)

print "\n"
print available_topics[topic_index]['title']
print available_topics[topic_index]['description']
