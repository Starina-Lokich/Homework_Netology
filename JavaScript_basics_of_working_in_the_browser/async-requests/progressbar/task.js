// Находим нужные элементы
const form = document.getElementById('form'); // Форма
const progressElement = document.getElementById('progress'); // Индикатор прогресса

// Добавляем обработчик отправки формы
form.addEventListener('submit', function (event) {
    event.preventDefault(); // Предотвращаем стандартную отправку формы

    const fileInput = document.getElementById('file'); // Поле ввода файла
    const file = fileInput.files[0]; // Получаем выбранный файл

    if (!file) {
        alert('Выберите файл для загрузки!');
        return;
    }

    // Создаем объект FormData для передачи файла
    const formData = new FormData();
    formData.append('file', file);

    // Создаем XMLHttpRequest для отправки файла
    const xhr = new XMLHttpRequest();

    // Устанавливаем URL для отправки
    xhr.open('POST', 'https://students.netoservices.ru/nestjs-backend/upload', true);

    // Обрабатываем событие прогресса загрузки
    xhr.upload.onprogress = function (event) {
        if (event.lengthComputable) {
            const percentComplete = (event.loaded / event.total) * 100; // Рассчитываем процент загрузки
            progressElement.value = percentComplete / 100; // Обновляем значение индикатора
        }
    };

    // Обрабатываем успешное завершение загрузки
    xhr.onload = function () {
        if (xhr.status === 200) {
            alert('Файл успешно загружен!');
        } else {
            alert('Произошла ошибка при загрузке файла.');
        }
    };

    // Обрабатываем ошибки загрузки
    xhr.onerror = function () {
        alert('Произошла ошибка при загрузке файла.');
    };

    // Отправляем данные
    xhr.send(formData);
});