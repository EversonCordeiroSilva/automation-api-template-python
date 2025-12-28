import subprocess
import sys
from src.config.allure_config import install_allure_if_needed

def run_tests():
    print("Running Behave tests...")
    subprocess.run(
        [sys.executable, "-m", "behave"],
        check=True
    )

def generate_allure_html():
    allure_results = "resources/reports/allure-results"
    allure_html = "resources/reports/allure-html"
    print("Generating Allure HTML report...")
    allure_bin = install_allure_if_needed()
    try:
        subprocess.run(
            [
                allure_bin,
                "generate",
                allure_results,
                "-o",
                allure_html,
                "--clean"
            ],
            check=True
        )
        print("Allure report generated successfully.")
    except subprocess.CalledProcessError:
        print("ERROR: Failed to generate Allure report.")


if __name__ == "__main__":
    run_tests()
    generate_allure_html()