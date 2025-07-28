# 📦 E‑Commerce API

🚧 **This project is still under active development.** New features, improvements, and documentation updates are being added regularly.

A **Django REST Framework–based API** for an e‑commerce platform. It provides endpoints for managing products, handling store operations, and supports Docker for easy deployment.

---

## 🚀 Features

✅ Manage products (CRUD)
✅ Store module for handling orders/customers (extendable)
✅ Built with **Django REST Framework**
✅ Ready for **Docker & Docker Compose** deployment
✅ Scalable project structure

---

## 🛠 Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL (or configured DB in settings)
* **Deployment:** Docker & Docker Compose
* **Auth:** (Planned – JWT authentication)

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nikanmafakheri/E-CommerceAPI.git
cd E-CommerceAPI
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

---

## 🐳 Running with Docker

```bash
docker-compose up --build
```

---

## 📡 API Endpoints

| Method | Endpoint          | Description          |
| ------ | ----------------- | -------------------- |
| GET    | `/products/`      | List all products    |
| POST   | `/products/`      | Create a new product |
| GET    | `/products/<id>/` | Retrieve a product   |
| PUT    | `/products/<id>/` | Update a product     |
| DELETE | `/products/<id>/` | Delete a product     |

(More endpoints will be added as the project grows.)

---

## 🔮 Roadmap / Future Improvements

* 🔐 JWT authentication
* 🛒 Cart & checkout system
* 📄 API documentation with Swagger/ReDoc
* 📦 Advanced store/order features

---

## 🤝 Contributing

Since this project is **still developing**, feel free to fork it and open pull requests for new features or improvements.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Nikan Mafakheri**
🔗 [GitHub](https://github.com/nikanmafakheri)
