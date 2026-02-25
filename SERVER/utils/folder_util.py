import os
import tempfile

NAME_LENGTH_CONSTRAINTS = [3, 15]

def create_folder(root_dir):
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

        return True
    return False

def create_joined_folder_path(root, name):
    path = os.path.join(root, name)
    create_folder(path)

    return path

def storage_directory(root_dir, folder_name):
    folder_name = folder_name.lower()
    if (len(folder_name) < 2 or len(folder_name) < NAME_LENGTH_CONSTRAINTS[0] or len(folder_name) > NAME_LENGTH_CONSTRAINTS[1] or len(folder_name) > 20):
        return False
    
    path = create_joined_folder_path(root_dir, folder_name[0])
    path = create_joined_folder_path(path, folder_name[:2])
    
    return path

def write_to_file(root_dir, meta_data):
    user = meta_data["user"]

    file_path = os.path.join(storage_directory(root_dir, user), user)
    file_path = file_path.lower()

    dirpath = os.path.dirname(file_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    def format_line(k, v):
        return f"{k}: {str(v)}\n"

    if not os.path.exists(file_path):
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=dirpath) as tmp:
            for k in sorted(meta_data.keys()):
                tmp.write(format_line(k, meta_data[k]))
            tmp_name = tmp.name
        os.replace(tmp_name, file_path)
        return file_path

    updated_keys = set()
    with open(file_path, "r", encoding="utf-8") as src, \
         tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=dirpath) as tmp:
        for raw_line in src:
            stripped = raw_line.rstrip("\n")
            if ":" in stripped:
                key_part = stripped.split(":", 1)[0].strip()
            else:
                key_part = stripped.strip()

            if key_part in meta_data:
                tmp.write(format_line(key_part, meta_data[key_part]))
                updated_keys.add(key_part)
            else:
                tmp.write(raw_line)
        tmp_name = tmp.name

    missing_keys = sorted(set(meta_data.keys()) - updated_keys)
    if missing_keys:
        with open(tmp_name, "a", encoding="utf-8") as tmp:
            try:
                with open(file_path, "rb") as fcheck:
                    fcheck.seek(-1, os.SEEK_END)
                    last = fcheck.read(1)
                    if last != b"\n":
                        tmp.write("\n")
            except (OSError, ValueError):
                pass

            for k in missing_keys:
                tmp.write(format_line(k, meta_data[k]))

    os.replace(tmp_name, file_path)
    return file_path

def read_from_file(root_dir, meta_data):
    user = meta_data["user"]

    file_path = os.path.join(storage_directory(root_dir, user), user)
    file_path = file_path.lower()

    if not os.path.exists(file_path):
        return {}

    result = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or ":" not in stripped:
                continue 

            key, value = stripped.split(":", 1)
            result[key.strip()] = value.strip()

    return result

def does_file_exist(root_dir, name):
    if not name:
        return False

    name = name.lower()

    if (len(name) < 2 or len(name) < NAME_LENGTH_CONSTRAINTS[0] or len(name) > NAME_LENGTH_CONSTRAINTS[1] or len(name) > 20):
        return False

    path = os.path.join(root_dir, name[0])
    path = os.path.join(path, name[:2])
    file_path = os.path.join(path, name)

    return os.path.isfile(file_path)
