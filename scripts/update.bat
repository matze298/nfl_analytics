psql -U nfldb -f D:\ws\py\08_nfl_data\scripts\Insert_JAX.sql
call activate nfl
python D:\ws\py\08_nfl_data\scripts\NewDB.py
psql -U nfldb -f D:\ws\py\08_nfl_data\scripts\Delete_JAX.sql
pause