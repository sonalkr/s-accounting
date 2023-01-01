CREATE TABLE if NOT EXISTS link_tag__all_table (
    id INTEGER PRIMARY KEY,
    tag_id INTEGER NOT NULL,
    table_name TEXT NOT NULL,
    table_id INTEGER NOT NULL,

    FOREIGN KEY(tag_id) REFERENCES tag(id)

     
);


