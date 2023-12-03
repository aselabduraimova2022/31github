import shutil
import os

def backup_files(source_folder,destination_folder):
try:
if not
os.path.exists(destination_folder):
os.makedirs(destination_folder)

files = os.listdir(source_folder)

for file in files:
source_path = os.path.join(source_folder, file)
desination_path = os.path.join(destination_folder, file)
shutil.copy2(source_path,destination_path)

print("Резервное копирование завершено успешно. ")
except Exception as e:
print(f"Произошла ошибка при копировании файлов: {e} ")
source_folder = "
