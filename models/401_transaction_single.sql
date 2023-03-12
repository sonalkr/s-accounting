CREATE TABLE if NOT EXISTS transaction_single (
    id INTEGER PRIMARY KEY,
    transaction_entry_id INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    
    amount_dr DECIMAL(20, 6) DEFAULT 0,
    amount_cr DECIMAL(20, 6) DEFAULT 0,

    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(transaction_entry_id) REFERENCES transaction_entry(id)
);
