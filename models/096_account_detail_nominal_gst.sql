CREATE TABLE if NOT EXISTS account_detail_nominal_gst (
    id INTEGER PRIMARY KEY,
    describe TEXT,
    hsn TEXT,
    is_capital_goods BOOLEAN DEFAULT 0 CHECK (is_capital_goods IN (0, 1)),
    is_rcm_applicable BOOLEAN DEFAULT 0 CHECK (is_rcm_applicable IN (0, 1)),
    igst_rate INTEGER DEFAULT 0,
    cess INTEGER DEFAULT 0,
    cess_type TEXT DEFAULT "" CHECK (cess_type IN ('', 'bassed_on_value', 'bassed_on_qty', 'bassed_on_value_and_qty')),
    bassed_on_value INTEGER,
    bassed_on_qty_id INTEGER, -- TODO: ref to qty_table

    FOREIGN KEY(bassed_on_qty_id) REFERENCES unit_rate(id)

);


