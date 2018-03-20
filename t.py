import requests
from lxml import html

session_requests = requests.session()
login_url = "https://213.27.202.18/remote/login?lang=en"

result = session_requests.get(login_url)
