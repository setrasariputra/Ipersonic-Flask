from .models import User

def ping():
    return 'Ping!'

def get_user(username):
    # Logika untuk mendapatkan user
    # Di sini kita hanya mengembalikan objek User sederhana
    return User(username, f"{username}@example.com")