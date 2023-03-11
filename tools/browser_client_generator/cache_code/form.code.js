const $name$_$action$_template = document.createElement('template');
$name$_$action$_template.innerHTML = /*html*/`
<style>
  .$dash_name$-$action$-$element$ {
    $style$
  }
</style>

<div class="$dash_name$-$action$-$element$">
  <div class="head">$heading$<div>
  $html$
</div>`;

class $proper_name$$proper_action$$proper_element$ extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.appendChild($name$_$action$_template.content.cloneNode(true));
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
window.customElements.define('$dash_name$-$action$-$element$', $proper_name$$proper_action$$proper_element$);