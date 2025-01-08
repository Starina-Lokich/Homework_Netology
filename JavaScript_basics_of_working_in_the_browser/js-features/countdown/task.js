// // Обычный уровень сложности
// // Получаем значение таймера
// const timerValue = document.getElementById("timer");

// // Устанавливаем начальное значение таймера
// let timerStart = parseInt(timerValue.textContent, 10);

// // Функция обновления таймера
// function updateTimer() {
//     timerStart--;

//     timerValue.textContent = timerStart;

//     if (timerStart <= 0) {
//         clearInterval(timerInterval);
//         timerValue.textContent = "0";
//         alert("Вы победили в конкурсе");
//     }
// }

// // Запускаем таймер
// const timerInterval = setInterval(updateTimer, 1000);


// Повышенный уровень сложности
// Получаем значение таймера
const timerValue = document.getElementById("timer");

// Устанавливаем начальное значение таймера
let timerStart = parseInt(timerValue.textContent, 10);

// Функция для обновления таймера
function updateTimer() {
    timerStart--;

    // Если время вышло, останавливаем таймер
    if (timerStart <= 0) {
        clearInterval(timerInterval);
        alert("Вы победили в конкурсе");
        timerValue.textContent = "00:00:00";
        return;
    }

    // Обновляем отображение таймера
    timerValue.textContent = formatTime(timerStart);
}

// Функция для форматирования времени
function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${pad(hours)}:${pad(minutes)}:${pad(secs)}`;
}

// Функция для добавления нуля, если число меньше 10
function pad(number) {
    return number < 10 ? `0${number}` : number;
}

// Запускаем таймер, обновляя его каждую секунду
const timerInterval = setInterval(updateTimer, 1000);

// Инициализация таймера
updateTimer();