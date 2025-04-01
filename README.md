Descrição
Este projeto foi desenvolvido como parte de um desafio técnico, com o objetivo de automatizar a coleta e processamento de dados do Rol de Procedimentos em Saúde da ANS. Ele realiza:

Web Scraping para baixar arquivos PDF

Processamento de dados para extrair e estruturar tabelas

Geração de arquivos prontos para análise

🛠️ Funcionalidades
1. Web Scraping
Acessa o site da ANS e localiza os links dos Anexos I e II

Faz o download dos arquivos PDF

Compacta os PDFs em um arquivo ZIP

2. Processamento de Dados
Extrai tabelas de um PDF usando pdfplumber

Limpa e estrutura os dados em um DataFrame

Substitui abreviações (OD → Odontológico, AMB → Ambulatorial)

Salva os dados em CSV e compacta em um arquivo ZIP

⚙️ Como Executar
Pré-requisitos
Instale as bibliotecas
pip install requests beautifulsoup4 pandas pdfplumber

Execute os scripts:
python web_scraping.py     # Baixa os PDFs
python data_processing.py  # Processa os dados

Os arquivos finais serão gerados nas pastas:
Downloads_NS/Anexos.zip (PDFs baixados)

Transformaçao_de_dados/Teste_Guilherme.zip (dados processados)


Observações
O projeto foi desenvolvido com Python 3

Bibliotecas principais: requests, BeautifulSoup, pandas, pdfplumber

O código inclui tratamento básico de erros

O desafio está parcialmente completo
