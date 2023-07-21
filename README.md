# Shelfwatch Project

## Installation

In order to collaborate, you will need to perform the following steps:

- Clone this repository

```git
git clone <repository URL>
```

- Install and activate a virtual enviroment inside the repository directory  
(If you don't have Python 3.11 version installed, run this command with python 3.10 instead.)

```git
python3.11 -m venv .venv --prompt Shelfwatch && source .venv/bin/activate
```

- Install all requirements by running this code:

```git
pip install -r requirements.txt
```

- Create a database in your PostgreSQL shell using:

```postgresql
CREATE DATABASE shelfwatch;
```

- Create tables and insert data running the following commands:

```text
\i absolute path to create.sql file

\i absolute path to init_data.sql file
```

- Create a branch using:

```git
git switch -c <branchname>
```

- Get to work!