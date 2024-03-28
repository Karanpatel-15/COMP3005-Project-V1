psql -d postgres -a -f db_reset.sql
psql -d postgres -a -f db_setup.sql
python3 db_competition_setup.py
python3 db_lineup_setup.py
python3 db_matches_setup.py
