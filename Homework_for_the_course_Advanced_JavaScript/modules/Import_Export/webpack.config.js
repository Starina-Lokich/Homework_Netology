// webpack.config.js

const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    // Точка входа
    entry: './src/app.js',

    // Конфигурация выходного файла
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'dist')
    },

    // Настройка загрузчиков (loaders)
    module: {
        rules: [
            {
                test: /\.js$/, // Регулярное выражение для поиска JS-файлов
                exclude: /node_modules/, // Исключаем папку node_modules
                use: {
                    loader: 'babel-loader', // Добавляем Babel для транспиляции ES6+
                    options: {
                        presets: ['@babel/preset-env'], // Поддержка современного синтаксиса
                        sourceType: 'unambiguous' // Автоматическое определение типа модулей
                    }
                }
            }
        ]
    },

    // Настройка плагинов
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html' // Шаблон HTML-файла
        })
    ],

    // Режим разработки
    mode: 'development', // Можно изменить на 'production' для финальной сборки

    // Дополнительная настройка для исправления ошибок с sourceType: module
    resolve: {
        fullySpecified: false // Отключение строгой проверки модулей
    }
};