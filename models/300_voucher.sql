CREATE TABLE if NOT EXISTS voucher (
    id INTEGER PRIMARY KEY,
    voucher_number TEXT NOT NULL,
    data TEXT NOT NULL,
    narration TEXT,

    voucher_type_id INTEGER NOT NULL,
    FOREIGN KEY(voucher_type_id) REFERENCES voucher_type(id)

);
