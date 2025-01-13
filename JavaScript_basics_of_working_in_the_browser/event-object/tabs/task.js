/**
 * Функция инициализации табов на странице
 * Добавляет обработчики событий для переключения между вкладками
 * и их содержимым
 */
document.addEventListener("DOMContentLoaded", () => {
    // Получаем все элементы вкладок
    const tabs = document.querySelectorAll(".tab");
    // Получаем все элементы содержимого вкладок
    const tabContents = document.querySelectorAll(".tab__content");

    // Добавляем обработчик клика для каждой вкладки
    tabs.forEach((tab, index) => {
        tab.addEventListener("click", () => {
            // Удаляем активный класс у всех вкладок и содержимого
            tabs.forEach(tab => {
                tab.classList.remove("tab_active")
            });
            tabContents.forEach(content => {
                content.classList.remove("tab__content_active")
            });

            // Добавляем активный класс к выбранной вкладке
            // и соответствующему ей содержимому по индексу
            tab.classList.add("tab_active");
            tabContents[index].classList.add("tab__content_active");
        });
    });
});
