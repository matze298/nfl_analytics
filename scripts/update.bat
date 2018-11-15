psql -U nfldb -f %~dp0Insert_JAX.sql
psql -U nfldb -f %~dp0Insert_LAC.sql
call activate nfl
python %~dp0NewDB.py
psql -U nfldb -f %~dp0Delete_JAX.sql
psql -U nfldb -f %~dp0Delete_LAC.sql
pause