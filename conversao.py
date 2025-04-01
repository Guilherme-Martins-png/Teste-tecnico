import pandas as pd
import re
import zipfile
import os

def extrair_e_formatar_tabela(caminho_pdf, seu_nome):
    """
    Função principal para extrair, formatar e salvar a tabela de procedimentos
    """
    try:
        # 1. Extrair os dados brutos do PDF
        dados_brutos = extrair_dados_pdf("Downloads_NS\Anexo_I.pdf")
        
        # 2. Criar DataFrame e limpar os dados
        df = criar_dataframe(dados_brutos)
        
        # 3. Substituir abreviações
        df = substituir_abreviacoes(df)
        
        # 4. Salvar em CSV e compactar
        salvar_compactar(df, seu_nome)
        
        print("Processo concluído com sucesso!")
        return True
    
    except Exception as e:
        print(f"Erro: {str(e)}")
        return False

import pdfplumber

def extrair_dados_pdf(caminho_pdf):
    dados = []
    
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            tabela = pagina.extract_table()
            if tabela:
                # Pula o cabeçalho se já tiver sido identificado
                if not dados and len(tabela) > 1:
                    dados.extend(tabela[1:])  # Pula a primeira linha (cabeçalho)
                else:
                    dados.extend(tabela)
    
    return dados

def criar_dataframe(dados_brutos):

    #Criando DataFrame e limpa os dados

    colunas = [
        "PROCEDIMENTO", "RN (intervalo)", "VIGÊNCIA", "OD", "AMB", "NCO", "HSO", 
        "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
    ]
    
    df = pd.DataFrame(dados_brutos, columns=colunas)
    
    # Limpeza básica dos dados
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    df.replace({"": pd.NA, " ": pd.NA}, inplace=True)
    
    return df

def substituir_abreviacoes(df):

    #Substitui as abreviações conforme a legenda
    
    substituicoes = {
        "OD": "Odontológico",
        "AMB": "Ambulatorial",

    }
    
    # Substitui nas colunas específicas
    for col in ["OD", "AMB"]:
        if col in df.columns:
            df[col] = df[col].replace(substituicoes)
    
    return df

def salvar_compactar(df, seu_nome):
   
    #Salvando CSV
    os.makedirs("Transformaçao_de_dados", exist_ok=True)
    
    # Nome do arquivo CSV
    nome_csv = os.path.join("Transformaçao_de_dados", "procedimentos_saude.csv")
    
    # Salva o CSV
    df.to_csv(nome_csv, index=False, encoding='utf-8-sig', sep=';')
    
    #Nome do ZIP
    nome_zip = os.path.join("Transformaçao_de_dados", f"Teste_{seu_nome}.zip")
    
    # Compacta o CSV
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(nome_csv, os.path.basename(nome_csv))
    
   
    os.remove(nome_csv)
    
    print(f"Arquivo gerado: {nome_zip}")

if __name__ == "__main__":
    caminho_pdf = "Anexo_I.pdf"
    seu_nome = "Guilherme"  
    
    extrair_e_formatar_tabela(caminho_pdf, seu_nome)