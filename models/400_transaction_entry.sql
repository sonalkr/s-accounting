CREATE TABLE if NOT EXISTS transaction_entry (
    id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    
    narration TEXT,

    voucher_id INTEGER NOT NULL,
    voucher_number TEXT NOT NULL,
    
    FOREIGN KEY(voucher_id) REFERENCES voucher(id)

);
