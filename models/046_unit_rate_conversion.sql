CREATE TABLE if NOT EXISTS unit_rate_conversion (
    id INTEGER PRIMARY KEY,
    unit_from_id INTEGER NOT NULL,
    unit_to_id INTEGER NOT NULL,
    rate_of_conversion INTEGER NOT NULL,
    FOREIGN KEY(unit_from_id) REFERENCES unit_rate(id),
    FOREIGN KEY(unit_to_id) REFERENCES unit_rate(id)
);


