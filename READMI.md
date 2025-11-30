

# Инструкция по запуску проекта

Для одновременной работы клиента и сервера откройте два терминала.

### Терминал 1: Frontend

Перейдите в папку фронтенда, установите зависимости и запустите режим разработки:

```bash
cd frontend
npm i
npm run dev
```

### Терминал 2: Backend

Перейдите в папку бэкенда, создайте/активируйте виртуальное окружение, установите зависимости и запустите сервер:

```powershell
cd backend
python -m venv .venv
.venv/Scripts/Activate.ps1
pip install -r requirements.txt
python manage.py runserver
```