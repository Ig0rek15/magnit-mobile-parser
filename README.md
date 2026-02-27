# Magnit Mobile API Parser

Парсер мобильного API приложения «Магнит».
API был проанализирован через перехват трафика мобильного приложения.
Эндпоинты и примеры запросов/ответов получил с помощью Burp Suite.
Спарсил данные для городов Москва и  Санкт-Петербург и сохранил в один файл, можно посмотреть в папке results/


Основные эндпоинты:

- `POST /v2/goods/search` — получение списка товаров категории
- `GET /v2/goods/{id}/stores/{storeCode}` — получение информации о конекретном товаре

---

## Установка

```bash
git clone https://github.com/Ig0rek15/magnit-mobile-parser
cd magnit-mobile-parser
python -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск
```bash
python main.py
```
---

