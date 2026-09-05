🏍️ Manage Motor — Motorcycle E-Commerce Platform

A web-based motorcycle e-commerce platform built with Django. The application provides customers with a complete shopping flow, including product browsing, category filtering, search, authentication, shopping cart management, checkout, order tracking, and product reviews.

The project was developed to practice building a full-stack web application using Django's MVT architecture, Django ORM, authentication system, database transactions, server-side rendering, and asynchronous cart updates with JavaScript.

✨ Features
👤 User Authentication
User registration
User login/logout
Session-based authentication using Django Authentication
User profile page
Authentication-aware shopping cart
🏍️ Product Catalog
Browse motorcycle products
Browse products by category
Product detail page
Product images
Original price and selling price
Product stock management
Product descriptions
Latest products section
Best-selling products section
🔎 Product Search
Search products by name
Paginated search results
🛒 Shopping Cart
Add products to cart
Increase/decrease product quantity
Automatically remove products when quantity reaches zero
Display total cart items
Calculate cart total
Authentication-based cart management

Cart updates are handled asynchronously through a JavaScript request to the Django backend.

📦 Checkout & Order Processing

The checkout process includes:

Stock availability validation
Order creation
Order detail creation/update
Product stock deduction
Database transaction handling with transaction.atomic()

This helps keep order creation and inventory updates consistent.

⭐ Product Reviews

Customers can leave:

Rating
Comment

The product detail page also calculates the average product rating.

📊 Product Ranking

The homepage provides:

Latest products
Best-selling products

Best-selling products are determined based on the number of associated order details.

📄 Pagination

Product listings and search results use Django's Paginator to improve navigation and page performance.

🛠️ Tech Stack
Category	Technology
Backend	Python, Django 5.0.4
Frontend	HTML5, CSS3, JavaScript
UI	Bootstrap, Boxicons
Template Engine	Django Templates
Database	SQLite
ORM	Django ORM
Authentication	Django Authentication Framework
Static Files	Django Static Files
Image Handling	Django ImageField
CI/CD	GitHub Actions
🏗️ Architecture

The application follows Django's Model–View–Template (MVT) architecture.

┌─────────────────────┐
│       Browser       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Django URLs      │
│     app/urls.py     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│       Views         │
│     app/views.py    │
└──────────┬──────────┘
           │
      ┌────┴─────┐
      ▼          ▼
┌───────────┐ ┌──────────────┐
│   Models  │ │   Templates  │
│ models.py │ │ HTML / CSS   │
└─────┬─────┘ │ JavaScript   │
      │       └──────────────┘
      ▼
┌─────────────────────┐
│       SQLite        │
│     db.sqlite3      │
└─────────────────────┘
🗃️ Data Model

The main entities are:

User
 │
 ├───────────────┐
 │               │
 ▼               ▼
Order        OrderDetail
 │               │
 │               ├──────────► Product
 │               │               │
 │               │               ▼
 │               │            Category
 │               │
 │               ├── rate
 │               └── comment
 │
 └── account
Main Models
Category

Represents motorcycle product categories.

Category
├── name
├── slug
├── description
├── image
├── status
└── created_at
Product

Represents products available in the store.

Product
├── category
├── name
├── slug
├── small_description
├── description
├── original_price
├── selling_price
├── image
├── qty
├── status
└── created_at
Order

Represents a customer's shopping cart or completed order.

Order
├── account
├── status
└── created_at
OrderDetail

Represents individual products inside an order.

OrderDetail
├── account
├── product
├── order
├── selling_price
├── quantity
├── status
├── rate
├── comment
└── created_at
🔄 Main Business Flows
Shopping Flow
Browse Products
       │
       ▼
Select Product
       │
       ▼
Product Detail
       │
       ▼
Add to Cart
       │
       ▼
Update Cart Quantity
       │
       ▼
Checkout
       │
       ▼
Check Stock
       │
       ├──── Insufficient Stock
       │            │
       │            ▼
       │       Show Error
       │
       ▼
Create Order
       │
       ▼
Create Order Details
       │
       ▼
Decrease Product Stock
       │
       ▼
Order Successful
Authentication Flow
Register
   │
   ▼
Django UserCreationForm
   │
   ▼
Create User
   │
   ▼
Login
   │
   ▼
Django Authentication
   │
   ▼
Authenticated Session
📁 Project Structure
Manage_Motor/
│
├── .github/
│   └── workflows/
│       └── django.yml
│
├── WebBanHang/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app/
│   ├── migrations/
│   ├── templates/
│   │   └── app/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── products.html
│   │       ├── product_detail.html
│   │       ├── search.html
│   │       ├── cart.html
│   │       ├── cart_status.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── user_profile.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── manage.py
├── db.sqlite3
└── README.md
🚀 Getting Started
1. Prerequisites

Make sure you have installed:

Python 3.10+
pip
Git

The project uses Django 5.0.4. A modern supported Python version is recommended for local development.

2. Clone the Repository
git clone https://github.com/Felix-Phong/Manage_Motor.git

cd Manage_Motor
3. Create a Virtual Environment
Windows
python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1
macOS / Linux
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies

If a requirements.txt file is available:

pip install -r requirements.txt

Otherwise, install Django and the required image package:

pip install django==5.0.4
pip install Pillow
5. Apply Database Migrations
python manage.py migrate
6. Create an Admin Account
python manage.py createsuperuser

Follow the prompts to create the administrator account.

7. Run the Development Server
python manage.py runserver

Open:

http://127.0.0.1:8000/
🔐 Django Admin

The project uses Django's built-in admin interface.

After creating a superuser, access:

http://127.0.0.1:8000/admin/

The admin interface can be used to manage application data registered with Django Admin.

🔌 Main Routes
Method	Endpoint	Description
GET	/	Homepage
GET	/products/	Product listing
GET	/products/<slug>/	Products by category
GET	/product/<slug>/	Product details
POST	/search/	Search products
GET	/cart/	Shopping cart
GET	/cart_status/	Order status
POST	/update_order/	Update cart
POST	/checkout/	Checkout
GET/POST	/login/	User login
GET/POST	/register/	User registration
GET	/logout/	User logout
GET	/user_profile/	User profile
💡 Technical Highlights

This project demonstrates practical experience with:

Django MVT architecture
Django ORM
Relational data modeling
Foreign key relationships
Django Authentication
Server-side rendering
Form validation
Database transactions
Inventory management
Shopping cart implementation
Product search
Pagination
Aggregation queries
Asynchronous JavaScript requests
Static and media file handling
GitHub Actions

One notable implementation is the checkout transaction:

with transaction.atomic():
    # create order
    # update order details
    # decrease product stock

Using a database transaction helps prevent partially completed checkout operations.

🧪 Testing

Run Django's test suite with:

python manage.py test

The repository also contains a GitHub Actions workflow intended to run automated tests on pushes and pull requests to the master branch.

🔮 Future Improvements

Potential improvements include:

Add requirements.txt

Add automated test coverage

Improve product filtering and sorting

Add payment gateway integration

Add order status management for administrators

Add customer order history

Improve inventory validation

Add REST API using Django REST Framework

Add environment-based configuration

Move secrets to environment variables

Use PostgreSQL for production

Add Docker support

Improve CI/CD pipeline

Add production deployment configuration

Remove committed virtual environment and cache files

⚠️ Development Notes

This repository is primarily a learning/portfolio project and currently uses SQLite and Django development settings.

For production deployment, the following should be improved:

Disable DEBUG
Move SECRET_KEY to environment variables
Configure ALLOWED_HOSTS
Use a production database such as PostgreSQL
Configure secure static/media file serving
Remove local virtual environment files from Git
Add proper dependency locking
Configure production WSGI/ASGI deployment
👨‍💻 Author

Felix Phong

GitHub: Felix-Phong

📄 License

This project is intended for educational and portfolio purposes.
