import logging
import os
import platform
import shutil

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def get_default_extensions() -> dict[str, list[str]]:
    return {
        "imagens": [".jpg", ".png", ".jpeg", ".gif"],
        "videos": [".mp4", ".mkv", ".mov", ".flv"],
        "docs": [".pdf", ".xls", ".xlsx", ".docx", ".doc", ".txt", ".ppt", ".pptx"],
        "archives": [".zip", ".rar", ".7z"],
        "setups": [".exe", ".msi"],
        "Others": [],
    }


def get_correct_folder(
    file_extension: str, extensions_map: dict[str, list[str]]
) -> str:
    for folder, extensions in extensions_map.items():
        if file_extension in extensions:
            return folder
    logger.info(f"Extensão inesperada: '{file_extension}', movendo para 'Outros'")
    return "Others"


def organize_files(folder_path: str):
    default_extensions = get_default_extensions()
    all_files: list[str] = os.listdir(folder_path)
    for file in all_files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_path)[1].lower()
            correct_folder = os.path.join(
                folder_path, get_correct_folder(file_extension, default_extensions)
            )
            os.makedirs(correct_folder, exist_ok=True)
            logger.info(f"Movendo '{file}' para '{correct_folder}'")
            shutil.move(file_path, correct_folder)


while True:
    target_folder = input("Caminho da pasta para organizar: ").strip()

    if os.path.isdir(target_folder):
        organize_files(target_folder)
        finish = input("Deseja executar novamente? (S/N)").lower().strip()

        if finish == "n":
            print("Encerrando...")
            break

        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    else:
        print("O diretório inserido não é válido!")
