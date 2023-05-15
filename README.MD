# Создание таймлапсов с помощью камеры RaspberryPi
### Описание
Проект позволяет делать снимки на камеру RaspberryPi с определенным интервалом, собирать тамйлапс и отправлять получившееся видео в Telegram.

### Технологии
- Python
- PiCamera
- ffmpeg
- Telegram


### Как запустить

1. Склонируйте репозиторий
```commandline
git@github.com:podlev/timelapse_project.git
```
2. Создайте и активируйте виртаульное окружение
```commandline
python -m venv venv
source venv/Scripts/activate
```  
3. Установите зависимости
```commandline
pip install -r requirements.txt
```
4. Включите поддержку камеры `Interface options -> Legacy camera support -> Yes`: 
```commandline
sudo raspi-config
```

5. Переиментуйте `.env.example` в `.env` и укажите `TELEGRAM_USER_ID` - кому отправлять таймлапсы и `TELEGRAM_BOT_TOKEN`.

### Настройки
- [ ] Дописать

### Результаты
- [ ] Дописать

### Пример
- [ ] Дописать

### Автор
Telegram: [Лев Подъельников](https://t.me/podlev)