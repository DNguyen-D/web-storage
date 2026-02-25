from . import folder_util as f_util
from . import auth_util

root = "SERVER/storage"

CORE_META_DATA = {"subscription": "false"}

def sign_up(user, password):
    if f_util.does_file_exist(root, user):
        return False

    hashed = auth_util.hash_password(password)

    meta_data = {
        "user": user,
        "password": hashed
    }

    meta_data = meta_data | CORE_META_DATA

    f_util.write_to_file(root, meta_data)
    return True


def login(user, password):
    if not f_util.does_file_exist(root, user):
        print("User doesn't exists.")
        return False

    meta_data = {"user": user}
    stored_data = f_util.read_from_file(root, meta_data)

    if "password" not in stored_data:
        return False

    return auth_util.verify_password(password, stored_data["password"])

def get_user_data(user):
    return f_util.read_from_file(root, {"user": user})



