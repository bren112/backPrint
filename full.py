from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from supabase import create_client, Client
from datetime import datetime
from flask_cors import CORS

# Configuração do Supabase
SUPABASE_URL = "https://yswtmpgzhxiizyoccpex.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inlzd3RtcGd6aHhpaXp5b2NjcGV4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIwNTAzNjEsImV4cCI6MjA1NzYyNjM2MX0.-2jY8ghCQmBy0mrVfWu5rFnRsYlQBs5hYBlQ2-5a7fA"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)
CORS(app)

# Função para obter valor do AlmoxidAgro
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def obter_valor_almoxid():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.102/"
        driver.get(url)
        time.sleep(3)  

       
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

      
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

  
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído: {valor_ultima_celula}")  

        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do almoxidAgro: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()


# Função para obter valor do Administrativo
def obter_valor():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.90"  # URL do administrativo
        driver.get(url)

        # Login
        driver.find_element(By.ID, "i0019").send_keys("1234")
        driver.find_element(By.ID, "i2101").send_keys("1234")
        driver.find_element(By.ID, "submitButton").click()

        # Navegação
        driver.find_element(By.CLASS_NAME, "Standby").click()
        driver.find_element(By.LINK_TEXT, "Verificar Contador").click()

        valor_td = driver.find_element(By.XPATH, '//tr[th[contains(text(), "101: Total 1")]]/td').text
        valor_int = int(valor_td.replace(",", "").strip())

        link_log_trabalho = driver.find_element(By.LINK_TEXT, "Log do Trabalho")
        link_log_trabalho.click()

        tabela = driver.find_element(By.XPATH, '//div[@class="ItemListComponent"]/table')
        linhas = tabela.find_elements(By.XPATH, './/tbody/tr')

        if linhas:
            primeira_linha = linhas[0]  # Pega a primeira linha
            celulas = primeira_linha.find_elements(By.TAG_NAME, 'td')

            if len(celulas) > 6:
                primeiro_nome_usuario = celulas[6].text
                return valor_int, primeiro_nome_usuario
            else:
                print("A primeira linha não tem células suficientes.")
        else:
            print("A tabela não contém linhas.")

    except Exception as e:
        return None, None  

    finally:
        driver.quit()

# Função para obter valor do RH
def obter_valor_rh():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.113"  # URL do RH
        driver.get(url)

        # Login
        driver.find_element(By.ID, "i0019").send_keys("1234")
        driver.find_element(By.ID, "i2101").send_keys("1234")
        driver.find_element(By.ID, "submitButton").click()

        # Navegação
        driver.find_element(By.CLASS_NAME, "Standby").click()
        driver.find_element(By.LINK_TEXT, "Verificar Contador").click()

        valor_td = driver.find_element(By.XPATH, '//tr[th[contains(text(), "101: Total 1")]]/td').text
        valor_int = int(valor_td.replace(",", "").strip())

        link_log_trabalho = driver.find_element(By.LINK_TEXT, "Log do Trabalho")
        link_log_trabalho.click()

        tabela = driver.find_element(By.XPATH, '//div[@class="ItemListComponent"]/table')
        linhas = tabela.find_elements(By.XPATH, './/tbody/tr')

        if linhas:
            primeira_linha = linhas[0]  # Pega a primeira linha
            celulas = primeira_linha.find_elements(By.TAG_NAME, 'td')

            if len(celulas) > 6:
                primeiro_nome_usuario = celulas[6].text
                return valor_int, primeiro_nome_usuario
            else:
                print("A primeira linha não tem células suficientes.")
        else:
            print("A tabela não contém linhas.")

    except Exception as e:
        return None, None  

    finally:
        driver.quit()


# Função para obter valor do setor agrícola
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def obter_valor_agricola():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.101/"  # Novo IP para o setor agrícola
        driver.get(url)
        time.sleep(3)  

        # Clique no botão de informações
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        # Abre a seção "Contadores de uso"
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        # Captura o valor da célula específica
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor Agrícola): {valor_ultima_celula}")  

        # Converte para inteiro, removendo vírgulas e espaços
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor agrícola: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()


# Função para obter valor do setor Refeitório
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def obter_valor_refeitorio():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.112/"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor Refeitório): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor refeitório: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()


# Função para obter valor do Juridico
def obter_valor_juridico():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.109"  # URL do Juridico
        driver.get(url)

        # Login
        driver.find_element(By.ID, "i0019").send_keys("1234")
        driver.find_element(By.ID, "i2101").send_keys("1234")
        driver.find_element(By.ID, "submitButton").click()

        # Navegação
        driver.find_element(By.CLASS_NAME, "Standby").click()
        driver.find_element(By.LINK_TEXT, "Verificar Contador").click()

        valor_td = driver.find_element(By.XPATH, '//tr[th[contains(text(), "101: Total 1")]]/td').text
        valor_int = int(valor_td.replace(",", "").strip())

        link_log_trabalho = driver.find_element(By.LINK_TEXT, "Log do Trabalho")
        link_log_trabalho.click()

        tabela = driver.find_element(By.XPATH, '//div[@class="ItemListComponent"]/table')
        linhas = tabela.find_elements(By.XPATH, './/tbody/tr')

        if linhas:
            primeira_linha = linhas[0]  # Pega a primeira linha
            celulas = primeira_linha.find_elements(By.TAG_NAME, 'td')

            if len(celulas) > 6:
                primeiro_nome_usuario = celulas[6].text
                return valor_int, primeiro_nome_usuario
            else:
                print("A primeira linha não tem células suficientes.")
        else:
            print("A tabela não contém linhas.")

    except Exception as e:
        return None, None  

    finally:
        driver.quit()

# Função para obter valor do setor Enfermagem
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def obter_valor_enfermagem():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.106/"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor Enfermagem): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor Enfermagem: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()

# Função para obter valor do setor ALMOXIND

def obter_valor_almoxind():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.103/"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor AlmoxInd): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor AlmoxInd: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()
    

    # Função para obter valor do setor PCMI

# Função para obter valor do setor PCMI

def obter_valor_pcmi():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.111/"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor pcmi): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor pcmi: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()


    # Função para obter valor do setor LABORATORIO


# Função para obter valor do setor LABO

def obter_valor_labo():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.110/"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor LABORATORIO): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor LABORATORIO: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()

# Função para obter valor do setor FROTA

def obter_valor_frota():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.108/"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor FROTA): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor FROTA: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()

# Função para obter valor do setor FATURAMENTO

def obter_valor_faturamento():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.106/"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor Faturamento): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor Faturamento: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()

# Função para obter valor do setor SEG

def obter_valor_seg():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.114/sws/index.html"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor SEGTRAB): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor SEGTRAB: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()

# Função para obter valor do setor alc

# def obter_valor_alc():
    chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--no-sandbox")  
    chrome_options.add_argument("--disable-dev-shm-usage")  

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.set_window_position(-2000, 0)

        url = "http://10.10.1.104"  
        driver.get(url)
        time.sleep(3)  

        
        botao_informacao = driver.find_element(By.ID, "ext-gen249")
        botao_informacao.click()
        time.sleep(3)

        
        contadores_item = driver.find_element(By.XPATH, "//span[text()='Contadores de uso']")
        contadores_item.click()
        time.sleep(3)

        
        valor_ultima_celula = driver.find_element(By.XPATH, "(//table[contains(@class, 'x-grid3-row-table')]//tr)[3]//td[last()]//div").text
        print(f"Valor extraído (Setor Carreg.Álcool): {valor_ultima_celula}")  

       
        valor_int = int(valor_ultima_celula.replace(",", "").strip())
        
        return valor_int

    except Exception as e:
        print(f"Erro ao obter valor do setor Carreg.Álcool: {e}")
        return None

    finally:
        time.sleep(2)  
        driver.quit()


# Função para salvar os dados no banco
def salvar_no_banco(nome, prints, usuario, id_impressora):
    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    existing_data = supabase.table("impressoras").select("*").eq("id", id_impressora).execute()

    if existing_data.data:
        # Se já existir, atualize os dados
        response = supabase.table("impressoras").update({
            "nome": nome,
            "prints": prints,
            "data_atual": data_atual,
            "ult": usuario  
        }).eq("id", id_impressora).execute()
    else:
        # Se não existir, insira um novo registro
        response = supabase.table("impressoras").insert({
            "id": id_impressora,  # Garantindo que o id seja o correto
            "nome": nome,
            "prints": prints,
            "data_atual": data_atual,
            "ult": usuario  
        }).execute()

    return response

# Função para obter dados do banco
def obter_dados_banco(id_impressora):
    response = supabase.table("impressoras").select("*").eq("id", id_impressora).execute()
    if response.data:
        return response.data[0]
    return None

# Rota da API para Almoxid Agro
@app.route('/almoxidagro', methods=['GET'])
def almoxidagro():
    valor_almoxid = obter_valor_almoxid()

    if valor_almoxid is not None:
        salvar_no_banco("Impressora Almoxid Agro", valor_almoxid, "Não Suporta", 2)

    informacoes_banco = obter_dados_banco(2)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

# Rota da API para Impressora Administrativo
@app.route('/dados', methods=['GET'])
def dados():
    valor, usuario = obter_valor()

    if valor is not None and usuario is not None:
        salvar_no_banco("Impressora Administrativo", valor, usuario, 1)

    dados_banco = obter_dados_banco(1)
    if dados_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": dados_banco['prints'],
            "nome": dados_banco['nome'],
            "data_atual": dados_banco['data_atual'],
            "ult": dados_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

# Rota da API para Impressora RH
@app.route('/rh', methods=['GET'])
def rh():
    valor_rh, usuario_rh = obter_valor_rh()  # Obtém o valor e o usuário da impressora RH

    if valor_rh is not None and usuario_rh is not None:
        salvar_no_banco("Impressora RH", valor_rh, usuario_rh, 3)  # Salvando os dados corretamente no banco

    informacoes_banco = obter_dados_banco(3)  # Obtendo os dados da impressora RH
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário que utilizou a impressora
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

# Rota da API para o Setor Agrícola
@app.route('/agricola', methods=['GET'])
def agricola():
    valor_agricola = obter_valor_agricola()

    if valor_agricola is not None:
        salvar_no_banco("Impressora Setor Agrícola", valor_agricola, "Não Suporta", 4)

    informacoes_banco = obter_dados_banco(4)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

# Rota da API para o Setor Refeitório
@app.route('/refeitorio', methods=['GET'])
def refeitorio():
    valor_refeitorio = obter_valor_refeitorio()

    if valor_refeitorio is not None:
        salvar_no_banco("Impressora Setor Refeitório", valor_refeitorio, "Não Suporta", 5)

    informacoes_banco = obter_dados_banco(5)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500



        # Rota da API para Impressora RH


@app.route('/juridico', methods=['GET'])
def juridico():
    valor_juridico, usuario_juridico = obter_valor_juridico()  

    if valor_juridico is not None and usuario_juridico is not None:
        salvar_no_banco("Impressora Juridico", valor_juridico, usuario_juridico, 6)  # Salvando os dados corretamente no banco

    informacoes_banco = obter_dados_banco(6)  
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário que utilizou a impressora
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

# Rota da API para o Setor Enfermagem
@app.route('/enfermagem', methods=['GET'])
def enfermagem():
    valor_enfermagem = obter_valor_enfermagem()

    if valor_enfermagem is not None:
        salvar_no_banco("Impressora Setor Enfermagem", valor_enfermagem, "Não Suporta", 7)

    informacoes_banco = obter_dados_banco(7)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

# Rota da API para o Setor Almoxind
@app.route('/almoxind', methods=['GET'])
def almoxind():
    valor_almoxind = obter_valor_almoxind()

    if valor_almoxind is not None:
        salvar_no_banco("Impressora Setor Almoxarifado", valor_almoxind, "Não Suporta", 8)

    informacoes_banco = obter_dados_banco(8)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

@app.route('/pcmi', methods=['GET'])
def pcmi():
    valor_pcmi = obter_valor_pcmi()

    if valor_pcmi is not None:
        salvar_no_banco("Impressora Setor PCMI", valor_pcmi, "Não Suporta", 9)

    informacoes_banco = obter_dados_banco(9)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

@app.route('/labo', methods=['GET'])
def labo():
    valor_labo = obter_valor_labo()

    if valor_labo is not None:
        salvar_no_banco("Impressora Setor Laboratório", valor_labo, "Não Suporta", 10)

    informacoes_banco = obter_dados_banco(10)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

@app.route('/frota', methods=['GET'])
def frota():
    valor_frota = obter_valor_frota()

    if valor_frota is not None:
        salvar_no_banco("Impressora Setor Frota", valor_frota, "Não Suporta", 11)

    informacoes_banco = obter_dados_banco(11)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

@app.route('/fatu', methods=['GET'])
def faturamento():
    valor_faturamento = obter_valor_faturamento()

    if valor_faturamento is not None:
        salvar_no_banco("Impressora Setor Faturamento", valor_faturamento, "Não Suporta", 12)

    informacoes_banco = obter_dados_banco(12)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

@app.route('/seg', methods=['GET'])
def seg():
    valor_seg = obter_valor_seg()

    if valor_seg is not None:
        salvar_no_banco("Impressora Setor SEGTRAB   ", valor_seg, "Não Suporta", 13)

    informacoes_banco = obter_dados_banco(13)
    if informacoes_banco:
        return jsonify({
            "mensagem": "Dados do banco recuperados com sucesso",
            "numero": informacoes_banco['prints'],
            "nome": informacoes_banco['nome'],
            "data_atual": informacoes_banco['data_atual'],
            "ult": informacoes_banco['ult']  # Último usuário
        })
    else:
        return jsonify({
            "mensagem": "Nenhum dado encontrado no banco."
        }), 500

# @app.route('/alc', methods=['GET'])
# def alc():
#     valor_alc = obter_valor_alc()

#     if valor_alc is not None:
#         salvar_no_banco("Impressora Setor Carreg.Álcool", valor_alc, "Não Suporta", 14)

#     informacoes_banco = obter_dados_banco(14)
#     if informacoes_banco:
#         return jsonify({
#             "mensagem": "Dados do banco recuperados com sucesso",
#             "numero": informacoes_banco['prints'],
#             "nome": informacoes_banco['nome'],
#             "data_atual": informacoes_banco['data_atual'],
#             "ult": informacoes_banco['ult']  # Último usuário
#         })
#     else:
#         return jsonify({
#             "mensagem": "Nenhum dado encontrado no banco."
#         }), 500

@app.route('/', methods=['GET'])
def impressora():
    return "Funcionando"

if __name__ == '__main__':
    app.run(debug=True, port=1000)
