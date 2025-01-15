document.addEventListener("scroll", function () {
    // Получаем все элементы с классом reval
    const reveals = document.querySelectorAll(".reveal");

    reveals.forEach(element => {
        // Узнаем положение элемента
        const elementPosition = element.getBoundingClientRect();
        // Получаем булевый результат true, если элемент виден, а иначе false
        const isVisible = (elementPosition.top < window.innerHeight) && 
                         (elementPosition.bottom > 0);

        // Если элемент виден, добавляем класс reveal_active
        if (isVisible) {
            element.classList.add("reveal_active");
        } else {
            element.classList.remove("reveal_active");
        }
    });
});