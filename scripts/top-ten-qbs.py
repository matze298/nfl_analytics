'''
Script tests functionality of nfldb
Displays Top-10 players by Passing-Yds
'''

from __future__ import print_function
import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_type='Regular')

for pp in q.sort('passing_yds').limit(10).as_aggregate():
    print(pp.player, pp.passing_yds, pp.passing_tds)
