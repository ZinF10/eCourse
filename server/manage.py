import getpass
from app import create_app, dao
from flask.cli import FlaskGroup

cli = FlaskGroup(create_app)

@cli.command("create_admin")
def create_admin():
    """Creates the admin user."""
    username = input("Username: ")
    email = input("Email address: ")
    password = getpass.getpass("Password: ")
    confirm_password = getpass.getpass("Password (again): ")
    
    if password != confirm_password:
        print("Passwords don't match")
    else:
        try:
            dao.create_user(username=username, email=email, password=password, is_admin=True)
            print(f"Admin with email {email} created successfully!")
        except Exception:
            print("Couldn't create admin user.")
            
if __name__ == "__main__":
    cli()