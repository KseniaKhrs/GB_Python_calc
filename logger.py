# Модуль для записи резуьтатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('calc_history.txt', 'a', encoding='utf-8') as h:
            h.write(f'{expr} --> {result}\n')

def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('calc_history.txt', 'r', encoding='utf-8') as h:
        text = h.read()
    return text
