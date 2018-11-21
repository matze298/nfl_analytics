'''
Plot all teams scoring over 50 points & their respective point differential
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

# Get all games with a team scoring more than 50 points
q.game(season_type='Regular').sort(('start_time', 'asc'))
big_score = nfldb.QueryOR(db).game(home_score__ge=50, away_score__ge=50)
q.andalso(big_score)

teams = []
score_diff = []
points = []
scores = []
for g in q.as_games():
    if g.home_score >= 50:
        teams.append(g.home_team)
        score_diff.append(g.home_score-g.away_score)
        scores.append(g.home_score)
    if g.away_score >= 50:
        teams.append(g.away_team)
        score_diff.append(g.away_score-g.home_score)
        scores.append(g.away_score)
    print(g)

score_diff = np.array(score_diff)
scores = np.array(scores)
colors = [nfl_colors[s] for s in teams]
colors_2 = [nfl_colors_2[s] for s in teams]

# Plot scores & differential
plt.style.use('ggplot')
fig, ax = plt.subplots()

for i, score in enumerate(scores):
    plt.scatter(score, score_diff[i], facecolors=colors[i], edgecolors=colors_2[i], label=teams[i], alpha=0.8)
    #plt.annotate(teams[i], (score+0.25, score_diff[i]-0.05))

# Create legend
unique_teams = np.unique(np.array(sorted(teams)))
unique_colors = [nfl_colors[s] for s in unique_teams]
unique_colors_2 = [nfl_colors_2[s] for s in unique_teams]
legend_elements = [Circle([0], [0], facecolor=c, edgecolor=unique_colors_2[i],label=unique_teams[i]) for i, c in enumerate(unique_colors)]


plt.legend(bbox_to_anchor=(1.1, 0.5), handles=legend_elements, ncol=2)
plt.title('Teams scoring over 50 points since 2009')
plt.xlabel('Points')
plt.ylabel('Point Differential')
plt.grid(True)
plt.xlim([49, 63])
plt.ylim([-5, 60])
ellipse = Ellipse((52.5, 0), 9, 1.75, angle=67.5, facecolor='none', edgecolor='black')
ax.add_patch(ellipse)
plt.savefig('../img/point_differential_over50.png')