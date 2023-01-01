CREATE TABLE if NOT EXISTS account_general_option (
    id INTEGER PRIMARY KEY,
    bill_by_bill BOOLEAN NOT NULL CHECK (bill_by_bill IN (0, 1)),
    credit_preiod INTEGER,
    cost_center BOOLEAN NOT NULL CHECK (cost_center IN (0, 1))  
);


