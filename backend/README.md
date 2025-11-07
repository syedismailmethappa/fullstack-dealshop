# Django Backend Setup

This is the Django REST API backend for the ShopSpot Showcase application.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment (if not already done):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Seed the database with sample products:**
   ```bash
   python manage.py seed_products
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

The backend API will be available at `http://localhost:8000`

## API Endpoints

- `GET /api/products/` - List all products
- `GET /api/products/{id}/` - Get a specific product
- `GET /api/products/by_store/?store=Flipkart` - Get products by store
- `GET /api/products/search/?q=shoes` - Search products
- `POST /api/products/` - Create a new product (requires authentication)
- `PUT /api/products/{id}/` - Update a product (requires authentication)
- `DELETE /api/products/{id}/` - Delete a product (requires authentication)

## Admin Panel

Access the Django admin panel at `http://localhost:8000/admin/` to manage products.

## Database

The default database is SQLite (`db.sqlite3`). For production, you should configure a PostgreSQL or MySQL database.

