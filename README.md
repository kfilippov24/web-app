![alt text](https://static11.tgcnt.ru/posts/_0/4f/4fd0b776ada0484854d605d25bb24840.jpg)
![alt text](https://avatars.mds.yandex.net/i?id=4756b9a7ee465e4901cda35f9ec69b1cc743f0cb-5672525-images-thumbs&n=13)
![alt text](https://avatars.mds.yandex.net/i?id=272998ada057f6f0dab7da6b2fe35316ac63ff5b-12536664-images-thumbs&n=13)
![alt text](https://avatars.mds.yandex.net/i?id=c9ef20877cdf36947c177e3ed59d4b10b323826d303fef76-12414924-images-thumbs&n=13)
<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>
<div id="badges">
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

