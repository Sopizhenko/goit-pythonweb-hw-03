# Python Web Server з Docker

## Огляд
Це веб-сервер на Python у контейнері Docker із постійним сховищем для збереження даних.

## Використання

### Запуск через Docker Compose
```sh
docker-compose -f app/docker-compose.yml up -d
```

## Доступ
Застосунок доступний за адресою:
```
http://localhost:3000
```

## Структура проєкту
```
├── app/
│   ├── images/
|   |   ├── logo.png
│   ├── storage/
│   │   ├── data.json
|   ├── templates/
│   │   ├── error.html
│   │   ├── index.html
|   |   ├── message.html
|   |   ├── read.html
|   ├── styles/
|   |   ├── style.css
│   ├── main.py
│   ├── README.md
│   ├── requirements.txt
│   ├── docker-compose.yml
│   ├── Dockerfile
