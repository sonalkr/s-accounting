from fastapi import APIRouter, Depends, HTTPException, Form
from pydantic import BaseModel
from sqlalchemy.orm import Session
from server_fastapi.auto_gen.utilities import as_form

from server_fastapi.auto_gen.database import get_db

default_api = APIRouter()


@as_form
class Account(BaseModel):
    id: int | None = None
    account_name: str
    alias: str | None = None
    opening_amount: float
    note: str | None = None
    account_under_id: int
    account_general_option_id: int
    account_detail_nominal_id: int
    account_detail_personal_tax_id: int

@default_api.post("/account/create/")
async def create_account(account: Account = Depends(Account.as_form), db: Session = Depends(get_db)):
    data = account.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO account({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/account/get/")
async def get_account(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM account;").all()
    return rs

@default_api.delete("/account/delete/")
async def delete_account(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM account WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM account WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/account/update/")
async def update_account(account: Account = Depends(Account.as_form), db: Session = Depends(get_db)):
    data = account.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE account SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Link_tag__all_table(BaseModel):
    id: int | None = None
    tag_id: int
    table_name: str
    table_id: int

@default_api.post("/link_tag__all_table/create/")
async def create_link_tag__all_table(link_tag__all_table: Link_tag__all_table = Depends(Link_tag__all_table.as_form), db: Session = Depends(get_db)):
    data = link_tag__all_table.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO link_tag__all_table({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/link_tag__all_table/get/")
async def get_link_tag__all_table(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM link_tag__all_table;").all()
    return rs

@default_api.delete("/link_tag__all_table/delete/")
async def delete_link_tag__all_table(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM link_tag__all_table WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM link_tag__all_table WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/link_tag__all_table/update/")
async def update_link_tag__all_table(link_tag__all_table: Link_tag__all_table = Depends(Link_tag__all_table.as_form), db: Session = Depends(get_db)):
    data = link_tag__all_table.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE link_tag__all_table SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Link_inventory__account__voucher(BaseModel):
    id: int | None = None
    inventory_id: int | None = None
    account_id: int
    transaction_entry_id: int
    voucher_id: int

@default_api.post("/link_inventory__account__voucher/create/")
async def create_link_inventory__account__voucher(link_inventory__account__voucher: Link_inventory__account__voucher = Depends(Link_inventory__account__voucher.as_form), db: Session = Depends(get_db)):
    data = link_inventory__account__voucher.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO link_inventory__account__voucher({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/link_inventory__account__voucher/get/")
async def get_link_inventory__account__voucher(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM link_inventory__account__voucher;").all()
    return rs

@default_api.delete("/link_inventory__account__voucher/delete/")
async def delete_link_inventory__account__voucher(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM link_inventory__account__voucher WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM link_inventory__account__voucher WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/link_inventory__account__voucher/update/")
async def update_link_inventory__account__voucher(link_inventory__account__voucher: Link_inventory__account__voucher = Depends(Link_inventory__account__voucher.as_form), db: Session = Depends(get_db)):
    data = link_inventory__account__voucher.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE link_inventory__account__voucher SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Account_detail_nominal_gst(BaseModel):
    id: int | None = None
    describe: str | None = None
    hsn: str | None = None
    is_capital_goods: bool | None = None
    is_rcm_applicable: bool | None = None
    igst_rate: int | None = None
    cess: int | None = None
    cess_type: str | None = None
    bassed_on_value: int | None = None
    bassed_on_qty_id: int | None = None

@default_api.post("/account_detail_nominal_gst/create/")
async def create_account_detail_nominal_gst(account_detail_nominal_gst: Account_detail_nominal_gst = Depends(Account_detail_nominal_gst.as_form), db: Session = Depends(get_db)):
    data = account_detail_nominal_gst.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO account_detail_nominal_gst({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/account_detail_nominal_gst/get/")
async def get_account_detail_nominal_gst(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM account_detail_nominal_gst;").all()
    return rs

@default_api.delete("/account_detail_nominal_gst/delete/")
async def delete_account_detail_nominal_gst(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM account_detail_nominal_gst WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM account_detail_nominal_gst WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/account_detail_nominal_gst/update/")
async def update_account_detail_nominal_gst(account_detail_nominal_gst: Account_detail_nominal_gst = Depends(Account_detail_nominal_gst.as_form), db: Session = Depends(get_db)):
    data = account_detail_nominal_gst.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE account_detail_nominal_gst SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Inventory(BaseModel):
    id: int | None = None
    account_name: str
    alias: str | None = None
    part_no: str | None = None
    note: str | None = None
    inventory_under_id: int
    unit_rate_id: int
    is_gst_applicable: str
    account_detail_nominal_gst_id: int
    opening_amount: float
    opening_qty: float
    opening_unit_rate_id: int

@default_api.post("/inventory/create/")
async def create_inventory(inventory: Inventory = Depends(Inventory.as_form), db: Session = Depends(get_db)):
    data = inventory.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO inventory({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/inventory/get/")
async def get_inventory(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM inventory;").all()
    return rs

@default_api.delete("/inventory/delete/")
async def delete_inventory(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM inventory WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM inventory WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/inventory/update/")
async def update_inventory(inventory: Inventory = Depends(Inventory.as_form), db: Session = Depends(get_db)):
    data = inventory.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE inventory SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Voucher(BaseModel):
    id: int | None = None
    voucher_number: str
    data: str
    narration: str | None = None
    voucher_type_id: int

@default_api.post("/voucher/create/")
async def create_voucher(voucher: Voucher = Depends(Voucher.as_form), db: Session = Depends(get_db)):
    data = voucher.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO voucher({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/voucher/get/")
async def get_voucher(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM voucher;").all()
    return rs

@default_api.delete("/voucher/delete/")
async def delete_voucher(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM voucher WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM voucher WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/voucher/update/")
async def update_voucher(voucher: Voucher = Depends(Voucher.as_form), db: Session = Depends(get_db)):
    data = voucher.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE voucher SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Transaction_entry(BaseModel):
    id: int | None = None
    account_id: int
    ref_account_id: int
    amount_dr: float
    amount_cr: float
    narration: str | None = None
    voucher_id: int
    voucher_number: str

@default_api.post("/transaction_entry/create/")
async def create_transaction_entry(transaction_entry: Transaction_entry = Depends(Transaction_entry.as_form), db: Session = Depends(get_db)):
    data = transaction_entry.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO transaction_entry({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/transaction_entry/get/")
async def get_transaction_entry(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM transaction_entry;").all()
    return rs

@default_api.delete("/transaction_entry/delete/")
async def delete_transaction_entry(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM transaction_entry WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM transaction_entry WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/transaction_entry/update/")
async def update_transaction_entry(transaction_entry: Transaction_entry = Depends(Transaction_entry.as_form), db: Session = Depends(get_db)):
    data = transaction_entry.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE transaction_entry SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Inventory_under(BaseModel):
    id: int | None = None
    inventory_under_name: str

@default_api.post("/inventory_under/create/")
async def create_inventory_under(inventory_under: Inventory_under = Depends(Inventory_under.as_form), db: Session = Depends(get_db)):
    data = inventory_under.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO inventory_under({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/inventory_under/get/")
async def get_inventory_under(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM inventory_under;").all()
    return rs

@default_api.delete("/inventory_under/delete/")
async def delete_inventory_under(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM inventory_under WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM inventory_under WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/inventory_under/update/")
async def update_inventory_under(inventory_under: Inventory_under = Depends(Inventory_under.as_form), db: Session = Depends(get_db)):
    data = inventory_under.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE inventory_under SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Account_general_option(BaseModel):
    id: int | None = None
    bill_by_bill: bool
    credit_preiod: int | None = None
    cost_center: bool

@default_api.post("/account_general_option/create/")
async def create_account_general_option(account_general_option: Account_general_option = Depends(Account_general_option.as_form), db: Session = Depends(get_db)):
    data = account_general_option.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO account_general_option({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/account_general_option/get/")
async def get_account_general_option(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM account_general_option;").all()
    return rs

@default_api.delete("/account_general_option/delete/")
async def delete_account_general_option(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM account_general_option WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM account_general_option WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/account_general_option/update/")
async def update_account_general_option(account_general_option: Account_general_option = Depends(Account_general_option.as_form), db: Session = Depends(get_db)):
    data = account_general_option.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE account_general_option SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Account_detail_nominal_tds_tcs(BaseModel):
    id: int | None = None
    describe: str | None = None
    section: str
    rate: float
    tax_limit: int
    amount_limit: int
    tds_tcs: str

@default_api.post("/account_detail_nominal_tds_tcs/create/")
async def create_account_detail_nominal_tds_tcs(account_detail_nominal_tds_tcs: Account_detail_nominal_tds_tcs = Depends(Account_detail_nominal_tds_tcs.as_form), db: Session = Depends(get_db)):
    data = account_detail_nominal_tds_tcs.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO account_detail_nominal_tds_tcs({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/account_detail_nominal_tds_tcs/get/")
async def get_account_detail_nominal_tds_tcs(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM account_detail_nominal_tds_tcs;").all()
    return rs

@default_api.delete("/account_detail_nominal_tds_tcs/delete/")
async def delete_account_detail_nominal_tds_tcs(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM account_detail_nominal_tds_tcs WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM account_detail_nominal_tds_tcs WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/account_detail_nominal_tds_tcs/update/")
async def update_account_detail_nominal_tds_tcs(account_detail_nominal_tds_tcs: Account_detail_nominal_tds_tcs = Depends(Account_detail_nominal_tds_tcs.as_form), db: Session = Depends(get_db)):
    data = account_detail_nominal_tds_tcs.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE account_detail_nominal_tds_tcs SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Unit_rate_conversion(BaseModel):
    id: int | None = None
    unit_from_id: int
    unit_to_id: int
    rate_of_conversion: int

@default_api.post("/unit_rate_conversion/create/")
async def create_unit_rate_conversion(unit_rate_conversion: Unit_rate_conversion = Depends(Unit_rate_conversion.as_form), db: Session = Depends(get_db)):
    data = unit_rate_conversion.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO unit_rate_conversion({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/unit_rate_conversion/get/")
async def get_unit_rate_conversion(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM unit_rate_conversion;").all()
    return rs

@default_api.delete("/unit_rate_conversion/delete/")
async def delete_unit_rate_conversion(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM unit_rate_conversion WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM unit_rate_conversion WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/unit_rate_conversion/update/")
async def update_unit_rate_conversion(unit_rate_conversion: Unit_rate_conversion = Depends(Unit_rate_conversion.as_form), db: Session = Depends(get_db)):
    data = unit_rate_conversion.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE unit_rate_conversion SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Account_detail_nominal(BaseModel):
    id: int | None = None
    inventory_value_are_affected: bool
    type_of_ledger: str
    fraction_value: int | None = None
    is_gst_applicable: str
    account_detail_nominal_gst_id: int
    is_tds_applicable: str
    account_detail_nominal_tds_tcs_id: int

@default_api.post("/account_detail_nominal/create/")
async def create_account_detail_nominal(account_detail_nominal: Account_detail_nominal = Depends(Account_detail_nominal.as_form), db: Session = Depends(get_db)):
    data = account_detail_nominal.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO account_detail_nominal({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/account_detail_nominal/get/")
async def get_account_detail_nominal(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM account_detail_nominal;").all()
    return rs

@default_api.delete("/account_detail_nominal/delete/")
async def delete_account_detail_nominal(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM account_detail_nominal WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM account_detail_nominal WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/account_detail_nominal/update/")
async def update_account_detail_nominal(account_detail_nominal: Account_detail_nominal = Depends(Account_detail_nominal.as_form), db: Session = Depends(get_db)):
    data = account_detail_nominal.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE account_detail_nominal SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Voucher_type(BaseModel):
    id: int | None = None
    voucher_number_start_from: int
    voucher_number_prefix: str | None = None
    voucher_number_sufix: str | None = None
    primary_voucher_type: str
    prevent_duplicate: bool

@default_api.post("/voucher_type/create/")
async def create_voucher_type(voucher_type: Voucher_type = Depends(Voucher_type.as_form), db: Session = Depends(get_db)):
    data = voucher_type.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO voucher_type({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/voucher_type/get/")
async def get_voucher_type(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM voucher_type;").all()
    return rs

@default_api.delete("/voucher_type/delete/")
async def delete_voucher_type(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM voucher_type WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM voucher_type WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/voucher_type/update/")
async def update_voucher_type(voucher_type: Voucher_type = Depends(Voucher_type.as_form), db: Session = Depends(get_db)):
    data = voucher_type.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE voucher_type SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Account_detail_personal_tax(BaseModel):
    id: int | None = None
    pan: str | None = None
    it_group: str
    gst_no: str | None = None
    gst_group: str

@default_api.post("/account_detail_personal_tax/create/")
async def create_account_detail_personal_tax(account_detail_personal_tax: Account_detail_personal_tax = Depends(Account_detail_personal_tax.as_form), db: Session = Depends(get_db)):
    data = account_detail_personal_tax.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO account_detail_personal_tax({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/account_detail_personal_tax/get/")
async def get_account_detail_personal_tax(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM account_detail_personal_tax;").all()
    return rs

@default_api.delete("/account_detail_personal_tax/delete/")
async def delete_account_detail_personal_tax(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM account_detail_personal_tax WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM account_detail_personal_tax WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/account_detail_personal_tax/update/")
async def update_account_detail_personal_tax(account_detail_personal_tax: Account_detail_personal_tax = Depends(Account_detail_personal_tax.as_form), db: Session = Depends(get_db)):
    data = account_detail_personal_tax.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE account_detail_personal_tax SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Tag(BaseModel):
    id: int | None = None
    tag_name: str

@default_api.post("/tag/create/")
async def create_tag(tag: Tag = Depends(Tag.as_form), db: Session = Depends(get_db)):
    data = tag.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO tag({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/tag/get/")
async def get_tag(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM tag;").all()
    return rs

@default_api.delete("/tag/delete/")
async def delete_tag(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM tag WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM tag WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/tag/update/")
async def update_tag(tag: Tag = Depends(Tag.as_form), db: Session = Depends(get_db)):
    data = tag.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE tag SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Account_under(BaseModel):
    id: int | None = None
    account_under_name: str
    primary_group: str

@default_api.post("/account_under/create/")
async def create_account_under(account_under: Account_under = Depends(Account_under.as_form), db: Session = Depends(get_db)):
    data = account_under.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO account_under({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/account_under/get/")
async def get_account_under(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM account_under;").all()
    return rs

@default_api.delete("/account_under/delete/")
async def delete_account_under(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM account_under WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM account_under WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/account_under/update/")
async def update_account_under(account_under: Account_under = Depends(Account_under.as_form), db: Session = Depends(get_db)):
    data = account_under.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE account_under SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


@as_form
class Unit_rate(BaseModel):
    id: int | None = None
    unit_name: str
    fraction_count: int

@default_api.post("/unit_rate/create/")
async def create_unit_rate(unit_rate: Unit_rate = Depends(Unit_rate.as_form), db: Session = Depends(get_db)):
    data = unit_rate.dict()
    del data['id']
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    query = f'INSERT INTO unit_rate({columns}) VALUES ({placeholders});'
    db.execute(query, data)
    db.commit()
    return "ok"


@default_api.get("/unit_rate/get/")
async def get_unit_rate(db: Session = Depends(get_db)):
    rs = db.execute("SELECT * FROM unit_rate;").all()
    return rs

@default_api.delete("/unit_rate/delete/")
async def delete_unit_rate(ids: list[int], db: Session = Depends(get_db)):
    for id in ids:
        rs = db.execute(f"SELECT * FROM unit_rate WHERE id = {str(id)};").all()
        if len(rs) == 0:
            raise HTTPException(status_code=404, detail=f"'{str(id)}'")
        db.execute(f"DELETE FROM unit_rate WHERE id = {str(id)};")
    db.commit()
    return "ok"

@default_api.put("/unit_rate/update/")
async def update_unit_rate(unit_rate: Unit_rate = Depends(Unit_rate.as_form), db: Session = Depends(get_db)):
    data = unit_rate.dict()
    id = data['id']
    del data['id']
    list_of_data = [i for i in zip(data.keys(), data.values())]
    print(list_of_data)
    query = 'UPDATE unit_rate SET {}'.format(', '.join("%s='%s'" % (k) for k in list_of_data))
    query = query + ' WHERE id = ' + str(id) + ';'
    print(query)
    db.execute(query)
    db.commit()
    return "ok"


