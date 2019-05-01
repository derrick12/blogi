from app import create_app, db
from app.models import User, Comments, Post
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

# the Manager class from flask-script that will initialize our extension and the Server class that help us launch our server.

# Creating app instance
# In development - create_app('development')
# In test - create_app('test')
# In production - create_app('production') 
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# Flask-script shell
@manager.shell
def make_shell_context():    
    """
    Flask-script shell
        return instances
    """
    return dict(app = app,db = db,User = User, Post=Post, Comments=Comments)

if __name__ == '__main__':
    manager.run()
