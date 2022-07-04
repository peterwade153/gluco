# Gluco

REST API to track blood glucose levels

Requires Postgres and built with Python 3.8 

### Installation

1. Create and activate a virtual environment and Clone the project `https://github.com/peterwade153/gluco.git`

2. Move into the project folder
   ```
   $ cd gluco
   ```

3. Install dependencies 
   ```
   $ pip install -r requirements.txt
   ```

4. Create a `.env` file from the `.env.sample` file.  Replace the variables in the sample file with the actual variables, such the database credentials, secret key etc. leaving the `ENV_VAR_FILE` as it is for local testing.

5. Run migrations
   ```
   python manage.py migrate
   ```

6. Start server
   ```
   python manage.py runserver
   ```

7.  The application can be accessed via swagger docs here http://127.0.0.1:8000/

6. Populate Database with sample data
   ```
   python manage.py populate
   ```

### Endpoint

Request             | Endpoints                                                               |       Functionality 
--------------------|-------------------------------------------------------------------------|--------------------------------
GET                 |  `/api/v1/levels/`                                                      |  Glucose levels.
GET    by ID        |  `/api/v1/levels/123`                                                   |  Glucose level entry by ID.
GET    Ordering     |  `/api/v1/levels/?ordering=id`                                          |  Ordering based on (id, user_id, seriennummer, gerätezeitstempel)
GET    limit result |  `/api/v1/levels/?size=5`                                               |  Limit return size of results
GET    page         |  `/api/v1/levels/?page=5`                                               |  Results on page 5
GET    filter       |  `/api/v1/levels/?start=2021-02-02T03:03:00Z&stop=2021-11-02T03:03:00Z` |  Filter by start date to stopdate