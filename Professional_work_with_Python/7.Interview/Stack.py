class Stack:
    def __init__(self):
        self.data = []
    
    def isEmpty(self) -> bool:
        '''
        Проверка стека на пустоту. Метод возвращает True или False
        '''
        return len(self.data) == 0

    def push(self, item):
        '''
        Добавляет новый элемент на вершину стека. Метод ничего не возвращает
        '''
        self.data.append(item)

    def pop(self) -> any:
        '''
        Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        '''
        if self.isEmpty():
            return None
        return self.data.pop()

    def peek(self) -> any:
        '''
        Возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        '''
        if self.isEmpty():
            return None
        return self.data[-1]
    
    def size(self) -> int:
        '''
        Возвращает количество элементов в стеке
        '''
        return len(self.data)

def check_brackets(s):
    stack = Stack()
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_pairs.values():
            stack.push(char)
        elif char in bracket_pairs.keys():
            if stack.isEmpty() or stack.peek() != bracket_pairs[char]:
                return "Несбалансированно"
            stack.pop()

    return "Сбалансированно" if stack.isEmpty() else "Несбалансированно"


# Тесты
print(check_brackets("(((([{}]))))"))  # Сбалансированно
print(check_brackets("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(check_brackets("{{[()]}}"))  # Сбалансированно
print(check_brackets("}{"))  # Несбалансированно
print(check_brackets("{{[(])]}}"))  # Несбалансированно
print(check_brackets("[[{())}]"))  # Несбалансированно