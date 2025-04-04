// Подключение плагинов
const path = require('path'); // Модуль Node.js для работы с путями
const HtmlWebpackPlugin = require('html-webpack-plugin'); // Генерация HTML-файла
const MiniCssExtractPlugin = require('mini-css-extract-plugin'); // Извлечение CSS в отдельный файл

module.exports = {
    // Точка входа
    entry: './src/index.js', // Основной файл проекта

    // Конфигурация выходного файла
    output: {
        filename: 'bundle.js', // Имя выходного файла
        path: path.resolve(__dirname, 'dist') // Путь к выходному каталогу
    },

    // Настройка загрузчиков (loaders)
    module: {
        rules: [
            // Обработка CSS-файлов
            {
                test: /\.css$/, // Регулярное выражение для поиска CSS-файлов
                use: [MiniCssExtractPlugin.loader, 'css-loader'] // Загрузчики для CSS
            }
        ]
    },

    // Настройка плагинов
    plugins: [
        // Генерация HTML-файла с автоматическим подключением бандла
        new HtmlWebpackPlugin({
            template: './src/index.html' // Шаблон HTML-файла
        }),

        // Извлечение CSS в отдельный файл
        new MiniCssExtractPlugin({
            filename: 'styles.css' // Имя выходного CSS-файла
        })
    ],

    // Режим разработки
    mode: 'development', // Можно изменить на 'production' для финальной сборки

    // Дополнительная настройка для исправления ошибок с sourceType: module
    resolve: {
        fullySpecified: false
    }
};