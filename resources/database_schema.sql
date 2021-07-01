CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    birthday TEXT,
    sex TEXT,
    mass REAL
);

CREATE TABLE beverage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    beverage_name TEXT,
    alcohol_proportion REAL,
    beverage_type TEXT
);

CREATE TABLE drink (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_people INTEGER REFERENCES people (id),
        id_beverage INTEGER REFERENCES beverage (id),
        drink_date TEXT,
        place TEXT,
        volume REAL
);