document.addEventListener('DOMContentLoaded', function() {
    const book = document.getElementById('book');
    
    // Обработка изменения размера шрифта
    const fontControls = document.querySelector('.book__control_font-size');
    fontControls.addEventListener('click', (event) => {
        event.preventDefault();
        
        if (event.target.classList.contains('font-size')) {
            // Удаляем активный класс у всех кнопок
            document.querySelectorAll('.font-size').forEach(button => {
                button.classList.remove('font-size_active');
            });
            
            // Добавляем активный класс нажатой кнопке
            event.target.classList.add('font-size_active');
            
            // Удаляем предыдущие классы размера шрифта
            book.classList.remove('book_fs-big', 'book_fs-small');
            
            // Устанавливаем новый размер шрифта
            const size = event.target.dataset.size;
            if (size) {
                book.classList.add(`book_fs-${size}`);
            }
        }
    });

    // Обработка изменения цвета текста
    const textColorControls = document.querySelector('.book__control_color');
    if (textColorControls) {
        textColorControls.addEventListener('click', (event) => {
            event.preventDefault();
            
            if (event.target.classList.contains('color')) {
                // Удаляем активный класс у всех кнопок цвета текста
                textColorControls.querySelectorAll('.color').forEach(button => {
                    button.classList.remove('color_active');
                });
                
                // Добавляем активный класс нажатой кнопке
                event.target.classList.add('color_active');
                
                // Удаляем предыдущие классы цвета текста
                book.classList.remove('book_color-black', 'book_color-gray', 'book_color-whitesmoke');
                
                // Устанавливаем новый цвет текста
                const textColor = event.target.dataset.textColor;
                if (textColor) {
                    book.classList.add(`book_color-${textColor}`);
                }
            }
        });
    }

    // Обработка изменения цвета фона
    const bgColorControls = document.querySelector('.book__control_background');
    if (bgColorControls) {
        bgColorControls.addEventListener('click', (event) => {
            event.preventDefault();
            
            if (event.target.classList.contains('color')) {
                // Удаляем активный класс у всех кнопок цвета фона
                bgColorControls.querySelectorAll('.color').forEach(button => {
                    button.classList.remove('color_active');
                });
                
                // Добавляем активный класс нажатой кнопке
                event.target.classList.add('color_active');
                
                // Удаляем предыдущие классы цвета фона
                book.classList.remove('book_bg-black', 'book_bg-gray', 'book_bg-white');
                
                // Устанавливаем новый цвет фона
                const bgColor = event.target.dataset.bgColor;
                if (bgColor) {
                    book.classList.add(`book_bg-${bgColor}`);
                }
            }
        });
    }
});
