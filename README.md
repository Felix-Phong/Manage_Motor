# 🏍️ Manage Motor — Motorcycle E-Commerce Website

A full-stack motorcycle e-commerce web application built with **Python and Django**.

The project provides a complete online shopping flow including product browsing, search, user authentication, shopping cart, checkout, order processing, and product reviews.

---

## 📌 Overview

**Manage Motor** is a motorcycle online shopping platform developed using Django's **Model–View–Template (MVT)** architecture.

The system allows customers to:

- Browse motorcycle products by category
- Search for motorcycles
- View detailed product information
- Register and authenticate accounts
- Add products to a shopping cart
- Update product quantities
- Remove products from the cart
- Checkout and create orders
- Manage user profiles
- Rate and review products

The project was developed to practice:

- Django web development
- Database modeling
- Django ORM
- User authentication
- E-commerce business logic
- Shopping cart implementation
- Order processing
- Inventory management
- Database transaction handling

---

## ✨ Features

### 👤 User Authentication

- User registration
- User login/logout
- Django Authentication Framework
- User profile management
- Authentication-protected features

### 🏍️ Product Management

- Product listing
- Product categories
- Product detail pages
- Product images
- Product descriptions
- Original price
- Selling price
- Product stock management
- Product status management

### 🔎 Product Search

Users can search for motorcycles by product name.

Search results are displayed using pagination to improve usability when dealing with multiple products.

### 🛒 Shopping Cart

The shopping cart supports:

- Add product to cart
- Update product quantity
- Remove product from cart
- Calculate product quantities and prices
- Validate available stock

Cart quantity updates are handled asynchronously using JavaScript `fetch()` requests.

### 💳 Checkout & Order Processing

The checkout process:

1. Validates requested product quantities.
2. Checks available inventory.
3. Creates or updates the customer's order.
4. Creates order details.
5. Updates product stock.
6. Uses Django database transactions to maintain data consistency.

The checkout logic uses:

```python
with transaction.atomic():
```

This helps ensure that related database operations are executed safely as a single transaction.

### ⭐ Product Rating & Reviews

Customers can rate and comment on products.

The system stores:

- Rating
- Comment
- Product
- Customer
- Order
- Order detail

Product pages can calculate the average rating based on customer reviews.

### 📈 Product Discovery

The homepage provides product discovery sections such as:

- Latest products
- Best-selling products

### 📄 Pagination

Product listings and search results use Django's `Paginator` to split products across multiple pages.

---

# 🏗️ Architecture

The project follows the **Django MVT architecture**.

```text
                    ┌─────────────────────┐
                    │       Browser       │
                    │   HTML / CSS / JS   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Django URL     │
                    │       Routing       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        Views        │
                    │   Business Logic    │
                    └──────────┬──────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │      Models     │       │    Templates    │
        │   Django ORM    │       │  Django HTML    │
        └────────┬────────┘       └─────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │    SQLite DB    │
        └─────────────────┘
```

### Main Components

| Component | Responsibility |
|---|---|
| URL Routing | Maps HTTP requests to views |
| Views | Handles application and business logic |
| Models | Defines database structure |
| Templates | Renders HTML pages |
| Django ORM | Handles database operations |
| Authentication | Handles user authentication |
| Static Files | CSS, JavaScript, images and frontend assets |

---

# 🗄️ Database Design

The application uses Django ORM to model the main entities.

```text
Category
   │
   │ 1
   │
   │ N
   ▼
Product
   │
   │ 1
   │
   │ N
   ▼
OrderDetail
   ▲
   │
   │ N
   │
   │ 1
   │
Order
```

## Category

Stores motorcycle categories.

### Main Fields

- `name`
- `slug`
- `description`
- `image`
- `status`
- `created_at`

## Product

Stores motorcycle information.

### Main Fields

- `category`
- `name`
- `slug`
- `small_description`
- `description`
- `original_price`
- `selling_price`
- `image`
- `qty`
- `status`
- `created_at`

## Order

Represents a customer's shopping cart or order.

### Main Fields

- `account`
- `status`
- `created_at`

## OrderDetail

Stores individual products belonging to an order.

### Main Fields

- `account`
- `product`
- `order`
- `selling_price`
- `quantity`
- `status`
- `rate`
- `comment`
- `created_at`

---

# 🔄 Shopping Flow

```text
Customer
   │
   ▼
Browse Products
   │
   ▼
View Product Details
   │
   ▼
Add to Cart
   │
   ▼
Update Quantity
   │
   ▼
Validate Stock
   │
   ▼
Checkout
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
Order Completed
```

---

# 🔐 Authentication Flow

```text
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
authenticate()
   │
   ▼
login()
   │
   ▼
Authenticated Session
```

Logout is handled using Django's built-in authentication system.

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| **Python** | Backend programming language |
| **Django 5.0.4** | Web framework |
| **Django ORM** | Database access |
| **SQLite** | Development database |
| **HTML5** | Page structure |
| **CSS3** | Styling |
| **JavaScript** | Client-side interactions |
| **Bootstrap** | Responsive UI |
| **Boxicons** | Icons |
| **Django Templates** | Server-side rendering |
| **Git / GitHub** | Version control |
| **GitHub Actions** | CI / testing workflow |

---

# 📂 Project Structure

```text
Manage_Motor/
│
├── app/
│   ├── migrations/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── cart.html
│   │   ├── cart_status.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── product_detail.html
│   │   ├── products.html
│   │   ├── register.html
│   │   ├── search.html
│   │   ├── user.html
│   │   ├── user_profile.html
│   │   └── vote.html
│   │
│   ├── static/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── WebBanHang/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .github/
│   └── workflows/
│
├── manage.py
├── db.sqlite3
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have installed:

- Python 3.10+
- pip
- Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/Felix-Phong/Manage_Motor.git
```

```bash
cd Manage_Motor
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise:

```bash
pip install django==5.0.4
pip install Pillow
```

---

## 4. Run Database Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## 5. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the instructions shown in the terminal.

---

## 6. Start the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

# 🌐 Main Routes

| Route | Description |
|---|---|
| `/` | Homepage |
| `/products/` | Product listing |
| `/products/<slug>/` | Product details |
| `/product/<slug>/` | Product details |
| `/search/` | Search products |
| `/cart/` | Shopping cart |
| `/cart_status/` | Cart status |
| `/update_order/` | Update cart/order |
| `/checkout/` | Checkout |
| `/login/` | User login |
| `/register/` | User registration |
| `/logout/` | Logout |
| `/user_profile/` | User profile |

---

# 💡 Technical Highlights

## 1. Django ORM

Database operations are implemented using Django ORM.

Example:

```python
Product.objects.filter(
    name__contains=searched
)
```

This allows users to search for products by name.

---

## 2. Database Transactions

Checkout operations use Django's transaction management:

```python
with transaction.atomic():
```

This helps maintain consistency between:

- Order creation
- Order detail creation
- Product inventory updates

---

## 3. Stock Validation

Before completing an order, the system checks whether the requested quantity is available.

```text
Requested Quantity
        │
        ▼
Compare with Product Stock
        │
   ┌────┴────┐
   │         │
Enough    Not Enough
   │         │
   ▼         ▼
Checkout   Reject
```

---

## 4. Asynchronous Cart Updates

Cart quantity updates communicate with the backend using JavaScript `fetch()`.

```text
User changes quantity
        │
        ▼
JavaScript fetch()
        │
        ▼
/update_order/
        │
        ▼
Django View
        │
        ▼
Update OrderDetail
        │
        ▼
Return updated status
```

This provides a smoother cart interaction without requiring a complete page reload for every quantity update.

---

## 5. Product Rating Aggregation

Product ratings are stored in `OrderDetail` together with customer comments.

The product detail page can calculate the average rating based on customer reviews.

---

# 🧪 Testing

Django's built-in testing framework can be executed with:

```bash
python manage.py test
```

The project also includes a GitHub Actions workflow intended to automatically run tests when changes are pushed or pull requests are created.

---

# 🔮 Future Improvements

Potential improvements for a production-ready version include:

- [ ] PostgreSQL or MySQL production database
- [ ] Django REST Framework API
- [ ] JWT authentication
- [ ] Payment gateway integration
- [ ] Email order confirmation
- [ ] Advanced product filtering
- [ ] Product image optimization
- [ ] Admin dashboard
- [ ] Order status tracking
- [ ] Automated unit and integration tests
- [ ] Docker deployment
- [ ] Environment variable configuration
- [ ] Production CI/CD deployment

---

# 🔒 Production Considerations

For production deployment, the following improvements should be made:

- Move `SECRET_KEY` to environment variables.
- Set `DEBUG=False`.
- Configure `ALLOWED_HOSTS`.
- Use a production database instead of SQLite.
- Configure static and media file storage.
- Remove local virtual environment files from Git.
- Remove Python cache files such as `__pycache__`.
- Avoid committing the local `db.sqlite3` database.
- Maintain dependencies in `requirements.txt`.

---

# 📚 What I Learned

Through this project, I practiced:

- Django MVT architecture
- Django ORM
- Relational database modeling
- User authentication
- CRUD operations
- E-commerce business logic
- Shopping cart implementation
- Order processing
- Inventory management
- Database transactions
- Search and pagination
- Server-side rendering
- JavaScript asynchronous requests
- Git and GitHub workflow

---

# 👨‍💻 Author

**Hoang Quoc Phong**

Software Engineering / Information Technology

### Interests

- Backend Development
- Node.js
- Python / Django
- RESTful API
- Database Systems
- Software Engineering

---

# 📄 License

This project was created for learning and portfolio purposes.