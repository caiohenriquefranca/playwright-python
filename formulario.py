import pytest
import os
import time
from playwright.sync_api import sync_playwright, expect

def test_formulario():
    os.makedirs("videos", exist_ok=True)
    with sync_playwright() as p:
        # Inicia o navegador com uma configuração mais lenta para melhor visualização utilizando slow_mo
        browser = p.chromium.launch(headless=False, slow_mo=1000)

         # Cria um contexto de navegador para gravar o vídeo
        context = browser.new_context(
            record_video_dir="videos/",
            record_video_size={"width": 1920, "height": 1080},
            viewport={"width": 1920, "height": 1080}
        )  
        page = context.new_page()     
        # Acessa a página de Login
        page.goto("https://sso.dev.govone.digital/sso/cidadao?client_id=portal.dev.govone.digital&state=https://portal.dev.govone.digital/inicio")
        page.locator("#username").type("25127127024")
        page.locator("#password").type("123Mudar")
        expect(page.locator("#submit-login")).to_be_enabled(timeout=10000)
        page.click("#submit-login")

        # Espera a navegação após o login
        expect(page).to_have_url("https://portal.dev.govone.digital/inicio")

        # Fechar modal de boas-vindas
        #page.locator("#close-btn").click()

        #Permtir cookies
        #page.get_by_role("button", name="Permitir").click()
        # Acessa a página de ouvidoria
        page.get_by_role("link", name="Fale com a Ouvidoria", exact=True).click()
        page.get_by_role("link", name="Acessar").first.click()
        page.get_by_role("button", name="Fazer um elogio").click()
        page.get_by_role("radio", name="Identificado Ao selecionar").click()
        page.get_by_role("button", name="Continuar").click()
        page.locator(".css-13cymwt-control").click()
        page.get_by_role("option", name="Alistamento Eleitoral").click()
        page.get_by_role("button", name="Continuar").click()
        page.get_by_role("combobox", name="Selecionar assunto *").click()
        page.get_by_role("option", name="Atendimento", exact=True).click()
        page.get_by_role("textbox", name="Descrição *").fill("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        page.get_by_role("button", name="Continuar").click()
        page.get_by_role("textbox", name="CEP").click()
        page.get_by_role("textbox", name="CEP").fill("76820-888")
        time.sleep(2)
        page.get_by_role("textbox", name="Número").click()
        page.get_by_role("textbox", name="Número").fill("2470")
        page.get_by_role("button", name="Continuar").click()
        page.get_by_role("button", name="Tudo certo, enviar!").click()


        video_path = page.video.path()
        print("Vídeo salvo em:", video_path)

        time.sleep(2)
        context.close() # Fecha o contexto de gravação de vídeo
        browser.close()




