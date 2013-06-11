#!usr/bin/env python
import json
import collections
import pprint

data = json.load(open("sample_data.json"))

actor_index = collections.defaultdict(list)

for film, actors in data.iteritems():
    for actor in actors:
        actor_index[actor].append(film)
