// Элементы DOM
const pollTitle = document.getElementById('poll__title'); // Заголовок опроса
const pollAnswers = document.getElementById('poll__answers'); // Контейнер для ответов

// Функция для создания кнопки ответа
function createAnswerButton(text) {
    const button = document.createElement('button');
    button.className = 'poll__answer';
    button.textContent = text;
    return button;
}

// Шаг 1: Загрузка данных опроса
fetch('https://students.netoservices.ru/nestjs-backend/poll')
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось получить данные опроса');
        }
        return response.json(); // Парсим JSON-ответ
    })
    .then(data => {
        // Заполняем заголовок опроса
        pollTitle.textContent = data.data.title;

        // Создаем кнопки для каждого варианта ответа
        data.data.answers.forEach((answer, index) => {
            const button = createAnswerButton(answer);
            button.addEventListener('click', () => handleVote(data.id, index, answer));
            pollAnswers.appendChild(button);
        });
    })
    .catch(error => {
        console.error('Ошибка при загрузке данных:', error);
    });

// Функция для обработки голоса
function handleVote(pollId, answerIndex, answerText) {
    // Показываем диалоговое окно
    alert('Спасибо, ваш голос засчитан!');

    // Отправляем POST-запрос для голосования
    fetch('https://students.netoservices.ru/nestjs-backend/poll', {
        method: 'POST',
        headers: {
            'Content-type': 'application/x-www-form-urlencoded'
        },
        body: `vote=${pollId}&answer=${answerIndex}`
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Не удалось получить результаты голосования');
            }
            return response.json(); // Парсим JSON-ответ
        })
        .then(data => {
            // Очищаем контейнер с ответами
            pollAnswers.innerHTML = '';

            // Рассчитываем проценты для каждого варианта ответа
            const totalVotes = data.stat.reduce((sum, item) => sum + item.votes, 0);

            // Отображаем результаты голосования
            const resultsTitle = document.createElement('div');
            resultsTitle.textContent = 'Результаты голосования:';
            pollAnswers.appendChild(resultsTitle);

            data.stat.forEach(stat => {
                const resultItem = document.createElement('div');
                const percentage = ((stat.votes / totalVotes) * 100).toFixed(2); // Проценты с двумя знаками после запятой
                resultItem.textContent = `${stat.answer}: ${stat.votes} голосов (${percentage}%)`;
                pollAnswers.appendChild(resultItem);
            });
        })
        .catch(error => {
            console.error('Ошибка при получении результатов:', error);
        });
}