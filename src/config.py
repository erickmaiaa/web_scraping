SELENIUM_GRID_URL = 'http://localhost:4444'
TARGET_URL = 'https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx'

WAIT_TIMEOUT = 20  # Increased timeout for potentially slow loading

# --- XPaths ---
CONTEST_DATE_XPATH = '//*[@id="wp_resultados"]/div[1]/div/h2/span'
BALL_LIST_XPATH = '//*[@id="ulDezenas"]/li'  # Base XPath for list items
NEXT_BUTTON_XPATH = '//*[@id="wp_resultados"]/div[1]/div/div[2]/ul/li[2]/a'
# To ensure page loaded initially
BUSCA_CONCURSO_INPUT_XPATH = '//*[@id="buscaConcurso"]'
