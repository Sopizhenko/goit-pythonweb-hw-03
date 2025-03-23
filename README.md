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
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── error.html
│   ├── index.html
│   ├── logo.png
│   ├── main.py
│   ├── message.html
│   ├── read.html
│   ├── README.md
│   ├── requirements.txt
│   ├── style.css
│   ├── storage/
│   │   ├── data.json
```
