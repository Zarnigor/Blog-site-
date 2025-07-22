# 📝 Full-Stack Blog Platform — Next.js + Django REST API

A modern full-stack blog platform built with **Next.js (App Router)** for the frontend and **Django REST Framework** for the backend. This project provides a fast, responsive, and extensible structure for publishing and managing blog posts with real-world features like token-based authentication, Markdown support, and deployment readiness.

## 🚀 Features
- ✨ Responsive and minimal blog UI (Next.js + Tailwind CSS)
- 🧠 TypeScript + MDX + App Router (Next.js 13+ architecture)
- 🔐 Django REST API with JWT Authentication
- 🛠️ CRUD operations for blog posts
- 👤 User registration and token-based login
- 🔄 Token refresh system
- 🌍 Deployable on Vercel (frontend) 

## 📁 Project Structure
```bash
Blog-site-/
├── backend/            # Django REST Framework API
└── README.md           # Project documentation
```

## ⚙️ Getting Started

### Clone the repository
```bash
git clone https://github.com/Zarnigor/Blog-site-.git
cd Blog-site-
```

### 🔧 Backend Setup (Django REST API)
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory:
```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Then run migrations and start the development server:
```bash
python manage.py migrate
python manage.py runserver
```

API will be available at: http://127.0.0.1:8000/api/

### 💻 Frontend Setup (Next.js App)
```bash
cd ../frontend
npm install
npm run dev
```

Frontend will be available at: http://localhost:3000

## 📬 API Endpoints
| Endpoint               | Method | Description              |
|------------------------|--------|--------------------------|
| soon                   | GET    | List all blog posts      |


Send authenticated requests with:
```makefile
Authorization: Bearer <your_token>
```

## 🔗 Useful Links
- Frontend Template: [timlrx/tailwind-nextjs-starter-blog](https://github.com/timlrx/tailwind-nextjs-starter-blog)
- Repository: [github.com/Zarnigor/Blog-site-](https://github.com/Zarnigor/Blog-site-)

## 📄 License
MIT License © [Zarnigor](https://github.com/Zarnigor)
