const account_create_template = document.createElement('template');
account_create_template.innerHTML = `
<style>
  .account-create-form {
    
  }
</style>

<div class="account-create-form">
  <div class="head">Account<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Account Name</div>
<div >
<input type="text" id="account_name" name="account_name" required>
</div>
<div >Alias</div>
<div >
<input type="text" id="alias" name="alias" >
</div>
<div >Opening Amount</div>
<div >
<input type="number" id="opening_amount" name="opening_amount" required>
</div>
<div >Note</div>
<div >
<input type="text" id="note" name="note" >
</div>
<div >Account Under Id</div>
<div >
<input type="number" id="account_under_id" name="account_under_id" required>
</div>
<div >Account General Option Id</div>
<div >
<input type="number" id="account_general_option_id" name="account_general_option_id" required>
</div>
<div >Account Detail Nominal Id</div>
<div >
<input type="number" id="account_detail_nominal_id" name="account_detail_nominal_id" required>
</div>
<div >Account Detail Personal Tax Id</div>
<div >
<input type="number" id="account_detail_personal_tax_id" name="account_detail_personal_tax_id" required>
</div>
<input type="submit">
</form>

</div>`;

class AccountCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(account_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('account-create-form', AccountCreateForm);

const link_tag__all_table_create_template = document.createElement('template');
link_tag__all_table_create_template.innerHTML = `
<style>
  .link-tag--all-table-create-form {
    
  }
</style>

<div class="link-tag--all-table-create-form">
  <div class="head">Link Tag  All Table<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Tag Id</div>
<div >
<input type="number" id="tag_id" name="tag_id" required>
</div>
<div >Table Name</div>
<div >
<input type="text" id="table_name" name="table_name" required>
</div>
<div >Table Id</div>
<div >
<input type="number" id="table_id" name="table_id" required>
</div>
<input type="submit">
</form>

</div>`;

class LinkTagAllTableCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(link_tag__all_table_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('link-tag--all-table-create-form', LinkTagAllTableCreateForm);

const transaction_entry_create_template = document.createElement('template');
transaction_entry_create_template.innerHTML = `
<style>
  .transaction-entry-create-form {
    
  }
</style>

<div class="transaction-entry-create-form">
  <div class="head">Transaction Entry<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Account Id</div>
<div >
<input type="number" id="account_id" name="account_id" required>
</div>
<div >Ref Account Id</div>
<div >
<input type="number" id="ref_account_id" name="ref_account_id" required>
</div>
<div >Amount Dr</div>
<div >
<input type="number" id="amount_dr" name="amount_dr" required>
</div>
<div >Amount Cr</div>
<div >
<input type="number" id="amount_cr" name="amount_cr" required>
</div>
<div >Narration</div>
<div >
<input type="text" id="narration" name="narration" >
</div>
<div >Voucher Id</div>
<div >
<input type="number" id="voucher_id" name="voucher_id" required>
</div>
<div >Voucher Number</div>
<div >
<input type="text" id="voucher_number" name="voucher_number" required>
</div>
<input type="submit">
</form>

</div>`;

class TransactionEntryCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(transaction_entry_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('transaction-entry-create-form', TransactionEntryCreateForm);

const account_detail_nominal_gst_create_template = document.createElement('template');
account_detail_nominal_gst_create_template.innerHTML = `
<style>
  .account-detail-nominal-gst-create-form {
    
  }
</style>

<div class="account-detail-nominal-gst-create-form">
  <div class="head">Account Detail Nominal Gst<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Describe</div>
<div >
<input type="text" id="describe" name="describe" >
</div>
<div >Hsn</div>
<div >
<input type="text" id="hsn" name="hsn" >
</div>
<div >Is Capital Goods</div>
<div >
<input type="checkbox" id="is_capital_goods" name="is_capital_goods" required>
</div>
<div >Is Rcm Applicable</div>
<div >
<input type="checkbox" id="is_rcm_applicable" name="is_rcm_applicable" required>
</div>
<div >Igst Rate</div>
<div >
<input type="number" id="igst_rate" name="igst_rate" >
</div>
<div >Cess</div>
<div >
<input type="number" id="cess" name="cess" >
</div>
<div >Cess Type</div>
<div >
<input type="text" id="cess_type" name="cess_type" required>
</div>
<div >Bassed On Value</div>
<div >
<input type="number" id="bassed_on_value" name="bassed_on_value" >
</div>
<div >Bassed On Qty Id</div>
<div >
<input type="number" id="bassed_on_qty_id" name="bassed_on_qty_id" >
</div>
<input type="submit">
</form>

</div>`;

class AccountDetailNominalGstCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(account_detail_nominal_gst_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('account-detail-nominal-gst-create-form', AccountDetailNominalGstCreateForm);

const inventory_create_template = document.createElement('template');
inventory_create_template.innerHTML = `
<style>
  .inventory-create-form {
    
  }
</style>

<div class="inventory-create-form">
  <div class="head">Inventory<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Account Name</div>
<div >
<input type="text" id="account_name" name="account_name" required>
</div>
<div >Alias</div>
<div >
<input type="text" id="alias" name="alias" >
</div>
<div >Part No</div>
<div >
<input type="text" id="part_no" name="part_no" >
</div>
<div >Note</div>
<div >
<input type="text" id="note" name="note" >
</div>
<div >Inventory Under Id</div>
<div >
<input type="number" id="inventory_under_id" name="inventory_under_id" required>
</div>
<div >Unit Rate Id</div>
<div >
<input type="number" id="unit_rate_id" name="unit_rate_id" required>
</div>
<div >Is Gst Applicable</div>
<div >
<input type="text" id="is_gst_applicable" name="is_gst_applicable" required>
</div>
<div >Account Detail Nominal Gst Id</div>
<div >
<input type="number" id="account_detail_nominal_gst_id" name="account_detail_nominal_gst_id" required>
</div>
<div >Opening Amount</div>
<div >
<input type="number" id="opening_amount" name="opening_amount" required>
</div>
<div >Opening Qty</div>
<div >
<input type="number" id="opening_qty" name="opening_qty" required>
</div>
<div >Opening Unit Rate Id</div>
<div >
<input type="number" id="opening_unit_rate_id" name="opening_unit_rate_id" required>
</div>
<input type="submit">
</form>

</div>`;

class InventoryCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(inventory_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('inventory-create-form', InventoryCreateForm);

const voucher_create_template = document.createElement('template');
voucher_create_template.innerHTML = `
<style>
  .voucher-create-form {
    
  }
</style>

<div class="voucher-create-form">
  <div class="head">Voucher<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Voucher Number</div>
<div >
<input type="text" id="voucher_number" name="voucher_number" required>
</div>
<div >Data</div>
<div >
<input type="text" id="data" name="data" required>
</div>
<div >Narration</div>
<div >
<input type="text" id="narration" name="narration" >
</div>
<div >Voucher Type Id</div>
<div >
<input type="number" id="voucher_type_id" name="voucher_type_id" required>
</div>
<input type="submit">
</form>

</div>`;

class VoucherCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(voucher_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('voucher-create-form', VoucherCreateForm);

const inventory_under_create_template = document.createElement('template');
inventory_under_create_template.innerHTML = `
<style>
  .inventory-under-create-form {
    
  }
</style>

<div class="inventory-under-create-form">
  <div class="head">Inventory Under<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Inventory Under Name</div>
<div >
<input type="text" id="inventory_under_name" name="inventory_under_name" required>
</div>
<input type="submit">
</form>

</div>`;

class InventoryUnderCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(inventory_under_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('inventory-under-create-form', InventoryUnderCreateForm);

const account_general_option_create_template = document.createElement('template');
account_general_option_create_template.innerHTML = `
<style>
  .account-general-option-create-form {
    
  }
</style>

<div class="account-general-option-create-form">
  <div class="head">Account General Option<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Bill By Bill</div>
<div >
<input type="checkbox" id="bill_by_bill" name="bill_by_bill" required>
</div>
<div >Credit Preiod</div>
<div >
<input type="number" id="credit_preiod" name="credit_preiod" >
</div>
<div >Cost Center</div>
<div >
<input type="checkbox" id="cost_center" name="cost_center" required>
</div>
<input type="submit">
</form>

</div>`;

class AccountGeneralOptionCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(account_general_option_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('account-general-option-create-form', AccountGeneralOptionCreateForm);

const account_detail_nominal_tds_tcs_create_template = document.createElement('template');
account_detail_nominal_tds_tcs_create_template.innerHTML = `
<style>
  .account-detail-nominal-tds-tcs-create-form {
    
  }
</style>

<div class="account-detail-nominal-tds-tcs-create-form">
  <div class="head">Account Detail Nominal Tds Tcs<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Describe</div>
<div >
<input type="text" id="describe" name="describe" >
</div>
<div >Section</div>
<div >
<input type="text" id="section" name="section" required>
</div>
<div >Rate</div>
<div >
<input type="number" id="rate" name="rate" required>
</div>
<div >Tax Limit</div>
<div >
<input type="number" id="tax_limit" name="tax_limit" required>
</div>
<div >Amount Limit</div>
<div >
<input type="number" id="amount_limit" name="amount_limit" required>
</div>
<div >Tds Tcs</div>
<div >
<input type="text" id="tds_tcs" name="tds_tcs" required>
</div>
<input type="submit">
</form>

</div>`;

class AccountDetailNominalTdsTcsCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(account_detail_nominal_tds_tcs_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('account-detail-nominal-tds-tcs-create-form', AccountDetailNominalTdsTcsCreateForm);

const unit_rate_conversion_create_template = document.createElement('template');
unit_rate_conversion_create_template.innerHTML = `
<style>
  .unit-rate-conversion-create-form {
    
  }
</style>

<div class="unit-rate-conversion-create-form">
  <div class="head">Unit Rate Conversion<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Unit From Id</div>
<div >
<input type="number" id="unit_from_id" name="unit_from_id" required>
</div>
<div >Unit To Id</div>
<div >
<input type="number" id="unit_to_id" name="unit_to_id" required>
</div>
<div >Rate Of Conversion</div>
<div >
<input type="number" id="rate_of_conversion" name="rate_of_conversion" required>
</div>
<input type="submit">
</form>

</div>`;

class UnitRateConversionCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(unit_rate_conversion_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('unit-rate-conversion-create-form', UnitRateConversionCreateForm);

const account_detail_nominal_create_template = document.createElement('template');
account_detail_nominal_create_template.innerHTML = `
<style>
  .account-detail-nominal-create-form {
    
  }
</style>

<div class="account-detail-nominal-create-form">
  <div class="head">Account Detail Nominal<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Inventory Value Are Affected</div>
<div >
<input type="checkbox" id="inventory_value_are_affected" name="inventory_value_are_affected" required>
</div>
<div >Type Of Ledger</div>
<div >
<input type="text" id="type_of_ledger" name="type_of_ledger" required>
</div>
<div >Fraction Value</div>
<div >
<input type="number" id="fraction_value" name="fraction_value" >
</div>
<div >Is Gst Applicable</div>
<div >
<input type="text" id="is_gst_applicable" name="is_gst_applicable" required>
</div>
<div >Account Detail Nominal Gst Id</div>
<div >
<input type="number" id="account_detail_nominal_gst_id" name="account_detail_nominal_gst_id" required>
</div>
<div >Is Tds Applicable</div>
<div >
<input type="text" id="is_tds_applicable" name="is_tds_applicable" required>
</div>
<div >Account Detail Nominal Tds Tcs Id</div>
<div >
<input type="number" id="account_detail_nominal_tds_tcs_id" name="account_detail_nominal_tds_tcs_id" required>
</div>
<input type="submit">
</form>

</div>`;

class AccountDetailNominalCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(account_detail_nominal_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('account-detail-nominal-create-form', AccountDetailNominalCreateForm);

const voucher_type_create_template = document.createElement('template');
voucher_type_create_template.innerHTML = `
<style>
  .voucher-type-create-form {
    
  }
</style>

<div class="voucher-type-create-form">
  <div class="head">Voucher Type<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Voucher Number Start From</div>
<div >
<input type="number" id="voucher_number_start_from" name="voucher_number_start_from" required>
</div>
<div >Voucher Number Prefix</div>
<div >
<input type="text" id="voucher_number_prefix" name="voucher_number_prefix" >
</div>
<div >Voucher Number Sufix</div>
<div >
<input type="text" id="voucher_number_sufix" name="voucher_number_sufix" >
</div>
<div >Primary Voucher Type</div>
<div >
<input type="text" id="primary_voucher_type" name="primary_voucher_type" required>
</div>
<div >Prevent Duplicate</div>
<div >
<input type="checkbox" id="prevent_duplicate" name="prevent_duplicate" required>
</div>
<input type="submit">
</form>

</div>`;

class VoucherTypeCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(voucher_type_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('voucher-type-create-form', VoucherTypeCreateForm);

const link_inventory__account__voucher_create_template = document.createElement('template');
link_inventory__account__voucher_create_template.innerHTML = `
<style>
  .link-inventory--account--voucher-create-form {
    
  }
</style>

<div class="link-inventory--account--voucher-create-form">
  <div class="head">Link Inventory  Account  Voucher<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Inventory Id</div>
<div >
<input type="number" id="inventory_id" name="inventory_id" >
</div>
<div >Account Id</div>
<div >
<input type="number" id="account_id" name="account_id" required>
</div>
<div >Transaction Entry Id</div>
<div >
<input type="number" id="transaction_entry_id" name="transaction_entry_id" required>
</div>
<div >Voucher Id</div>
<div >
<input type="number" id="voucher_id" name="voucher_id" required>
</div>
<input type="submit">
</form>

</div>`;

class LinkInventoryAccountVoucherCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(link_inventory__account__voucher_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('link-inventory--account--voucher-create-form', LinkInventoryAccountVoucherCreateForm);

const account_detail_personal_tax_create_template = document.createElement('template');
account_detail_personal_tax_create_template.innerHTML = `
<style>
  .account-detail-personal-tax-create-form {
    
  }
</style>

<div class="account-detail-personal-tax-create-form">
  <div class="head">Account Detail Personal Tax<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Pan</div>
<div >
<input type="text" id="pan" name="pan" >
</div>
<div >It Group</div>
<div >
<input type="text" id="it_group" name="it_group" required>
</div>
<div >Gst No</div>
<div >
<input type="text" id="gst_no" name="gst_no" >
</div>
<div >Gst Group</div>
<div >
<input type="text" id="gst_group" name="gst_group" required>
</div>
<input type="submit">
</form>

</div>`;

class AccountDetailPersonalTaxCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(account_detail_personal_tax_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('account-detail-personal-tax-create-form', AccountDetailPersonalTaxCreateForm);

const tag_create_template = document.createElement('template');
tag_create_template.innerHTML = `
<style>
  .tag-create-form {
    
  }
</style>

<div class="tag-create-form">
  <div class="head">Tag<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Tag Name</div>
<div >
<input type="text" id="tag_name" name="tag_name" required>
</div>
<input type="submit">
</form>

</div>`;

class TagCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(tag_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('tag-create-form', TagCreateForm);

const account_under_create_template = document.createElement('template');
account_under_create_template.innerHTML = `
<style>
  .account-under-create-form {
    
  }
</style>

<div class="account-under-create-form">
  <div class="head">Account Under<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Account Under Name</div>
<div >
<input type="text" id="account_under_name" name="account_under_name" required>
</div>
<div >Primary Group</div>
<div >
<input type="text" id="primary_group" name="primary_group" required>
</div>
<input type="submit">
</form>

</div>`;

class AccountUnderCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(account_under_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('account-under-create-form', AccountUnderCreateForm);

const unit_rate_create_template = document.createElement('template');
unit_rate_create_template.innerHTML = `
<style>
  .unit-rate-create-form {
    
  }
</style>

<div class="unit-rate-create-form">
  <div class="head">Unit Rate<div>
  <form>
<div hidden>Id</div>
<div hidden>
<input type="number" id="id" name="id" >
</div>
<div >Unit Name</div>
<div >
<input type="text" id="unit_name" name="unit_name" required>
</div>
<div >Fraction Count</div>
<div >
<input type="number" id="fraction_count" name="fraction_count" required>
</div>
<input type="submit">
</form>

</div>`;

class UnitRateCreateForm extends HTMLElement{
 constructor(){
     super();
     this.attachShadow({ mode: 'open'});
     this.shadowRoot.appendChild(unit_rate_create_template.content.cloneNode(true));
    //  this.shadowRoot.querySelector('h3').innerText = this.getAttribute('name');
    //  this.shadowRoot.querySelector('img').src = this.getAttribute('avatar');   
 } 

 connectedCallback(){
//    this.h3 = this.getAttribute("name")
   this.render();
 }

 render(){
//    this.h3;
 }
}
window.customElements.define('unit-rate-create-form', UnitRateCreateForm);

