CREATE TABLE if NOT EXISTS account_detail_nominal_tds_tcs (
    id INTEGER PRIMARY KEY,
    describe TEXT,
    section TEXT NOT NULL,
    rate DECIMAL NOT NULL,
    tax_limit INTEGER NOT NULL,
    amount_limit INTEGER NOT NULL,
    tds_tcs TEXT NOT NULL CHECK (tds_tcs IN ('tds', 'tcs'))
);


