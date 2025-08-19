import pyttsx3 #Biblioteca de text-to-speech
from PyPDF2 import PdfReader #Biblioteca permite manipular arquivos PDF
from tkinter.filedialog import askopenfilename #Biblioteca que cria uma janela para o usuário selecionar o arquivo PDF.

# Abre uma janela de diálogo para que o usuário escolha o arquivo PDF que deseja ler.
book = askopenfilename() 
# Cria um objeto reader do PdfReader para ler o arquivo PDF.
reader = PdfReader(book) 
# Armazena o número total de páginas do documento.
pages = len(reader.pages)

# Inicia um loop que percorre todas as páginas do PDF, de 0 até o número total de páginas menos um.
for num in range(pages):
    page = reader.pages[num] # Seleciona a página atual.
    text = page.extract_text() # Extrair o texto da página.

    # Verifica se a variável text não está vazia.
    if text:
        # Inicializa a fala.
        engine = pyttsx3.init()
        
        # Manda dizer o texto extraído da página.
        engine.say(text)

        #Inicia o processo de fala aguardando até que todo o texto da página seja lido antes de ir para a próxima.
        engine.runAndWait()
    # Se o text for vazio o programa imprime uma mensagem avisando que a página não pôde ser lida.
    else:
        print(f"Page {num + 1} is empty or could not be read.")
