document.addEventListener("DOMContentLoaded", () => {
    const tasksForm = document.getElementById("tasks__form");
    const taskInput = document.getElementById("task__input");
    const tasksList = document.getElementById("tasks__list");
  
    // Загрузка задач из localStorage
    function loadTasks() {
      const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
      tasks.forEach(task => addTask(task));
    }
  
    // Сохранение задач в localStorage
    function saveTasks() {
      const tasks = Array.from(tasksList.querySelectorAll(".task__title")).map(task => task.textContent);
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }
  
    // Добавление задачи
    function addTask(taskText) {
      const taskElement = document.createElement("div");
      taskElement.classList.add("task");
  
      const taskTitle = document.createElement("div");
      taskTitle.classList.add("task__title");
      taskTitle.textContent = taskText;
  
      const taskRemove = document.createElement("a");
      taskRemove.classList.add("task__remove");
      taskRemove.innerHTML = "&times;";
      taskRemove.href = "#";
  
      taskElement.appendChild(taskTitle);
      taskElement.appendChild(taskRemove);
      tasksList.appendChild(taskElement);
  
      // Обработчик для удаления задачи
      taskRemove.addEventListener("click", (event) => {
        event.preventDefault();
        taskElement.remove();
        saveTasks();
      });
    }
  
    // Обработчик отправки формы
    tasksForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const taskText = taskInput.value.trim();
      if (taskText) {
        addTask(taskText);
        taskInput.value = "";
        saveTasks();
      }
    });
  
    // Загрузка задач при старте
    loadTasks();
  });