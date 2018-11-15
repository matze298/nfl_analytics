from __future__ import print_function 
import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year=2018,season_type='Regular')

for g in q.game(season_year=2018,season_type='Regular').as_games():
    print(g.gsis_id)
    print(g.home_team)
    print(g.away_team)
    print()
    
    
import nflgame.live
import nflgame.update_sched
year, week = nflgame.live.current_year_and_week()
phase = nflgame.live._cur_season_phase
print(year,week)
    
#for pp in q.sort('passing_yds').limit(10).as_aggregate():
#    print(pp.player,pp.passing_yds)