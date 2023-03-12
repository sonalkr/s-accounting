CREATE TABLE if NOT EXISTS account_general_option (
    id INTEGER PRIMARY KEY,
    bill_by_bill BOOLEAN DEFAULT 0 CHECK (bill_by_bill IN (0, 1)),
    credit_preiod INTEGER,
    cost_center BOOLEAN DEFAULT 0 CHECK (cost_center IN (0, 1))  
);


