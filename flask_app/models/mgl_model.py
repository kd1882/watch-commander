from flask_app.config.mysql_conn import connectToMySQL
from flask import flash
import re
import pprint

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class MGL:
    DB = 'watchCommander'

    def __init__(self, data):
        self.Chapter = data['Chapter']
        self.Section = data['Section']
        self.Name  = data['Name']
        self.Text = data['Text']
        self.IsRepealed = data['IsRepealed']
        self.Details = data['Details']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Create
    # @classmethod
    # def save(cls, data):
    #     query = "INSERT INTO users (first_name, last_name, email, department, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(department)s, %(password)s);"
    #     return connectToMySQL(cls.DB).query_db(query, data)
    
    # get sections from chapter
    @classmethod
    def get_sections(cls, data):
        query = "SELECT * FROM mgl WHERE Chapter = %(chapter)s;"
        data = {"chapter": data}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    
    # Read all
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM mgl;"
        results = connectToMySQL(cls.DB).query_db(query)
        mgl_all = []
        for mgl in results:
            mgl_all.append(cls(mgl))
        return mgl_all
    
    # # Read one by id
    # @classmethod
    # def get_by_id(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(id)s;"
    #     data = {"id": data}
    #     result = connectToMySQL(cls.DB).query_db(query, data)
    #     return cls(result[0])
    
    # # Read one by email
    # @classmethod
    # def get_by_email(cls, data):
    #     query = "SELECT * FROM users WHERE email = %(email)s;"
    #     result = connectToMySQL(cls.DB).query_db(query,data)

    #     # Didn't find a matching user
    #     if len(result) < 1:
    #         return False
    #     return cls(result[0])
    
    # # Validate user
    # @staticmethod
    # def validate_user(user, users):
    #     is_valid = True

    #     # Check for email
    #     email_list = []
    #     for user_email in users:
    #         email_list.append(user_email.email)

    #     if len(user['first_name']) <= 2:
    #         flash("First name must be at least 2 characters.")
    #         is_valid = False
    #     if len(user['last_name']) <= 2:
    #         flash("Last name must be at least 2 characters.")
    #         is_valid = False
    #     if len(user['email']) < 2:
    #         flash("Email must be at least 2 characters.")
    #         is_valid = False
    #     if not EMAIL_REGEX.match(user['email']): 
    #         flash("Invalid email address!")
    #         is_valid = False
    #     if len(user['department']) < 2:
    #         flash("You must select a Department/Affiliation.")
    #         is_valid = False
    #     if user['email'] in email_list:
    #         flash("That email is already in use.")
    #         is_valid = False
    #     if len(user['password']) < 8:
    #         flash("Password must be at least 8 characters.")
    #         is_valid = False
    #     if user['password'] != user['confirm_password']:
    #         flash("Passwords must match.")
    #         is_valid = False

    #     return is_valid