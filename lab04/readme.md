# Лабораторная работа №4  
**Jenkins + SSH Agent + CI/CD для PHP**

**Выполнил:** Курилов Анатолий 

### Что сделано
1. Поднят Jenkins Controller в Docker Compose  
2. Создан SSH-агент на Alpine с PHP 8.2 + Composer  
3. Автоматическое подключение агента по SSH  
4. Настроен Declarative Pipeline:  
   → клонирование репозитория  
   → `composer install`  
   → запуск PHPUnit с `--testdox`  
5. Все тесты проходят успешно

### Структура папки lab04/

    lab04/
    ├── docker-compose.yml
    ├── Dockerfile
    ├── .env
    ├── Jenkinsfile
    └── secrets/


### Ответы на вопросы

**Преимущества Jenkins**  
• Бесплатный, >1800 плагинов  
• Гибкие пайплайны  
• Легко масштабируется (SSH, Docker, K8s)  
• Интеграция со всем стеком DevOps

**Другие типы агентов**  
• JNLP • SSH • Docker • Kubernetes • Windows

**Проблемы → Решения**  
• Агент не подключался → Non verifying Host Key  
• Нет Composer → добавил в Dockerfile  
• Permission denied → ключ без passphrase + точный pubkey в .env  
• PHPUnit падал → добавил php-xml, php-dom и др.

### Доказательства
1. Разблокировка Jenkins  
2. Плагины  
3. SSH-ключ  
4. Узел ssh-agent1  
5. Агент онлайн  
6. Пайплайн  
7. Успешный билд  
8. Красивый вывод тестов

**Запуск одной командой:**  
```bash
cd lab04 && docker compose up -d --build