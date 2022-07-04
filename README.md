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
