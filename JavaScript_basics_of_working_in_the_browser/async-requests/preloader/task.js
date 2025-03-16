// Находим необходимые элементы
const loader = document.getElementById('loader'); // Анимация загрузки
const itemsContainer = document.getElementById('items'); // Контейнер для отображения валют

// Функция для создания элемента валюты
function createCurrencyItem(code, value) {
    const item = document.createElement('div');
    item.className = 'item';

    const codeDiv = document.createElement('div');
    codeDiv.className = 'item__code';
    codeDiv.textContent = code;

    const  valueDiv = document.createElement('div');
    valueDiv.className = 'item__value';
    valueDiv.textContent = value;

    const currencyDiv = document.createElement('div');
    currencyDiv.className = 'item__currency';
    currencyDiv.textContent = 'руб.';

    item.appendChild(codeDiv);
    item.appendChild(valueDiv);
    item.appendChild(currencyDiv);

    return item;
}

// Отправляем GET-запрос на сервер для получения курса валют
fetch('https://students.netoservices.ru/nestjs-backend/slow-get-courses')
    .then(response => {
        if (!response.ok) {
            throw new Error('Не удалось получить данные о валюте');
        }
        return response.json(); // Парсим JSON-ответ
    })
    .then(data => {
        // Скрываем анимацию загрузки
        loader.classList.remove('loader_active');

        // Получаем список валют из ответа
        const valuteData = data.response.Valute;

        // Создаем элементы для каждой валюты и добавляем их в контейнер
        for (const key in valuteData) {
            if (valuteData.hasOwnProperty(key)) {
                const currency = valuteData[key];
                const currencyItem = createCurrencyItem(
                    currency.CharCode, // Код валюты
                    currency.Value.toFixed(2) // Значение валюты (с двумя знаками после запятой)
                );
                itemsContainer.appendChild(currencyItem);
            }
        }
    })
    .catch(error => {
        // В случае ошибки скрываем анимацию загрузки и выводим сообщение об ошибке
        loader.classList.remove('loader_active');
        console.error('Ошибка при загрузке данных:', error);
    });