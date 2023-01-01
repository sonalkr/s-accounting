
CREATE TABLE if NOT EXISTS inventory (
    id INTEGER PRIMARY KEY,
    account_name TEXT NOT NULL,
    alias TEXT,
    part_no TEXT,
    note TEXT,
    inventory_under_id INTEGER NOT NULL,
    
    unit_rate_id INTEGER NOT NULL,

    is_gst_applicable TEXT NOT NULL CHECK (is_gst_applicable IN ('yes', 'no', 'n/a')),
    account_detail_nominal_gst_id INTEGER NOT NULL,

    opening_amount DECIMAL(20, 6) NOT NULL,
    opening_qty DECIMAL(20, 6) NOT NULL,
    opening_unit_rate_id INTEGER NOT NULL,
    
    
    
    FOREIGN KEY(unit_rate_id) REFERENCES unit_rate(id),
    FOREIGN KEY(opening_unit_rate_id) REFERENCES unit_rate(id),
    FOREIGN KEY(inventory_under_id) REFERENCES inventory_under(id)

);

