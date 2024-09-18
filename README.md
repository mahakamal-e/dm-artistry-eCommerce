# D&M Artistry - Django E-commerce Platform

**D&M Artistry** is an online art gallery and shop that showcases original and curated artwork, allowing users to browse, purchase, and explore various art collections. The platform enables users to manage their accounts, view order histories, and complete purchases using a shopping cart system.

## Key Features
- **Browse Artwork**: Users can explore a collection of original and curated art pieces.
- **User Authentication**: Registered users can manage their profiles, view order history, and make purchases.
- **Shopping Cart**: Add, update, and remove items from the cart.
- **Checkout**: A seamless checkout process with payment methods, including credit cards (Stripe integration planned, not yet implemented).
- **Order Management**: Users can view their past orders from their profile.
- **Anonymous User Support**: The platform allows anonymous users to shop and checkout as guests.
  
## Apps Overview

1. **Shop**: Handles product listings and categories, allowing users to browse and view artwork.
2. **Cart**: Manages the shopping cart functionality, including adding and removing items.
3. **Orders**: Manages the checkout process, including order creation and management.
               And handles the logic for payment methods.
4. **Accounts**: Handles user registration, login, and profile management. 

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
###Explanation of Routes
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
   python -m venv myenv
   source myenv/bin/activate

3. **Install Dependencies**
   pip install -r requirements.txt

4. **Apply Migrations**
   python manage.py migrate

5. **Load Initial Data**
   python manage.py import_data

6. **Import Additional Data**
   python manage.py load_data

7. **Run the Development Server**
   python manage.py runserver

## Usage Guide
Homepage: Browse featured products.
Shop: Navigate through the available art categories and select products to view in detail.
Cart: Add products to the cart, review them, and adjust quantities.
Checkout: After adding products, proceed to checkout, fill in shipping details, and select a payment method.
Profile: If registered, view order history and manage account settings.

## Authors

- **[Maha Kamal]** - *Full-Stack Developer* - (https://github.com/mahakamal-e)
- **[Deena Kamal]** - *Full-Stack Developer* - (https://github.com/deenakamal)

We worked together to build D&M Artistry, an online platform for showcasing and purchasing artwork. Our collaborative effort focused on creating a user-friendly e-commerce experience, implementing key features like product listings, shopping carts, and user profiles.

