
# Django Store 🛒

A full-featured e-commerce application built with Django. This project enables users to browse products, manage orders, and includes an admin panel for store management.

## 🚀 Features

- **Product Browsing**: View and search available products.
- **Order Management**: Integrated ordering and checkout.
- **Admin Panel**: Control products, orders, and user accounts from a single dashboard.

## ⚙️ Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd django_store
   ```

2. **Create Virtual Environment and Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## 📂 Project Structure

- `core/`, `order/`, `store/`: Django apps for various features of the store.
- `media/`, `templates/`: Directories for images and HTML templates.
- `db.sqlite3`: Database file (for development/testing).

## 🛠 Usage

- **Access the Application**: Visit `http://127.0.0.1:8000/` to explore the store.
- **Admin Dashboard**: Accessible at `http://127.0.0.1:8000/admin/`.

## 📝 License

This project is licensed under the **MIT License**.
