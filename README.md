# LuxeJewels & Sarees — Premium Indian E-Commerce Platform

A production-oriented modular monolithic Django e-commerce platform specializing in Gold, Silver, and Artificial Jewellery, alongside exquisite Silk, Cotton, and Designer Sarees for the Indian market.

## Features
- **Bilingual**: Full English and Telugu (తెలుగు) support with Django i18n.
- **Luxury Aesthetic**: Ivory, Maroon, and Gold luxury storefront designed with Bootstrap 5.
- **Robust Pricing**: Dynamic gold and silver weight-based pricing alongside fixed pricing.
- **Secure Payments**: PhonePe payment gateway integration ready.
- **PostgreSQL & Neon**: Optimized for Neon PostgreSQL with full-text search & trigram matching.

---

## Local Installation & Running on Windows 11

### 1. Prerequisites
- Python 3.11+ installed and added to PATH.
- PostgreSQL / Neon DB instance.
- Git.

### 2. Clone and Setup Virtual Environment
```bash
git clone https://github.com/vijaysmart043/Fashion-Ecommerce.git
cd Fashion-Ecommerce
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your Neon PostgreSQL database URL and other credentials:
```bash
copy .env.example .env
```

### 5. Run Database Migrations
```bash
python manage.py makemigrations accounts core catalog jewellery sarees inventory pricing cart checkout orders payments shipping promotions reviews wishlist notifications dashboard reports cms search
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```
Access the storefront at `http://127.0.0.1:8000/` and custom admin panel at `http://127.0.0.1:8000/admin-panel/`.

### 8. Run Tests
```bash
python manage.py test
```
