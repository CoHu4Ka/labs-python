# lab02/currency_exchange_rate.py

import requests
import json
import os
import sys
import logging
import re
from datetime import datetime

# Настройка логирования
logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    if len(sys.argv) != 4:
        print("Использование: python currency_exchange_rate.py <from_currency> <to_currency> <date>")
        print("Пример: python currency_exchange_rate.py USD EUR 2025-01-01")
        sys.exit(1)

    from_curr = sys.argv[1].upper()
    to_curr = sys.argv[2].upper()
    date_str = sys.argv[3]

    # Валидация формата даты (YYYY-MM-DD)
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        error_msg = f"Неверный формат даты: {date_str}. Ожидается YYYY-MM-DD."
        print(error_msg)
        logging.error(error_msg)
        sys.exit(1)

    # Проверка, что дата в диапазоне данных (2025-01-01 to 2025-09-15)
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        start_date = datetime(2025, 1, 1)
        end_date = datetime(2025, 9, 15)
        if not (start_date <= date_obj <= end_date):
            error_msg = f"Дата {date_str} вне диапазона доступных данных (2025-01-01 to 2025-09-15)."
            print(error_msg)
            logging.error(error_msg)
            sys.exit(1)
    except ValueError:
        error_msg = f"Неверная дата: {date_str}."
        print(error_msg)
        logging.error(error_msg)
        sys.exit(1)

    url = "http://localhost:8080/"
    params = {"from": from_curr, "to": to_curr, "date": date_str}
    data = {"key": "EXAMPLE_API_KEY"}  # API ключ из sample.env

    try:
        response = requests.post(url, params=params, data=data)
        response.raise_for_status()  # Вызвать исключение при HTTP ошибке
        result = response.json()

        if result.get("error"):
            error_msg = f"Ошибка API: {result['error']}"
            print(error_msg)
            logging.error(error_msg)
            sys.exit(1)

        # Создание директории data, если не существует
        os.makedirs('data', exist_ok=True)

        # Формирование имени файла
        filename = f"data/{from_curr}_{to_curr}_{date_str}.json"

        # Сохранение данных в JSON файл
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result['data'], f, ensure_ascii=False, indent=4)

        print(f"Данные успешно сохранены в {filename}")

    except requests.exceptions.RequestException as e:
        error_msg = f"Ошибка запроса: {str(e)}"
        print(error_msg)
        logging.error(error_msg)
        sys.exit(1)
    except json.JSONDecodeError:
        error_msg = "Ошибка разбора JSON ответа."
        print(error_msg)
        logging.error(error_msg)
        sys.exit(1)
    except Exception as e:
        error_msg = f"Неизвестная ошибка: {str(e)}"
        print(error_msg)
        logging.error(error_msg)
        sys.exit(1)

if __name__ == "__main__":
    main()