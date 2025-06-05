from app import create_app, db
from app.models import *

app = create_app()

with app.app_context():
    try:
        db.create_all()
        print("Tables created successfully.")
    except Exception as e:
        print("Error creating tables:", e)

if __name__ == '__main__':
    app.run(debug=True)
