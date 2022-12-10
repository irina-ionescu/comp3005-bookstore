# comp3005-bookstore
This is a sample bookstore application.

## Student name: 
  - Irina Ionescu
## Student number: 
  - 101 131 375

## Prerequisites
- Bash environment, Linux/Mac
- Postgres 14.x installed on localhost(127.0.0.1)
- Python 3.8
- psycopg2 installed (psycopg.org/docs/install.html)
- PrettyTable: pip install PTable

## Setup
- Environment variables for PGUSER, PGPORT (run pg_env.sh from the Postgres installation directory)
- Add an environment variable for the postgres user PGPASS in ~/.bash_rc or ~/.bash_profile and load in bash with source
- Create a database named Bookstore
- Execute the create.sql (this will also create the trigger in trigger.sql)

## Folder structure:


## Run customer app:
- from command line: python3 customer_app.py
- choose options from the menus by entering corresponding numbers
- to enter data, type directly in command line as required (follow prompts)

## Run owner app:
- from command line: python3 owner_app.py
- choose options from the menus by entering corresponding numbers
- to enter data, type directly in command line as required (follow prompts)
