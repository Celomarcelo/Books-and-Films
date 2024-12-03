# **README: Review Platform Backend**

---

## **Project Description**
The **Review Platform** is a backend application developed with Django and Django REST Framework. It provides a robust API to manage reviews of books and films, including features such as JWT authentication, user management, categories, genres, likes, and comments.

---

## **Technologies Used**
- **Django** (v3.2)
- **Django REST Framework**
- **PostgreSQL** (via `dj_database_url`)
- **JWT Authentication** (`SimpleJWT`)
- **Cloudinary** (image storage)
- **WhiteNoise** (static file management)
- **CORS Headers** (cross-origin support)

---

## **Features**
- **Authentication and User Registration:**
  - User registration with validation.
  - JWT authentication with access and refresh token generation.
  - Password change.
  - Profile deletion.
- **Review Management:**
  - Full CRUD for reviews.
  - Filters by categories and genres.
  - Review search by title, author, or content.
- **Likes and Comments:**
  - Like/unlike reviews.
  - Add, list, and delete comments.
- **Categories and Genres:**
  - List categories and genres.
  - Filter reviews by category and genre.
- **Favorites:**
  - Add or remove favorite users.
  - List authenticated user's favorites.

---

## **Requirements**
Make sure you have the following tools installed:
- Python 3.8 or higher
- PostgreSQL
- Virtualenv (recommended)
- Git

---

## **Main Routes**

### **Authentication**
- **POST** `/api/token/` - Get access and refresh tokens.
- **POST** `/api/token/refresh/` - Refresh the access token.
- **POST** `/api/register/` - Register a new user.

### **Users**
- **GET** `/api/user-profile/` - Retrieve profile information.
- **PUT** `/api/user-profile/` - Update profile.
- **DELETE** `/api/user-profile/` - Delete profile.
- **POST** `/api/change-password/` - Change password.

### **Reviews**
- **GET** `/api/reviews/` - List all reviews.
- **POST** `/api/reviews/` - Create a new review.
- **GET** `/api/reviews/<id>/` - Retrieve review details.
- **PUT** `/api/reviews/<id>/` - Edit a review.
- **DELETE** `/api/reviews/<id>/` - Delete a review.

### **Likes and Comments**
- **POST** `/api/reviews/<id>/like/` - Like/unlike a review.
- **POST** `/api/reviews/<id>/comments/` - Add a comment.
- **GET** `/api/reviews/<id>/comments/` - List comments.
- **DELETE** `/api/comments/<id>/` - Delete a comment.

### **Categories and Genres**
- **GET** `/api/categories/` - List categories.
- **GET** `/api/categories/<id>/genres/` - List genres in a category.


## Deployment

For correct operation, it is necessary to create two apps on Heroku, one for the frontend and one for the API.
The deployment process ensures that your Books and Films application is live and accessible to users. Below is a step-by-step guide with detailed explanations for deploying the application using Heroku:

1. **Clone the Repository**  
   Clone the project repositories to your local environment or GitHub account.

2. **Install Heroku CLI**  
   Download and install the Heroku CLI.
   After installation, log in using:

    `heroku login`, on your terminal.

   This opens a browser window for authentication.

3. **Create a Heroku App**  
   On your Heroku dashboard, click the `New` button in the right corner and then `Create new app`.
   On the next page, add a name for your app and select the region you want.
   On the next page, navigate to the `Deploy` section and in the `Deployment method` option select `Github`, connect to your Github repository.

   **Repeat this process to create the second app where the API will work**

4. **Add Necessary Add-ons**  
    **This step is only necessary for the API app**
    In the `Resources` tab on your Heroku app's dashboard, add the following `add ons` to the search field:

    - Heroku Postgres for the database.
    - Cloudinary for image storage.

5. **Configure Environment Variables**  

    **Frontend app**
    In the Heroku dasbord, go to the `settings` tab and in the `Config Var` section add the following variable: 
    - `REACT_APP_API_URL` with the value of the url of your Api app.

    It can be found in the dasbord of your API app in the `settings` tab in the `Domains` section.

    **API app**
    In the Heroku dasbord, go to the `settings` tab and in the `Config Var` section add the following variable:
    - `ALLOWED_HOSTS`: Your app's domain.
    - `DATABASE_URL`: URL for the Postgres database.
    - `CLOUDINARY_URL`: Your Cloudinary API key.
    - `DEBUG` : value of False.
    - `SECRET_KEY`: Django secret key.

6. **Perform Database Migrations**  
    On your environment access the Heroku terminal:

    `heroku run bash -a your api app name`
    Replace "your api app name" with the name of your API app

    Run `python manage.py migrate` in the Heroku terminal.

7. **Deploy the Application**  
   After this process, in the `Deploy` tab in the `Manual deploy` section, click on the `Deploy Branch` button to start the app.

8. **Access the Live Application**  
   The site will be live at the Heroku app URL.

---

