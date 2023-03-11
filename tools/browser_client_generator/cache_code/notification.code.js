const notification_template = document.createElement('template');
notification_template.innerHTML = /*html*/`
<style>
  .notification-element {
    
  }
</style>

<div class="notification-element">

</div>`;

class NotificationElement extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.appendChild(notification_template.content.cloneNode(true));
    }

    connectedCallback() {
        this.render();
    }

    render() {
    }
}
window.customElements.define('notification-element', NotificationElement);