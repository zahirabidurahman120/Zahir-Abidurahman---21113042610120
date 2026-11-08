import json
from pathlib import Path

path = Path("username.json")


def get_stored_username():
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)

    return None


def get_new_username():
    username = input("Masukkan nama pengguna: ")

    contents = json.dumps(username)
    path.write_text(contents)

    return username


def greet_user():
    username = get_stored_username()

    if username:
        print(f"Apakah nama Anda {username}?")

        answer = input("Benar? (y/n): ")

        if answer.lower() == "y":
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username()
            print(f"Selamat datang, {username}!")

    else:
        username = get_new_username()
        print(f"Selamat datang, {username}!")


greet_user()