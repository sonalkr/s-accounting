CREATE TABLE if NOT EXISTS link_inventory__account__voucher (
    id INTEGER PRIMARY KEY,
    inventory_id INTEGER,
    account_id INTEGER NOT NULL,
    transaction_entry_id INTEGER NOT NULL,
    voucher_id INTEGER NOT NULL,

    FOREIGN KEY(account_id) REFERENCES account(id),
    FOREIGN KEY(inventory_id) REFERENCES inventory(id),
    FOREIGN KEY(transaction_entry_id) REFERENCES transaction_entry(id),
    FOREIGN KEY(voucher_id) REFERENCES voucher(id)

     
);


