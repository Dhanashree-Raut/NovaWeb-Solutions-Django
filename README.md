# NovaWeb Solutions

NovaWeb Solutions is a modern **service-based website** built using
**Django and Bootstrap**.\
The project demonstrates a professional web development agency website
with multiple pages, responsive design, and a working contact form.

------------------------------------------------------------------------

## 🚀 Live Demo

**Deployed on Render:**\
https://novaweb-solutions-django.onrender.com/

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python
-   Django
-   Bootstrap
-   HTML5
-   CSS3
-   JavaScript
-   WhiteNoise (static file handling)
-   Gunicorn (production server)

------------------------------------------------------------------------

## 📂 Features

-   Modern responsive UI
-   Hero section with call-to-action
-   About page with company details
-   Services page showcasing offerings
-   Contact form with database storage
-   Django Admin panel to manage contact messages
-   Scroll animations for better UX
-   Production-ready static file configuration

------------------------------------------------------------------------

## 📄 Pages Included

-   Home
-   About
-   Services
-   Contact

------------------------------------------------------------------------

## 📬 Contact Form

Users can send messages using the contact form.\
Submitted messages are stored in the database and can be viewed from the
**Django Admin Dashboard**.

------------------------------------------------------------------------

## ⚙️ Installation

Clone the repository:

``` bash
git clone https://github.com/Dhanashree-Raut/NovaWeb-Solutions-Django.git
```

Move into the project directory:

``` bash
cd NovaWeb-Solutions-Django
```

Create a virtual environment:

``` bash
python -m venv venv
```

Activate virtual environment

**Windows**

``` bash
venv\Scripts\activate
```

**Mac/Linux**

``` bash
source venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run migrations:

``` bash
python manage.py migrate
```

Run development server:

``` bash
python manage.py runserver
```

Open in browser:

    http://127.0.0.1:8000/

------------------------------------------------------------------------

## 📦 Deployment

This project is deployed on **Render** using:

-   Gunicorn
-   WhiteNoise
-   collectstatic

------------------------------------------------------------------------

## 📁 Project Structure

    NovaWeb-Solutions-Django
    │
    ├── home/
    ├── mysite/
    ├── static/
    ├── templates/
    ├── manage.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 👩‍💻 Author

**Dhanashree Raut**

GitHub:\
https://github.com/Dhanashree-Raut

LinkedIn:\
https://www.linkedin.com/in/dhanashree-raut-3a763420b

------------------------------------------------------------------------

## ⭐ Future Improvements

-   Portfolio section
-   Blog system
-   Client testimonials
-   Authentication system
-   API integrations
