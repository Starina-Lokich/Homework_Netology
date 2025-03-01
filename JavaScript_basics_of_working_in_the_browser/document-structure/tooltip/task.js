document.addEventListener("DOMContentLoaded", () => {
    const tooltips = document.querySelectorAll(".has-tooltip");
    let activeTooltip = null;
  
    tooltips.forEach(tooltip => {
      tooltip.addEventListener("click", (event) => {
        event.preventDefault();
  
        // Если активная подсказка уже существует и она для этого элемента, удаляем её
        if (activeTooltip && activeTooltip.dataset.tooltipFor === tooltip.innerText) {
          activeTooltip.remove();
          activeTooltip = null;
          return;
        }
  
        // Удаляем предыдущую подсказку, если она есть
        if (activeTooltip) {
          activeTooltip.remove();
        }
  
        // Создаем новую подсказку
        const title = tooltip.getAttribute("title");
        const position = tooltip.getAttribute("data-position") || "bottom";
  
        const tooltipElement = document.createElement("div");
        tooltipElement.classList.add("tooltip", "tooltip_active");
        tooltipElement.innerText = title;
        tooltipElement.dataset.tooltipFor = tooltip.innerText; // Связываем подсказку с элементом
        document.body.appendChild(tooltipElement);
  
        // Позиционируем подсказку
        const rect = tooltip.getBoundingClientRect();
        const { width, height } = tooltipElement.getBoundingClientRect();
  
        let top, left;
        const offset = 5; // Отступ между подсказкой и элементом
  
        switch (position) {
          case "top":
            top = rect.top - height - offset;
            left = rect.left;
            break;
          case "right":
            top = rect.top;
            left = rect.right + offset;
            break;
          case "left":
            top = rect.top;
            left = rect.left - width - offset;
            break;
          case "bottom":
          default:
            top = rect.bottom + offset;
            left = rect.left;
            break;
        }
  
        // Устанавливаем позицию подсказки
        tooltipElement.style.top = `${top}px`;
        tooltipElement.style.left = `${left}px`;
  
        // Сохраняем текущую подсказку
        activeTooltip = tooltipElement;
      });
    });
  
    // Закрываем подсказку при клике вне элемента
    document.addEventListener("click", (event) => {
      if (activeTooltip && !event.target.classList.contains("has-tooltip")) {
        activeTooltip.remove();
        activeTooltip = null;
      }
    });
  });