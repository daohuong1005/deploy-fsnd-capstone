from flask import Flask
from flask_migrate import Migrate
from app import create_app
from models.database import db 

app = create_app()  # Create your Flask application instance
migrate = Migrate(app, db)  # Setup Flask-Migrate

@app.cli.command("db_upgrade")
def db_upgrade():
    """Run database migrations."""
    from flask_migrate import upgrade
    upgrade()

if __name__ == "__main__":
    app.run()