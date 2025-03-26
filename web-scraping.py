from bs4 import BeautifulSoup
import requests


html = requests.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos").content
soup = BeautifulSoup(html, 'html.parser')

arquivos_em_anexo_um = soup.find ("a" , href=lambda href: href and href.endswith('.pdf') , class_="internal-link") #Filtragem usando href
arquivos_em_anexo_dois = soup.find ("a" , string=lambda text: 'Anexo II' in str(text) , class_="internal-link") #Filtragem usando opção de texto



print ( f'este é o arquivo numero um: {arquivos_em_anexo_um}')
print (f'este é o arquivo numero dois :{arquivos_em_anexo_dois}')