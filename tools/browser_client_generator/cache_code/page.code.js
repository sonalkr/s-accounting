const page_template = document.createElement('template');
page_template.innerHTML = /*html*/ `
<style>
  .page-element {
    
  }
</style>

<div class="page-element">

</div>`;

class PageElement extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
    }

    render() {
    }
}
window.customElements.define('page-element', PageElement);