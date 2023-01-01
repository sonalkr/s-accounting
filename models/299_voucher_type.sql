CREATE TABLE if NOT EXISTS voucher_type (
    id INTEGER PRIMARY KEY,
    voucher_number_start_from INTEGER NOT NULL,
    voucher_number_prefix TEXT,
    voucher_number_sufix TEXT,
    primary_voucher_type TEXT NOT NULL,
    prevent_duplicate BOOLEAN NOT NULL CHECK (prevent_duplicate IN (0, 1))
    

);
