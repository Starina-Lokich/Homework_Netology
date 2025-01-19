function rotateAds() {
    // Находим все ротаторы на странице
    const rotators = document.querySelectorAll(".rotator");

    rotators.forEach(rotator => {
        // Получаем все элементы в ротаторе
        const cases = Array.from(rotator.querySelectorAll(".rotator__case"));
        let currentIndex = cases.findIndex(item => item.classList.contains("rotator__case_active"));

        function rotate() {
            // Удаляем класс активности с текущего элемента
            cases[currentIndex].classList.remove("rotator__case_active");

            // Переходим к следующему элементу или возвращаемся к началу
            currentIndex = (currentIndex + 1) % cases.length;

            // Делаем следующий элемент активным
            const nextCase = cases[currentIndex];
            nextCase.classList.add("rotator__case_active");

            // Устанавливаем цвет текста, если он указан в атрибуте
            if (nextCase.dataset.color) {
                nextCase.style.color = nextCase.dataset.color;
            }

            // Устанавливаем стандартную скорость перехожа, или скорость из атрибута
            const speed = nextCase.dataset.speed ? parseInt(nextCase.dataset.speed) : 1000;

            // планируем следующую ротацию
            setTimeout(rotate, speed);
        }

        // запускаем ротацию
        rotate();
    });
}

document.addEventListener("DOMContentLoaded", rotateAds);

