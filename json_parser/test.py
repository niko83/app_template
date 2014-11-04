#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class DictDiffer(object):

    """
    Calculate the difference between two dictionaries.

    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """

    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.current_keys, self.past_keys = [set(d.keys()) for d in (current_dict, past_dict)]
        self.intersect = self.current_keys.intersection(self.past_keys)

    def added(self):
        return self.current_keys - self.intersect

    def removed(self):
        return self.past_keys - self.intersect

    def changed(self):
        return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])

    def unchanged(self):
        return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])

from json_parser import JSONRequest

f = open('request.json', 'r')
j = JSONRequest(f.read())

j.getPosInt(['emitter_id'])
j.getPosInt(('periphery_id', )),
j.getObj(['callback'], default={}),
# j.getObj(['time'], default={}),

# "time": {
# "results_periphery": 86400,
# "results_bigworld": 60,
# "creation_deadline": 600
# },

j.getStr(['settings', 'comment'])
j.getBool(['settings', 'destroyIfCreatorOut'])
j.getBool(['settings', 'notifyWeb'])
# settings["ver"] = 2,
j.getEnum(['settings', 'bonusType'], enum=[1, 2, 3, 4, 5, 6], default=4)
j.getEnum(['settings', 'chatChannels'], enum=[1, 2, 3, 4, 5, 6], default=2)
j.getPosInt(['settings', 'defaultRoster'], 17)
j.getList(['settings', 'accountsToInvite'], parser=int)
# settings["clanRoles"]: {},
# settings["clansToInvite"]: [],
# settings["winsLimit"]: 2,
# settings["type"]: 4,
# settings["winnerIfDraw"]: 0,
# settings["isOpened"]: false,
# settings["timeBetweenBattles"]: 180,
# settings["startType"]: 1,
# settings["startTime"]: 1404316800,
# settings["startIfReady"]: true,
# settings["roles"]: {},
# settings["battlesLimit": 5,
# settings["roundLength": 600,
# settings["lifeTime": 0,
# settings["switchBattleTeams": true,
# settings["arenaTypeID": 3
j.getObj(['settings', 'extraData'], default={})
# settings["opponents"] = j.getObj(key + ['opponents'], default={}),
# "extraData": {
# "localized_data": {
# "ru": {
# "event_name": "",
# "session_name": "",
# "desc": ""
# }
# },
# "opponents": {
# "1": { "name": "Good Luck & Have FuN" },
# "2": { "name": "33 Team" } }
# },

j.getPosInt(['settings', 'teamRoles', '1'], 36)
j.getPosInt(['settings', 'teamRoles', '2'], 72)

# key = ['settings', 'initialRosters']
# initialRosters = j.key(filtred_data, key, default=[])
# initialRosters[0] = j.getObj(key + [0], default={})
# initialRosters[1] = j.getObj(key + [1], default={})

for last_key in ['0', '1', '2']:
    key = ['settings', 'limits', last_key]
    j.getList(key + ['totalLevel'], parser=int, count=2, default=[])
    j.getList(key + ['level'], parser=int, count=2, default=[])
    j.getList(key + ['maxCount'], parser=int, count=2, default=[])


print j.filtred_data
j.filtred_data = json.loads(json.dumps(j.filtred_data))

d = DictDiffer(j.filtred_data, j.json)
print "Added:", d.added()
print "Removed:", d.removed()
print "Changed:", d.changed()
print "Unchanged:", d.unchanged()
d = DictDiffer(j.filtred_data['settings'], j.json['settings'])
print "Added:", d.added()
print "Removed:", d.removed()
print "Changed:", d.changed()
print "Unchanged:", d.unchanged()

print j.getWarnings()
