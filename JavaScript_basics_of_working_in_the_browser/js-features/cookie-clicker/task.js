// //Обычный уровень сложности
// const cookieImg = document.getElementById("cookie");
// const clickCounter = document.getElementById("clicker__counter");

// let isCookieBig = false;

// cookieImg.onclick = function () {
//     // Увеличиваем счётчик кликов
//     clickCounter.textContent = parseInt(clickCounter.textContent) + 1;

//     // Чередуем размер 
//     if (isCookieBig) {
//         cookieImg.width = 200; // Возвращаем исходный размер
//     } else {
//         cookieImg.width = 250; // Увеличиваем размер
//     }

//     // Меняем состояние размера
//     isCookieBig = !isCookieBig;
// };


//Повышенный уровень сложности
const cookieImg = document.getElementById('cookie'); // Печенька
const clickCounter = document.getElementById('clicker__counter'); // Счётчик кликов
const clickSpeed = document.createElement('div'); // Элемент для отображения скорости клика

// Добавляем элемент скорости клика в DOM
clickSpeed.id = 'clicker__speed';
clickSpeed.textContent = 'Скорость клика: 0 кликов/сек';
document.querySelector('.clicker').appendChild(clickSpeed);

// Переменные для хранения данных
let lastClickTime = null; // Время последнего клика
let clickCount = 0; // Общее количество кликов

// Обработчик клика на печеньку
cookieImg.onclick = function () {
    const currentTime = new Date(); // Текущее время

    // Увеличиваем счётчик кликов
    clickCount++;
    clickCounter.textContent = clickCount;

    // Если это не первый клик, вычисляем скорость
    if (lastClickTime !== null) {
        const timeDiff = (currentTime - lastClickTime) / 1000; // Разница во времени в секундах
        const speed = 1 / timeDiff; // Скорость клика (кликов в секунду)

        // Обновляем значение скорости
        clickSpeed.textContent = `Скорость клика: ${speed.toFixed(2)} кликов/сек`;
    }

    // Обновляем время последнего клика
    lastClickTime = currentTime;

    // Чередуем размер печеньки (опционально)
    cookieImg.width = cookieImg.width === 200 ? 250 : 200;
};