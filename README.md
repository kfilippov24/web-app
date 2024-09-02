###Python Bootstrap Flask SQLite
### Убедитесь, что `.env` файл содержит валидные значения

# Установка Poetry
```bash
pip install poetry
```

# Установка зависимостей проекта (создание виртуального окружения)
```bash
poetry install --no-root
```

# Запуск проекта
```bash
poetry run python src/__main__.py
```

# Корневая директория
- `poetry.lock` - библиотеки, которые будут установлены в проект (`poetry add new_library`)
- `pyproject.toml` - конфиг проекта (название, описание, зависимости и т.д.)

### Директория `src`
- `callbacks` - колбэк хендлеры
- `handlers` - месадж хендлеры
- `filters` - кастомные фильтры
- `keyboards` - клавиатуры (inline, factory, reply, builders)
- `states` - стейты
- `middlewares` - мидлвари

- `__main__.py` - основной файл, который отвечает за запуск бота
- `config_reader.py` - осуществляет подгрузку переменных из `.env` файла

