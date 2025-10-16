from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Get the absolute path to the HTML file
        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")
        # Generate a PDF to check the print layout
        page.pdf(path="jules-scratch/verification/verification.pdf", format='A4', print_background=True)
        # Also take a screenshot of the first page for a quick visual check
        page.screenshot(path="jules-scratch/verification/verification.png")
        browser.close()

if __name__ == "__main__":
    run()