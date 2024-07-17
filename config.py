import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    # Tambahkan konfigurasi lainnya di sini
