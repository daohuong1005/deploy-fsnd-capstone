from flask import Flask
from flask_migrate import Migrate
from app import create_app
from models.database import db

app = create_app()
migrate = Migrate(app, db)

# Lệnh cho Flask CLI
@app.cli.command("db-init")
def db_init():
    """Initialize the database."""
    db.create_all()
    print("Database initialized.")

@app.cli.command("db-migrate")
def db_migrate():
    """Run migrations."""
    from flask_migrate import upgrade
    upgrade()
    print("Migrations completed.")

if __name__ == "__main__":
    app.run()