# Django Backend Setup

This is the Django REST API backend for the ShopSpot Showcase application.

## Local Development

1. **Navigate to the backend directory:**
   ```powershell
   cd backend
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```powershell
   python manage.py migrate
   ```

5. **Start the development server (Windows):**
   ```powershell
   # Option 1: Django development server
   python manage.py runserver 0.0.0.0:8000

   # Option 2: Uvicorn (recommended for ASGI)
   python -m uvicorn backend.asgi:application --host 0.0.0.0 --port 8000 --reload
   ```

## Production Deployment (Render)

1. **Environment Variables Required:**
   ```
   DATABASE_URL=your-postgres-url
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_ALLOWED_HOSTNAME=your-app-name.onrender.com
   RENDER_EXTERNAL_HOSTNAME=your-app-name.onrender.com
   DJANGO_SUPERUSER_PASSWORD=your-superuser-password
   ```
   
   **Note:** The `DJANGO_SUPERUSER_PASSWORD` environment variable is used to automatically create a superuser during deployment with:
   - Username: `syed`
   - Email: `syedmethappa0987@gmail.com`
   
   If this variable is not set, the superuser creation will be skipped (you can create it manually later).

2. **Build Command:**
   ```bash
   ./build.sh
   ```

3. **Start Command:**
   ```bash
   gunicorn backend.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --workers 2 --timeout 30
   ```

## API Endpoints

- `GET /api/products/` - List all products
- `GET /api/products/{id}/` - Get specific product
- `GET /api/products/by_store/?store=Flipkart` - Get products by store
- `GET /api/products/search/?q=shoes` - Search products

## Files for Deployment

- `Procfile`: Defines process types and commands
- `runtime.txt`: Specifies Python version
- `requirements.txt`: Lists all dependencies
- `build.sh`: Build script for collecting static files and migrations

## Database

Production uses PostgreSQL via DATABASE_URL environment variable.
Development uses SQLite by default.

