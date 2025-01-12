class Dropdown {
    constructor(container) {
        this.container = container;
        this.value = container.querySelector('.dropdown__value');
        this.list = container.querySelector('.dropdown__list');
        this.links = container.querySelectorAll('.dropdown__link');

        this.value.addEventListener("click", () => this.toggleDropdown());

        this.links.forEach(link => {
            link.addEventListener("click", (event) => {
                event.preventDefault();
                this.value.textContent = link.textContent;
                this.hideDropdown();
            });
        });
    }

    toggleDropdown() {
        this.list.classList.toggle("dropdown__list_active");
    }

    hideDropdown() {
        this.list.classList.remove("dropdown__list_active");
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const dropdowns = document.querySelectorAll('.dropdown');    // Находим все выпадающие списки на странице
    dropdowns.forEach(dropdown => new Dropdown(dropdown));       // Создаём для каждого экземпляр класса Dropdown
});
