# Космический Flickr

Консольная утилита, которая загружает фото от [SpaceX](https://www.spacex.com/) и [Hubble](https://hubblesite.org/) на [Flickr](https://www.flickr.com/).

### Зарегистрировать приложение на Flickr
Перед тем, как постить фотографии в Flickr, нужно [создать приложение](https://www.flickr.com/services/apps/create/) и получить `api-key` и `api-secret`.

### Настройка окружения
`api-key` и `api-secret` записать в переменные окружения `FLICKR_API_KEY` и `FLICKR_API_SECRET` соответственно.

### Пример `.env` файла:
```
FLICKR_API_KEY=<api-key>
FLICKR_API_SECRET=<api-secret>
```

### Установка необходимых библиотек
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
$ pip install -r requirements.txt
```

### Запуск
```
$ python3 main.py
```
