import time
import pytest
from playwright.sync_api import sync_playwright, expect

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://admin.dev.govone.digital")  # URL do teste

        # Usa type() para simular digitação real (aciona eventos JS)
        page.locator("#username").type("25127127024")
        page.locator("#password").type("123Mudar")

        # Espera o botão ser habilitado
        expect(page.locator("#submit-login")).to_be_enabled(timeout=10000)

        # Clica no botão
        page.click("#submit-login")
        # Espera a navegação após o login
        time.sleep(4)
        browser.close()
