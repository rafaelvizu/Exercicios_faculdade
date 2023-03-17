from models.services import Services
from views.Dados import Dados


df = Services.read()

Dados(Services.read())
