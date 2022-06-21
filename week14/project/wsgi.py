from app import app
from app import routes
from app import models

if __name__ == "__main__":         # Protect this code to be ran if he is imported
    app.run(port=5000, debug=True)
