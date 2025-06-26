<h1 align="center">Parser-Log</h1>

## Это инструмент для парсинга логов в формате .log

Как запустить:

## 1. скачайте репозиторий

```bash
git clone https://github.com/SoundRush/parser-log
```

<h2 align='center'>2. Установите Python 3.12.9 или другую</h2>

```Links:
https://www.python.org/downloads/
```

<h2 align='center'>3. Замените путь к логов в файле errors.py</h2>

### Следующие пути:

* all_logs/server_errors.log

### На что то другое, например:

* erors/erorrs.log
---


<h2 align='center'>4. Запустите скрипт в консоле</h2>

```bash
python errors.py
```

<h2 align='center'>5. Когда скрипт будет запущен вы увидите в консоли такое</h2>

```bash
Введи коды статусов (например: 500-504 404 200): Traceback (most recent call last):
```
