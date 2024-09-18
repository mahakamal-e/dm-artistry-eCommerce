# D&M Artistry - Django E-commerce Platform

**D&M Artistry** is an online art gallery and shop that showcases original and curated artwork, allowing users to browse, purchase, and explore various art collections. The platform enables users to manage their accounts, view order histories, and complete purchases using a shopping cart system.

## Key Features
- **Browse Artwork**: Users can explore a collection of original and curated art pieces.
- **User Authentication**: Registered users can manage their profiles, view order history, and make purchases.
- **Shopping Cart**: Add, update, and remove items from the cart.
- **Checkout**: A seamless checkout process with payment methods, including credit cards (Stripe integration planned, not yet implemented).
- **Order Management**: Users can view their past orders from their profile.
- **Anonymous User Support**: The platform allows anonymous users to shop and checkout as guests.

## Apps and Their Responsibilities

1. **Shop**:
   - **Product Listings**: Manages and displays a comprehensive list of available artwork and categories. Users can browse through different art collections and view detailed information about each product.
   - **Homepage**: Displays featured products and provides an introduction to the art gallery, setting the tone for the site’s artistic offerings.
   - **Product Detail**: Shows detailed information about individual artwork pieces when a user selects a product.
   - **About Us Page**: Provides information about the D&M Artistry team, their vision, and what they offer. This page helps users understand the mission and values of the gallery.
   - **Contact Us Page**: Allows users to get in touch with the gallery for inquiries, support, or feedback. This page typically includes a contact form and relevant contact details.

2. **Cart**:
   - **Cart Management**: Handles the addition and removal of products from the shopping cart, allowing users to view and manage items they intend to purchase.

3. **Orders**:
   - **Checkout and Payment**: Manages the checkout process, including entering shipping details and processing payments. The Orders app integrates payment functionality directly within the checkout process to ensure a seamless transaction experience.
   - **Order History**: Allows authenticated users to view their past orders and order details. Provides a comprehensive view of previous transactions.

4. **Accounts**:
   - **User Authentication**: Handles user login, registration, and profile management. Authenticated users can manage their accounts, view order history, and update their profile information.


## Routes Overview

## Routes Overview

| Route                                | HTTP Method | Description                                                                          |
|--------------------------------------|-------------|--------------------------------------------------------------------------------------|
| `/shop/`                                  | `GET`       | Displays the homepage with featured products.                                        |
| `/shop/about/`                            | `GET`       | Displays the About Us page with information about D&M Artistry.                      |
| `/shop/contact/`                          | `GET`       | Displays the contact us page.                                                         |
| `/shop/products/`                         | `GET`       | Lists all available artwork products and categories.                                 |
| `/shop/products/<int:id>/`                | `GET`       | Displays the details of a single product based on its ID.                             |
| `cart/view/`                             | `GET`       | Shows the items currently in the user's cart (for authenticated users).               |
| `cart/add/<int:product_id>/`              | `POST`      | Adds a product to the cart (for authenticated users).                                 |
| `cart/remove/<int:item_id>/`             | `POST`      | Removes a product from the cart (for authenticated users).                            |
| `cart/anon/`                             | `GET`       | Shows the items currently in the cart for anonymous users.                            |
| `cart/anon/add/<int:product_id>/`         | `POST`      | Adds a product to the cart (for anonymous users).                                     |
| `cart/anon/remove/<int:product_id>/`      | `POST`      | Removes a product from the cart (for anonymous users).                                |
| `/cart/cart/empty/`                       | `POST`      | Empties the cart (for authenticated users).                                           |
| `/accounts/register/`                         | `GET`, `POST`| Registration page for new users to create an account.                                |
| `/accounts/login/`                            | `GET`, `POST`| Login page for users to authenticate.                                                |
| `/accounts/profile/`                          | `GET`       | Displays the user's profile and order history (authenticated users only).            |
| `/accounts/logout/`                           | `POST`      | Logs out the current user.                                                           |

### Explanation of Routes
**Homepage**: Displays featured products and main content of the site.
**About Us**: Provides information about D&M Artistry.
**Contact Us**: Allows users to get in touch with you.
**Products List**: Shows all products and their categories.
**Product Detail**: Displays detailed information about a specific product.
**Cart Management**: Handles viewing, adding, and removing items in the cart for both authenticated and anonymous users.
**Registration and Login**: Handles user registration, login, and profile management.
**Profile**: Displays user-specific data and order history.
**Logout**: Logs the user out of their session.
This table provides a clear overview of the different routes and their purposes in your Django project.## Installation and Setup

### Prerequisites
- Python 3.x
- Django 4.x
- Redis (optional, for caching)
- SQLite (or PostgreSQL for production)

### Steps to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/dm-artistry-eCommerce.git
   cd dm-artistry-eCommerce

2. **Activate the virtual environment**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Load Initial Data**
   ```bash
   python manage.py import_data

6. **Import Additional Data**
   ```bash
    python manage.py load_data

7. **Run the Development Server**
   ```bash
   python manage.py runserver

8. **Access the site**
   ```bash
   Open http://127.0.0.1:8000 in your browser.

## Usage Guide

Homepage: Browse featured products.
Shop: Navigate through the available art categories and select products to view in detail.
Cart: Add products to the cart, review them, and adjust quantities.
Checkout: After adding products, proceed to checkout, fill in shipping details, and select a payment method.
Profile: If registered, view order history and manage account settings.

## Authors

- **[Maha Kamal]** - *Full-Stack Developer* - [Github](https://github.com/mahakamal-e)
- **[Deena Kamal]** - *Full-Stack Developer* - [Github](https://github.com/deenakamal)

We worked together to build D&M Artistry, an online platform for showcasing and purchasing artwork. Our collaborative effort focused on creating a user-friendly e-commerce experience, implementing key features like product listings, shopping carts, and user profiles.

