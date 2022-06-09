from app import app
from app import routes

if __name__ == "__main__":         # Protect this code to be ran if he is imported
    app.run(port=5000, debug=True)
