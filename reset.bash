psql -d postgres -a -f /Users/karanpatel/Library/CloudStorage/OneDrive-CarletonUniversity/Winter2024/Comp3005/COMP3005-Project-V1/db_reset.sql
psql -d postgres -a -f /Users/karanpatel/Library/CloudStorage/OneDrive-CarletonUniversity/Winter2024/Comp3005/COMP3005-Project-V1/db_setup.sql
python3 db_competition_setup.py
python3 db_matches_setup.py