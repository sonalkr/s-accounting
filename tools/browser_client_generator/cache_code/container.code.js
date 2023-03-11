const container_template = document.createElement('template');
container_template.innerHTML = /*html*/`
<style>
  .container-element {
    
  }
</style>

<div class="container-element">

</div>`;

class ContainerElement extends HTMLElement {
  constructor() {
    super();
    // this.attachShadow({ mode: "open" });

  }

  connectedCallback() {
    this.render();
  }

  render() {
  }
}
window.customElements.define('container-element', ContainerElement);