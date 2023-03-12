const nav_template = document.createElement('template');
nav_template.innerHTML = /*html*/ `
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}
</style>
`;

class NavElement extends HTMLElement {
    list_of_nav = []
    nav_list_element = document.createElement('ul');
    section_element = document.createElement('div')
    constructor() {
        super();
        this.attachShadow({ mode: "open" });

        this.querySelectorAll("page-element").forEach((el, i) => {
            this.list_of_nav.push(el.getAttribute("name"))
            let nav_li = document.createElement('li')
            let nav_a = document.createElement('a')
            nav_a.innerText = el.getAttribute("name")
            console.log(el.getAttribute("href"))
            nav_a.setAttribute('href', el.getAttribute("href") || "#")
            nav_a.setAttribute('page_no', i)
            nav_a.addEventListener('click', this.navigate_to_page.bind(this))
            nav_li.appendChild(nav_a)
            this.nav_list_element.appendChild(nav_li)
        })
        // this.insertBefore(this.nav_el_list, this.firstChild)
        this.shadowRoot.appendChild(nav_template.content.cloneNode(true))
        this.shadowRoot.appendChild(this.nav_list_element)
        this.section_element.appendChild(this.querySelector('page-element').cloneNode(true))
        this.shadowRoot.appendChild(this.section_element)
    }

    connectedCallback() {
        this.render();
    }

    navigate_to_page(e) {
        e.preventDefault()
        let page_index = e.target.getAttribute('page_no')
        while (this.section_element.hasChildNodes()) {
            this.section_element.removeChild(this.section_element.firstChild);
        }
        this.section_element.appendChild(this.querySelectorAll('page-element')[page_index].cloneNode(true))
    }

    render() {
    }
}
window.customElements.define('nav-element', NavElement);



const nav_nest_template = document.createElement('template');
nav_nest_template.innerHTML = /*html*/ `
<style>
  .nav-nest-element {
    height: 300px;
  }
</style>

<div class="nav-nest-element">

</div>`;

class NavNestElement extends HTMLElement {
    constructor() {
        super();
        // this.attachShadow({ mode: 'open' });
        this.innerHTML(nav_nest_template.content.cloneNode(true));
    }

    connectedCallback() {
        this.render();
    }

    render() {
    }
}
window.customElements.define('nav-nest-element', NavNestElement);