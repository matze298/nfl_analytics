UPDATE play SET pos_team = 'SD' WHERE pos_team = 'LAC';
UPDATE game SET home_team = 'SD' WHERE home_team = 'UNK';
UPDATE game SET away_team = 'SD' WHERE away_team = 'UNK';
DELETE FROM team WHERE team_id = 'LAC';