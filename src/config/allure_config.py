import os
import urllib.request
import zipfile

ALLURE_VERSION = "2.21.0"
ALLURE_DIR = os.path.join(os.getcwd(), "resources/reports/allure-cli")


def get_allure_bin():
    return os.path.join(
        ALLURE_DIR,
        f"allure-{ALLURE_VERSION}",
        "bin",
        "allure.bat"
    )


def install_allure_if_needed():
    allure_bin = get_allure_bin()

    if os.path.exists(allure_bin):
        return allure_bin

    print("Allure CLI not found. Downloading...")

    url = (
        "https://github.com/allure-framework/allure2/"
        f"releases/download/{ALLURE_VERSION}/"
        f"allure-{ALLURE_VERSION}.zip"
    )

    zip_path = "allure.zip"
    urllib.request.urlretrieve(url, zip_path)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(ALLURE_DIR)

    os.remove(zip_path)
    print("Allure CLI installed successfully.")

    return allure_bin
