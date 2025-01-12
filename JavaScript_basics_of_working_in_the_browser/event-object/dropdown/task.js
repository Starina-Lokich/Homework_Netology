/**
 * Класс, представляющий выпадающий список
 */
class Dropdown {
    /**
     * Создает экземпляр выпадающего списка
     * @param {HTMLElement} container - DOM элемент, содержащий выпадающий список
     */
    constructor(container) {
        // Сохраняем корневой элемент выпадающего списка
        this.container = container;
        // Находим элемент, отображающий текущее выбранное значение
        this.value = container.querySelector('.dropdown__value');
        // Находим сам выпадающий список
        this.list = container.querySelector('.dropdown__list');
        // Получаем все ссылки внутри списка
        this.links = container.querySelectorAll('.dropdown__link');

        // Добавляем обработчик клика для отображения/скрытия списка
        this.value.addEventListener("click", () => this.toggleDropdown());

        // Добавляем обработчики для каждой ссылки в списке
        this.links.forEach(link => {
            link.addEventListener("click", (event) => {
                // Предотвращаем стандартное поведение ссылки
                event.preventDefault();
                // Обновляем текст выбранного значения
                this.value.textContent = link.textContent;
                // Скрываем список после выбора
                this.hideDropdown();
            });
        });
    }

    /**
     * Переключает отображение выпадающего списка
     */
    toggleDropdown() {
        // Добавляем или удаляем класс активности для отображения/скрытия списка
        this.list.classList.toggle("dropdown__list_active");
    }

    /**
     * Скрывает выпадающий список
     */
    hideDropdown() {
        // Удаляем класс активности, чтобы скрыть список
        this.list.classList.remove("dropdown__list_active");
    }
}

// Ждем полной загрузки DOM перед инициализацией
document.addEventListener('DOMContentLoaded', () => {
    const dropdowns = document.querySelectorAll('.dropdown');    // Находим все выпадающие списки на странице
    dropdowns.forEach(dropdown => new Dropdown(dropdown));       // Создаём для каждого экземпляр класса Dropdown
});

