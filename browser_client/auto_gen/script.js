const account_create_template = document.createElement('template');
account_create_template.innerHTML = /*html*/`
<style>
  .account-create-form {
    
  }
</style>

<div class="account-create-form">
  <div class="head">Account<div>
  <form action="/account/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="account_name">Account Name</label>
<input type="text" id="account_name" name="account_name" required>
</div>
<div >
<label for="alias">Alias</label>
<input type="text" id="alias" name="alias" >
</div>
<div >
<label for="opening_amount">Opening Amount</label>
<input type="number" id="opening_amount" name="opening_amount" required>
</div>
<div >
<label for="note">Note</label>
<input type="text" id="note" name="note" >
</div>
<div >
<label for="account_under_id">Account Under Id</label>
<input type="number" id="account_under_id" name="account_under_id" required>
</div>
<div >
<label for="account_general_option_id">Account General Option Id</label>
<input type="number" id="account_general_option_id" name="account_general_option_id" required>
</div>
<div >
<label for="account_detail_nominal_id">Account Detail Nominal Id</label>
<input type="number" id="account_detail_nominal_id" name="account_detail_nominal_id" required>
</div>
<div >
<label for="account_detail_personal_tax_id">Account Detail Personal Tax Id</label>
<input type="number" id="account_detail_personal_tax_id" name="account_detail_personal_tax_id" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class AccountCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(account_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('account-create-form', AccountCreateForm);

const link_tag__all_table_create_template = document.createElement('template');
link_tag__all_table_create_template.innerHTML = /*html*/`
<style>
  .link-tag--all-table-create-form {
    
  }
</style>

<div class="link-tag--all-table-create-form">
  <div class="head">Link Tag  All Table<div>
  <form action="/link_tag__all_table/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="tag_id">Tag Id</label>
<input type="number" id="tag_id" name="tag_id" required>
</div>
<div >
<label for="table_name">Table Name</label>
<input type="text" id="table_name" name="table_name" required>
</div>
<div >
<label for="table_id">Table Id</label>
<input type="number" id="table_id" name="table_id" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class LinkTagAllTableCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(link_tag__all_table_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('link-tag--all-table-create-form', LinkTagAllTableCreateForm);

const link_inventory__account__voucher_create_template = document.createElement('template');
link_inventory__account__voucher_create_template.innerHTML = /*html*/`
<style>
  .link-inventory--account--voucher-create-form {
    
  }
</style>

<div class="link-inventory--account--voucher-create-form">
  <div class="head">Link Inventory  Account  Voucher<div>
  <form action="/link_inventory__account__voucher/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="inventory_id">Inventory Id</label>
<input type="number" id="inventory_id" name="inventory_id" >
</div>
<div >
<label for="account_id">Account Id</label>
<input type="number" id="account_id" name="account_id" required>
</div>
<div >
<label for="transaction_entry_id">Transaction Entry Id</label>
<input type="number" id="transaction_entry_id" name="transaction_entry_id" required>
</div>
<div >
<label for="voucher_id">Voucher Id</label>
<input type="number" id="voucher_id" name="voucher_id" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class LinkInventoryAccountVoucherCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(link_inventory__account__voucher_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('link-inventory--account--voucher-create-form', LinkInventoryAccountVoucherCreateForm);

const transaction_single_create_template = document.createElement('template');
transaction_single_create_template.innerHTML = /*html*/`
<style>
  .transaction-single-create-form {
    
  }
</style>

<div class="transaction-single-create-form">
  <div class="head">Transaction Single<div>
  <form action="/transaction_single/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="transaction_entry_id">Transaction Entry Id</label>
<input type="number" id="transaction_entry_id" name="transaction_entry_id" required>
</div>
<div >
<label for="account_id">Account Id</label>
<input type="number" id="account_id" name="account_id" required>
</div>
<div >
<label for="amount_dr">Amount Dr</label>
<input type="number" id="amount_dr" name="amount_dr" >
</div>
<div >
<label for="amount_cr">Amount Cr</label>
<input type="number" id="amount_cr" name="amount_cr" >
</div>
<input type="submit" value="Create">
</form>

</div>`;

class TransactionSingleCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(transaction_single_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('transaction-single-create-form', TransactionSingleCreateForm);

const account_detail_nominal_gst_create_template = document.createElement('template');
account_detail_nominal_gst_create_template.innerHTML = /*html*/`
<style>
  .account-detail-nominal-gst-create-form {
    
  }
</style>

<div class="account-detail-nominal-gst-create-form">
  <div class="head">Account Detail Nominal Gst<div>
  <form action="/account_detail_nominal_gst/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="describe">Describe</label>
<input type="text" id="describe" name="describe" >
</div>
<div >
<label for="hsn">Hsn</label>
<input type="text" id="hsn" name="hsn" >
</div>
<div >
<label for="is_capital_goods">Is Capital Goods</label>
<input type="checkbox" id="is_capital_goods" name="is_capital_goods" >
</div>
<div >
<label for="is_rcm_applicable">Is Rcm Applicable</label>
<input type="checkbox" id="is_rcm_applicable" name="is_rcm_applicable" >
</div>
<div >
<label for="igst_rate">Igst Rate</label>
<input type="number" id="igst_rate" name="igst_rate" >
</div>
<div >
<label for="cess">Cess</label>
<input type="number" id="cess" name="cess" >
</div>
<div >
<label for="cess_type">Cess Type</label>
<input type="text" id="cess_type" name="cess_type" >
</div>
<div >
<label for="bassed_on_value">Bassed On Value</label>
<input type="number" id="bassed_on_value" name="bassed_on_value" >
</div>
<div >
<label for="bassed_on_qty_id">Bassed On Qty Id</label>
<input type="number" id="bassed_on_qty_id" name="bassed_on_qty_id" >
</div>
<input type="submit" value="Create">
</form>

</div>`;

class AccountDetailNominalGstCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(account_detail_nominal_gst_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('account-detail-nominal-gst-create-form', AccountDetailNominalGstCreateForm);

const inventory_create_template = document.createElement('template');
inventory_create_template.innerHTML = /*html*/`
<style>
  .inventory-create-form {
    
  }
</style>

<div class="inventory-create-form">
  <div class="head">Inventory<div>
  <form action="/inventory/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="account_name">Account Name</label>
<input type="text" id="account_name" name="account_name" required>
</div>
<div >
<label for="alias">Alias</label>
<input type="text" id="alias" name="alias" >
</div>
<div >
<label for="part_no">Part No</label>
<input type="text" id="part_no" name="part_no" >
</div>
<div >
<label for="note">Note</label>
<input type="text" id="note" name="note" >
</div>
<div >
<label for="inventory_under_id">Inventory Under Id</label>
<input type="number" id="inventory_under_id" name="inventory_under_id" required>
</div>
<div >
<label for="unit_rate_id">Unit Rate Id</label>
<input type="number" id="unit_rate_id" name="unit_rate_id" required>
</div>
<div >
<label for="is_gst_applicable">Is Gst Applicable</label>
<input type="text" id="is_gst_applicable" name="is_gst_applicable" required>
</div>
<div >
<label for="account_detail_nominal_gst_id">Account Detail Nominal Gst Id</label>
<input type="number" id="account_detail_nominal_gst_id" name="account_detail_nominal_gst_id" required>
</div>
<div >
<label for="opening_amount">Opening Amount</label>
<input type="number" id="opening_amount" name="opening_amount" required>
</div>
<div >
<label for="opening_qty">Opening Qty</label>
<input type="number" id="opening_qty" name="opening_qty" required>
</div>
<div >
<label for="opening_unit_rate_id">Opening Unit Rate Id</label>
<input type="number" id="opening_unit_rate_id" name="opening_unit_rate_id" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class InventoryCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(inventory_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('inventory-create-form', InventoryCreateForm);

const voucher_create_template = document.createElement('template');
voucher_create_template.innerHTML = /*html*/`
<style>
  .voucher-create-form {
    
  }
</style>

<div class="voucher-create-form">
  <div class="head">Voucher<div>
  <form action="/voucher/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="voucher_number">Voucher Number</label>
<input type="text" id="voucher_number" name="voucher_number" required>
</div>
<div >
<label for="data">Data</label>
<input type="text" id="data" name="data" required>
</div>
<div >
<label for="narration">Narration</label>
<input type="text" id="narration" name="narration" >
</div>
<div >
<label for="voucher_type_id">Voucher Type Id</label>
<input type="number" id="voucher_type_id" name="voucher_type_id" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class VoucherCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(voucher_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('voucher-create-form', VoucherCreateForm);

const transaction_entry_create_template = document.createElement('template');
transaction_entry_create_template.innerHTML = /*html*/`
<style>
  .transaction-entry-create-form {
    
  }
</style>

<div class="transaction-entry-create-form">
  <div class="head">Transaction Entry<div>
  <form action="/transaction_entry/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="account_id">Account Id</label>
<input type="number" id="account_id" name="account_id" required>
</div>
<div >
<label for="narration">Narration</label>
<input type="text" id="narration" name="narration" >
</div>
<div >
<label for="voucher_id">Voucher Id</label>
<input type="number" id="voucher_id" name="voucher_id" required>
</div>
<div >
<label for="voucher_number">Voucher Number</label>
<input type="text" id="voucher_number" name="voucher_number" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class TransactionEntryCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(transaction_entry_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('transaction-entry-create-form', TransactionEntryCreateForm);

const inventory_under_create_template = document.createElement('template');
inventory_under_create_template.innerHTML = /*html*/`
<style>
  .inventory-under-create-form {
    
  }
</style>

<div class="inventory-under-create-form">
  <div class="head">Inventory Under<div>
  <form action="/inventory_under/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="inventory_under_name">Inventory Under Name</label>
<input type="text" id="inventory_under_name" name="inventory_under_name" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class InventoryUnderCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(inventory_under_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('inventory-under-create-form', InventoryUnderCreateForm);

const account_general_option_create_template = document.createElement('template');
account_general_option_create_template.innerHTML = /*html*/`
<style>
  .account-general-option-create-form {
    
  }
</style>

<div class="account-general-option-create-form">
  <div class="head">Account General Option<div>
  <form action="/account_general_option/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="bill_by_bill">Bill By Bill</label>
<input type="checkbox" id="bill_by_bill" name="bill_by_bill" >
</div>
<div >
<label for="credit_preiod">Credit Preiod</label>
<input type="number" id="credit_preiod" name="credit_preiod" >
</div>
<div >
<label for="cost_center">Cost Center</label>
<input type="checkbox" id="cost_center" name="cost_center" >
</div>
<input type="submit" value="Create">
</form>

</div>`;

class AccountGeneralOptionCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(account_general_option_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('account-general-option-create-form', AccountGeneralOptionCreateForm);

const account_detail_nominal_tds_tcs_create_template = document.createElement('template');
account_detail_nominal_tds_tcs_create_template.innerHTML = /*html*/`
<style>
  .account-detail-nominal-tds-tcs-create-form {
    
  }
</style>

<div class="account-detail-nominal-tds-tcs-create-form">
  <div class="head">Account Detail Nominal Tds Tcs<div>
  <form action="/account_detail_nominal_tds_tcs/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="describe">Describe</label>
<input type="text" id="describe" name="describe" >
</div>
<div >
<label for="section">Section</label>
<input type="text" id="section" name="section" required>
</div>
<div >
<label for="rate">Rate</label>
<input type="number" id="rate" name="rate" required>
</div>
<div >
<label for="tax_limit">Tax Limit</label>
<input type="number" id="tax_limit" name="tax_limit" required>
</div>
<div >
<label for="amount_limit">Amount Limit</label>
<input type="number" id="amount_limit" name="amount_limit" required>
</div>
<div >
<label for="tds_tcs">Tds Tcs</label>
<input type="text" id="tds_tcs" name="tds_tcs" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class AccountDetailNominalTdsTcsCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(account_detail_nominal_tds_tcs_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('account-detail-nominal-tds-tcs-create-form', AccountDetailNominalTdsTcsCreateForm);

const unit_rate_conversion_create_template = document.createElement('template');
unit_rate_conversion_create_template.innerHTML = /*html*/`
<style>
  .unit-rate-conversion-create-form {
    
  }
</style>

<div class="unit-rate-conversion-create-form">
  <div class="head">Unit Rate Conversion<div>
  <form action="/unit_rate_conversion/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="unit_from_id">Unit From Id</label>
<input type="number" id="unit_from_id" name="unit_from_id" required>
</div>
<div >
<label for="unit_to_id">Unit To Id</label>
<input type="number" id="unit_to_id" name="unit_to_id" required>
</div>
<div >
<label for="rate_of_conversion">Rate Of Conversion</label>
<input type="number" id="rate_of_conversion" name="rate_of_conversion" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class UnitRateConversionCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(unit_rate_conversion_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('unit-rate-conversion-create-form', UnitRateConversionCreateForm);

const account_detail_nominal_create_template = document.createElement('template');
account_detail_nominal_create_template.innerHTML = /*html*/`
<style>
  .account-detail-nominal-create-form {
    
  }
</style>

<div class="account-detail-nominal-create-form">
  <div class="head">Account Detail Nominal<div>
  <form action="/account_detail_nominal/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="inventory_value_are_affected">Inventory Value Are Affected</label>
<input type="checkbox" id="inventory_value_are_affected" name="inventory_value_are_affected" required>
</div>
<div >
<label for="type_of_ledger">Type Of Ledger</label>
<input type="text" id="type_of_ledger" name="type_of_ledger" required>
</div>
<div >
<label for="fraction_value">Fraction Value</label>
<input type="number" id="fraction_value" name="fraction_value" >
</div>
<div >
<label for="is_gst_applicable">Is Gst Applicable</label>
<input type="text" id="is_gst_applicable" name="is_gst_applicable" required>
</div>
<div >
<label for="account_detail_nominal_gst_id">Account Detail Nominal Gst Id</label>
<input type="number" id="account_detail_nominal_gst_id" name="account_detail_nominal_gst_id" required>
</div>
<div >
<label for="is_tds_applicable">Is Tds Applicable</label>
<input type="text" id="is_tds_applicable" name="is_tds_applicable" required>
</div>
<div >
<label for="account_detail_nominal_tds_tcs_id">Account Detail Nominal Tds Tcs Id</label>
<input type="number" id="account_detail_nominal_tds_tcs_id" name="account_detail_nominal_tds_tcs_id" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class AccountDetailNominalCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(account_detail_nominal_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('account-detail-nominal-create-form', AccountDetailNominalCreateForm);

const voucher_type_create_template = document.createElement('template');
voucher_type_create_template.innerHTML = /*html*/`
<style>
  .voucher-type-create-form {
    
  }
</style>

<div class="voucher-type-create-form">
  <div class="head">Voucher Type<div>
  <form action="/voucher_type/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="voucher_number_start_from">Voucher Number Start From</label>
<input type="number" id="voucher_number_start_from" name="voucher_number_start_from" required>
</div>
<div >
<label for="voucher_number_prefix">Voucher Number Prefix</label>
<input type="text" id="voucher_number_prefix" name="voucher_number_prefix" >
</div>
<div >
<label for="voucher_number_sufix">Voucher Number Sufix</label>
<input type="text" id="voucher_number_sufix" name="voucher_number_sufix" >
</div>
<div >
<label for="primary_voucher_type">Primary Voucher Type</label>
<input type="text" id="primary_voucher_type" name="primary_voucher_type" required>
</div>
<div >
<label for="prevent_duplicate">Prevent Duplicate</label>
<input type="checkbox" id="prevent_duplicate" name="prevent_duplicate" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class VoucherTypeCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(voucher_type_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('voucher-type-create-form', VoucherTypeCreateForm);

const account_detail_personal_tax_create_template = document.createElement('template');
account_detail_personal_tax_create_template.innerHTML = /*html*/`
<style>
  .account-detail-personal-tax-create-form {
    
  }
</style>

<div class="account-detail-personal-tax-create-form">
  <div class="head">Account Detail Personal Tax<div>
  <form action="/account_detail_personal_tax/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="pan">Pan</label>
<input type="text" id="pan" name="pan" >
</div>
<div >
<label for="it_group">It Group</label>
<input type="text" id="it_group" name="it_group" required>
</div>
<div >
<label for="gst_no">Gst No</label>
<input type="text" id="gst_no" name="gst_no" >
</div>
<div >
<label for="gst_group">Gst Group</label>
<input type="text" id="gst_group" name="gst_group" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class AccountDetailPersonalTaxCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(account_detail_personal_tax_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('account-detail-personal-tax-create-form', AccountDetailPersonalTaxCreateForm);

const tag_create_template = document.createElement('template');
tag_create_template.innerHTML = /*html*/`
<style>
  .tag-create-form {
    
  }
</style>

<div class="tag-create-form">
  <div class="head">Tag<div>
  <form action="/tag/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="tag_name">Tag Name</label>
<input type="text" id="tag_name" name="tag_name" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class TagCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(tag_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('tag-create-form', TagCreateForm);

const account_under_create_template = document.createElement('template');
account_under_create_template.innerHTML = /*html*/`
<style>
  .account-under-create-form {
    
  }
</style>

<div class="account-under-create-form">
  <div class="head">Account Under<div>
  <form action="/account_under/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="account_under_name">Account Under Name</label>
<input type="text" id="account_under_name" name="account_under_name" required>
</div>
<div >
<label for="primary_group">Primary Group</label>
<input type="text" id="primary_group" name="primary_group" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class AccountUnderCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(account_under_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('account-under-create-form', AccountUnderCreateForm);

const unit_rate_create_template = document.createElement('template');
unit_rate_create_template.innerHTML = /*html*/`
<style>
  .unit-rate-create-form {
    
  }
</style>

<div class="unit-rate-create-form">
  <div class="head">Unit Rate<div>
  <form action="/unit_rate/create/" method="post">
<div hidden>
<label for="id">Id</label>
<input type="number" id="id" name="id" >
</div>
<div >
<label for="unit_name">Unit Name</label>
<input type="text" id="unit_name" name="unit_name" required>
</div>
<div >
<label for="fraction_count">Fraction Count</label>
<input type="number" id="fraction_count" name="fraction_count" required>
</div>
<input type="submit" value="Create">
</form>

</div>`;

class UnitRateCreateForm extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild(unit_rate_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
  }

  connectedCallback() {
    //    this.h3 = this.getAttribute("name")
    this.render();
  }

  render() {
    //    this.h3;
  }
}
window.customElements.define('unit-rate-create-form', UnitRateCreateForm);

