from behave import given, when, then
from playwright.sync_api import sync_playwright, expect

@given('que o usuário está na página de login')
def step_impl(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto("https://admin.dev.govone.digital/")

@when('ele preenche os dados corretos')
def step_impl(context):
    context.page.locator("#username").type("25127127024")
    context.page.locator("#password").type("123Mudar")
    expect(context.page.locator("#submit-login")).to_be_enabled(timeout=10000)
    context.page.click("#submit-login")

@then('ele deve ver a página de admin')
def step_impl(context):
    assert "Gerenciamento" in context.page.title()
    context.browser.close()
    context.playwright.stop()