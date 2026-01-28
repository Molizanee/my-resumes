#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright"]
# ///
"""Convert HTML resume to PDF using playwright."""

from pathlib import Path

from playwright.sync_api import sync_playwright


def main():
    script_dir = Path(__file__).parent
    files = ("david-molizane.html", "david-molizane-pt-br.html")
    for file in files:
        input_file = script_dir / file
        output_file = input_file.with_suffix(".pdf")

        # Convert to file:// URL for playwright
        file_url = input_file.resolve().as_uri()

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(file_url)
            page.pdf(path=str(output_file), format="A4", print_background=True)
            browser.close()

        print(f"Successfully converted to {output_file}")


if __name__ == "__main__":
    main()
