# ShopSpot Showcase - Setup Guide

This guide will help you set up both the backend and frontend of the ShopSpot Showcase application.

## Project Structure

```
shopfiy/
├── backend/          # Django REST API backend
├── shopspot-showcase/ # React + TypeScript frontend
└── SETUP.md          # This file
```

## Backend Setup (Django)

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
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

4. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Seed the database with sample products:**
   ```bash
   python manage.py seed_products
   ```

6. **Start the Django server:**
   ```bash
   python manage.py runserver
   ```

   The backend will run on `http://localhost:8000`

## Frontend Setup (React + TypeScript)

1. **Navigate to frontend directory:**
   ```bash
   cd shopspot-showcase
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Create environment file (optional):**
   Create a `.env` file in the `shopspot-showcase` directory:
   ```env
   VITE_API_BASE_URL=https://fullstack-dealshop00.onrender.com/
   ```

   If you don't create this file, it will default to `https://fullstack-dealshop00.onrender.com/`

4. **Start the development server:**
   ```bash
   npm run dev
   ```

   The frontend will run on `http://localhost:8080`

## Running the Application

1. **Start the backend server:**
   - Open a terminal and run the Django server (see Backend Setup step 6)

2. **Start the frontend server:**
   - Open another terminal and run the React dev server (see Frontend Setup step 4)

3. **Access the application:**
   - Open your browser and navigate to `http://localhost:8080`

## Features

- ✅ Product listing from multiple stores (Flipkart, Myntra, Meesho)
- ✅ Search functionality
- ✅ Store filtering
- ✅ RESTful API with Django REST Framework
- ✅ CORS enabled for frontend-backend communication
- ✅ SQLite database (can be changed to PostgreSQL/MySQL for production)

## API Endpoints

- `GET /api/products/` - Get all products
- `GET /api/products/{id}/` - Get a specific product
- `GET /api/products/by_store/?store=Flipkart` - Get products by store
- `GET /api/products/search/?q=shoes` - Search products

## Troubleshooting

### Backend Issues

- **Port 8000 already in use:** Change the port by running `python manage.py runserver 8001`
- **Migration errors:** Delete `db.sqlite3` and run migrations again
- **CORS errors:** Make sure `django-cors-headers` is installed and configured in `settings.py`

### Frontend Issues

- **Cannot connect to backend:** Ensure the backend is running and check the `VITE_API_BASE_URL` environment variable
- **Port 8080 already in use:** The Vite server will automatically use the next available port

## Production Deployment

For production deployment:

1. **Backend:**
   - Change `DEBUG = False` in `settings.py`
   - Use a production database (PostgreSQL recommended)
   - Set up proper CORS allowed origins
   - Use environment variables for sensitive settings

2. **Frontend:**
   - Build the production bundle: `npm run build`
   - Serve the `dist` folder using a web server (Nginx, Apache, etc.)
   - Set up proper environment variables

## License

This project is open source and available under the MIT License.

