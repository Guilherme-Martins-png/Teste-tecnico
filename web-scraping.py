from bs4 import BeautifulSoup
import requests
from pathlib import Path
import zipfile

#Criando a pasta com arquivos 
PASTA = Path("Downloads_NS")
PASTA.mkdir(exist_ok=True)
BASE_URL = "https://www.gov.br"
url_pdf = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
caminho = PASTA / "Anexo_I.pdf"

resposta = requests.get (url_pdf, stream=True)
with open (caminho, 'wb') as arquivos:
    for chunk in resposta.iter_content(chunk_size=8192):
        arquivos.write(chunk)

#Extração dos dados da pagina 
HTML = requests.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos").content
soup = BeautifulSoup(HTML, 'html.parser')
arquivos_em_anexo_um = soup.find ("a" , href=lambda href: href and href.endswith('.pdf') , class_="internal-link") #Filtragem usando href
arquivos_em_anexo_dois = soup.find ("a" , string=lambda text: 'Anexo II' in str(text) , class_="internal-link") #Filtragem usando opção de texto

# Baixar Anexo I
if arquivos_em_anexo_um:
    link = arquivos_em_anexo_um['href']
    resposta = requests.get(link)
    with open(PASTA / "Anexo_I.pdf", 'wb') as f:
        f.write(resposta.content)
    print("Anexo I baixado!")

# Baixar Anexo II
if arquivos_em_anexo_dois:
    link = arquivos_em_anexo_dois['href']
    resposta = requests.get(link)
    with open(PASTA / "Anexo_II.pdf", 'wb') as f:
        f.write(resposta.content)
    print("Anexo II baixado!")

#compactando
with zipfile.ZipFile(PASTA / "Anexos.zip", 'w') as zipf:
    zipf.write(PASTA / "Anexo_I.pdf", "Anexo_I.pdf")
    zipf.write(PASTA / "Anexo_II.pdf", "Anexo_II.pdf")
print("ZIP criado!")