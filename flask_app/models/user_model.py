from flask_app.config.mysql_conn import connectToMySQL
from flask import flash
import re
import pprint

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = 'magazines'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name  = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Create
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def edit_user(cls, data):
        pass
    #     query = "UPDATE tv_show SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"
    #     return connectToMySQL(cls.DB).query_db(query, data)
    
    # Read all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    # Read one by id
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": data}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    # Read one by email
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)

        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
    
    # Validate user
    @staticmethod
    def validate_user(user, users):
        is_valid = True

        # Check for email
        email_list = []
        for user_email in users:
            email_list.append(user_email.email)

        if len(user['first_name']) <= 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) <= 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if len(user['email']) < 2:
            flash("Email must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if user['email'] in email_list:
            flash("That email is already in use.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords must match.")
            is_valid = False

        return is_valid