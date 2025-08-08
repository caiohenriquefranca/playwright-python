Feature: Login no sistema

  Scenario: Usuário acessa com sucesso
    Given que o usuário está na página de login
    When ele preenche os dados corretos
    Then ele deve ver a página de admin
