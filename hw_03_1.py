import os
import shutil
import sys

def main():
    # Парсинг аргументів
    if len(sys.argv) < 2:
        print("Використання: python script.py <source_directory> [destination_directory]")
        return
    
    source_dir = sys.argv[1]
    if len(sys.argv) > 2:
        destination_dir = sys.argv[2]
    else:
        destination_dir = os.path.join(source_dir, "dist")

    # Створення директорії призначення, якщо вона не існує
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Рекурсивне копіювання файлів
    try:
        copy_files(source_dir, destination_dir)
        print("Файли успішно скопійовано.")
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def copy_files(current_dir, destination_dir):
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            # Рекурсивний виклик для директорії
            copy_files(item_path, destination_dir)
        elif os.path.isfile(item_path):
            # Визначення розширення файлу та створення відповідної піддиректорії
            ext = os.path.splitext(item)[-1][1:]  # Вилучення тексту після крапки
            if ext == "":
                ext = "no_extension"
            ext_dir = os.path.join(destination_dir, ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            
            # Копіювання файлу
            shutil.copy(item_path, ext_dir)

if __name__ == "__main__":
    main()