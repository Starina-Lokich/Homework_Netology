// Получаем элементы для счётчиков
const deadCounter = document.getElementById("dead");
const lostCounter = document.getElementById("lost");

// Функция для получения лунки по индексу
const getHole = (index) => document.getElementById(`hole${index}`);

// Функция для обработки клика по лунке
function handleClik(event) {
    const hole = event.target;
    
    // Проверяем, есть ли крот в лунке
    if (hole.classList.contains('hole_has-mole')) {
        // Увеличиваем счётчик побед
        deadCounter.textContent = parseInt(deadCounter.textContent) + 1;
    } else {
        // Увеличиваем счётчик поражений
        lostCounter.textContent = parseInt(lostCounter.textContent) + 1;
    }

    // Проверяем условия победы или поражения
    if (parseInt(deadCounter.textContent) === 10) {
        alert('Победа! Вы убили 10 кротов!');
        resetGame();
    } else if (parseInt(lostCounter.textContent) === 5) {
        alert('Поражение! Вы допустили 5 промахов.');
        resetGame();
    }
}

// Функция для сброса игры
function resetGame() {
    deadCounter.textContent = 0;
    lostCounter.textContent = 0;
}

// Регистрируем обработчики кликов для всех лунок
for (let i = 1; i <= 9; i++) {
    getHole(i).addEventListener("click", handleClik);
}