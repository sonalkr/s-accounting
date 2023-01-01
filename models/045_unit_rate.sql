CREATE TABLE if NOT EXISTS unit_rate (
    id INTEGER PRIMARY KEY,
    unit_name TEXT NOT NULL UNIQUE,
    fraction_count INTEGER NOT NULL
);

