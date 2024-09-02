
<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>
<div id="badges" align="center">
  <a href="your-linkedin-URL">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="your-youtube-URL">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  <a href="your-twitter-URL">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
</div>

Убедитесь, что `.env` файл содержит валидные значения
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

