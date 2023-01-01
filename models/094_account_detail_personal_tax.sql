
CREATE TABLE if NOT EXISTS account_detail_personal_tax (
    id INTEGER PRIMARY KEY,
    pan TEXT,
    it_group TEXT NOT NULL CHECK (it_group IN ('huf', 'individual', 'company')),
    gst_no TEXT,
    gst_group TEXT NOT NULL CHECK (gst_group IN ('regular', 'unregister', 'consumer'))
);

