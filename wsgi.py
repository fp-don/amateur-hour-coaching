"""
WSGI entry point for AmateurHour Coaching website
Used for production deployment with WSGI servers like Gunicorn
"""

from app import app

if __name__ == "__main__":
    app.run()

