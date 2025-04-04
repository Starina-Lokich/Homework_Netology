// babel.config.js

module.exports = {
    presets: [
        ['@babel/preset-env', { targets: { browsers: ['last 2 versions'] } }] // Поддержка современных браузеров
    ],
    sourceType: 'unambiguous' // Автоматическое определение типа модулей
};