🛒 Django Electronic Store

A full-featured **e-commerce web application** built with **Django** for selling electronic products such as **laptops, mobile phones, headphones, and other digital gadgets.  
This project was developed as a practical Django learning experience with a clean, modular architecture and real-world e-commerce features.

---

🚀 Features

- User authentication system (Register, Login, Logout)
- Product management with categories and brands
- Product listing and detail pages
- Product sorting and filtering
- Shopping cart system
- Order placement and order management
- Wishlist functionality
- User dashboard (profile & orders)
- Blog and articles module
- About Us and Contact Us pages
- FAQ section
- Homepage slider and banners
- Dynamic header and footer using context processors
- Django Admin panel for full site management

---

🧰 Tech Stack

- **Backend:** Python 3, Django 5.2.6
- **Database:** SQLite3
- **Frontend:**
  - HTML5 / CSS3
  - Bootstrap
  - JavaScript / jQuery
  - Owl Carousel
- **Third-party Packages:**
  - `sorl-thumbnail`
  - `django-render-partial`

---

🧩 Project Structure

```text
config/
├── home_module
├── account_module
├── product_module
├── blog_module
├── cart_module
├── order_module
├── wishlist_module
├── dashboard_module
├── faq_module
├── about_module
├── contact_module

--------------------------------------------------
⚙️ Installation & Setup

Clone the repository:

git clone <repository-url>
cd project


Create and activate a virtual environment:

python -m venv venv
source venv/binactivate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Run the development server:

python manage.py runserver


The application will be available at:

http://127.0.0.1:8000/

-------------------------------------------------

🎨 Frontend Template Credit

The frontend design of this project is based on the following open-source template.
Special thanks to the template creator for providing a clean and professional e-commerce UI.

🔗 Template Repository:
https://github.com/ahmadhuss/ludus-free-premium-ecommerce-template
├── site_module
├── polls
