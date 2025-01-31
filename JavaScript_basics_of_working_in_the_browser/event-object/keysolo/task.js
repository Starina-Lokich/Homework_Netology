class Game {
  constructor(container) {
    this.container = container;
    this.wordElement = container.querySelector('.word');
    this.winsElement = container.querySelector('.status__wins');
    this.lossElement = container.querySelector('.status__loss');
    this.timerLimit = 0; // Лимит времени для ввода слова
    this.timer = null; // Идентификатор таймера

    this.reset();

    this.registerEvents();
  }

  reset() {
    this.setNewWord();
    this.winsElement.textContent = 0;
    this.lossElement.textContent = 0;
  }

  registerEvents() {
    /*
      TODO:
      Написать обработчик события, который откликается
      на каждый введённый символ.
      В случае правильного ввода символа вызываем this.success()
      При неправильном вводе символа - this.fail();
      DOM-элемент текущего символа находится в свойстве this.currentSymbol.
     */
      document.addEventListener("keyup", (event) => {
        const inputChair = event.key.toLowerCase();
        const currentChar = this.currentSymbol.textContent.toLowerCase();
    
        if (inputChair === currentChar) {
          this.success();
        } else {
          this.fail();
        }
      });
  }

  success() {
    if(this.currentSymbol.classList.contains("symbol_current")) this.currentSymbol.classList.remove("symbol_current");
    this.currentSymbol.classList.add('symbol_correct');
    this.currentSymbol = this.currentSymbol.nextElementSibling;

    if (this.currentSymbol !== null) {
      this.currentSymbol.classList.add('symbol_current');
      return;
    }

    if (++this.winsElement.textContent === 10) {
      alert('Победа!');
      this.reset();
    }
    this.setNewWord();
  }

  fail() {
    if (++this.lossElement.textContent === 5) {
      alert('Вы проиграли!');
      this.reset();
    }
    this.setNewWord();
  }

  /**
   * Устанавливает новое слово для игры и запускает таймер.
   * Изменения, произведенные в рамках задания:
   * - Установка лимита времени для ввода слова в зависимости от его длины.
   * - Запуск таймера, который отсчитывает время до истечения лимита.
   * - Использование свойства класса `timer` для управления таймером,
   *   что позволяет останавливать предыдущий таймер перед запуском нового.
   */
  setNewWord() {
    const word = this.getWord();

    this.renderWord(word);
    // Устанавливаем лимит времени в зависимости от длины слова
    this.timerLimit = word.length;
    this.startTimer(); // Запускаем таймер
  }

  startTimer() {
    if (this.timer) {
      clearInterval(this.timer); // Очищаем предыдущий таймер
    }

    this.timer = setInterval(() => {
      console.log(this.currentSymbol.textContent);
      if (this.timerLimit > 0) {
        this.timerLimit--; // Уменьшаем лимит времени
      } else {
        clearInterval(this.timer); // Останавливаем таймер
        this.fail(); // Вызываем метод fail при истечении времени
      }
    }, 1000); // Интервал в 1 секунду
  }

  getWord() {
    const words = [
        'bob',
        'awesome',
        'netology',
        'hello',
        'kitty',
        'rock',
        'youtube',
        'popcorn',
        'cinema',
        'love',
        'javascript'
      ],
      index = Math.floor(Math.random() * words.length);

    return words[index];
  }

  renderWord(word) {
    const html = [...word]
      .map(
        (s, i) =>
          `<span class="symbol ${i === 0 ? 'symbol_current': ''}">${s}</span>`
      )
      .join('');
    this.wordElement.innerHTML = html;

    this.currentSymbol = this.wordElement.querySelector('.symbol_current');
  }
}

new Game(document.getElementById('game'))

