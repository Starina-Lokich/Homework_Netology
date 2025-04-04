// src/game.js

import Character from './domain.js'; // Импорт класса Character из domain.js

class Game {
  start() {
    console.log('game started');
  }
}

class GameSavingData {
  // Логика сохранения игры
}

function readGameSaving() {
  // Реализация чтения сохранения
}

function writeGameSaving() {
  // Реализация записи сохранения
}

export default Game; // Экспорт класса Game как default
export { GameSavingData, readGameSaving, writeGameSaving }; // Именованный экспорт остальных элементов