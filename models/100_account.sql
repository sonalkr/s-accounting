CREATE TABLE if NOT EXISTS account (
    id INTEGER PRIMARY KEY,
    account_name TEXT NOT NULL UNIQUE,
    alias TEXT,
    opening_amount DECIMAL(20, 6) NOT NULL,
    note TEXT,
    
    account_under_id INTEGER NOT NULL,
    account_general_option_id INTEGER NOT NULL UNIQUE,
    account_detail_nominal_id INTEGER NOT NULL UNIQUE,
    account_detail_personal_tax_id INTEGER NOT NULL UNIQUE,
    

    FOREIGN KEY(account_under_id) REFERENCES account_under(id),
    FOREIGN KEY(account_general_option_id) REFERENCES account_general_option(id),
    FOREIGN KEY(account_detail_nominal_id) REFERENCES account_detail_nominal(id),
    FOREIGN KEY(account_detail_personal_tax_id) REFERENCES account_detail_personal_tax(id)
);


