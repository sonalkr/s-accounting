CREATE TABLE if NOT EXISTS account_detail_nominal (
    id INTEGER PRIMARY KEY,
    inventory_value_are_affected BOOLEAN NOT NULL CHECK (inventory_value_are_affected IN (0, 1)),
    type_of_ledger TEXT NOT NULL CHECK (type_of_ledger IN ('discount', 'invoice rounding', 'n/a')),
    fraction_value INTEGER DEFAULT 0,
    
    is_gst_applicable TEXT NOT NULL CHECK (is_gst_applicable IN ('yes', 'no', 'n/a')),
    account_detail_nominal_gst_id INTEGER NOT NULL,
    
    is_tds_applicable TEXT NOT NULL CHECK (is_tds_applicable IN ('yes', 'no', 'n/a')),
    account_detail_nominal_tds_tcs_id INTEGER NOT NULL,
    
    
    FOREIGN KEY(account_detail_nominal_tds_tcs_id) REFERENCES account_detail_nominal_tds_tcs(id),
    FOREIGN KEY(account_detail_nominal_gst_id) REFERENCES account_detail_nominal_gst(id)

);


