CREATE TABLE if NOT EXISTS transaction_entry (
    id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    
    ref_account_id INTEGER NOT NULL,
    
    amount_dr DECIMAL(20, 6) NOT NULL DEFAULT 0,
    amount_cr DECIMAL(20, 6) NOT NULL DEFAULT 0,
    narration TEXT,

    voucher_id INTEGER NOT NULL,
    voucher_number TEXT NOT NULL,
    
    FOREIGN KEY(ref_account_id) REFERENCES account(id),
    
    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(voucher_id) REFERENCES voucher(id)

);
