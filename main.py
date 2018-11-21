'''
Playground for latest plots & functions
author: Matthias Rath
'''

# Imports
from __future__ import print_function
import nfldb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
from matplotlib import rcParams
from utils.nfl_colors import nfl_colors, nfl_colors_2
rcParams.update({'figure.autolayout': True})

# DB-connection
db = nfldb.connect()
q = nfldb.Query(db)

# # Query
# # All passes of Aaron Rodgers in 2018 resulting in a TD
# q.game(season_year='2018',season_type='Regular')
# q.player(full_name='Aaron Rodgers')
# q.play_player(passing_yds__ge=20, passing_tds=1)
#
# # Process data
# for pp in q.as_plays():
#     print(pp)

# Get all RB's rushing for more than min_yds & min_att
min_yds=100
min_att=20
q = nfldb.Query(db)
q.game(season_year='2018', season_type='Regular')
q.player(position='RB')
q.aggregate(rushing_yds__ge=min_yds, rushing_att__ge=min_att)

poi = []
print('Player (Team),     Attempts, Yds, Yds/Att')
for pp in q.sort('rushing_yds').as_aggregate():
    poi.append(pp)
    yds_att = float(pp.rushing_yds)/pp.rushing_att
    print(pp.player, pp.rushing_att, pp.rushing_yds, '%.1f' % yds_att)






