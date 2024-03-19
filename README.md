# COMP3005-Project-V1

COMP 3005 Project V1

Youtube link: https://youtu.be/HAVE_TO_FILL_OUT

To run this Python console application, you need to do the following:

1. Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

2. Ensure that you have a PostgreSQL database running on your local machine. And that you have a database called `postgres` with a user `postgres` and password `admin`. If you have a different setup, you can change the values in the `database.ini` file.

<!-- 3. Ensure the database has the students table created. You can do this by running the following command (replace database name and user with your own if necessary) assuming you have the `psql` command line tool installed and in your path:

```bash
psql -U postgres -d postgres -a -f Assignment3-1.sql
``` -->

3. Run the application by running the following command:

```bash
python3 -u postgresDB-connector-python.py
```
