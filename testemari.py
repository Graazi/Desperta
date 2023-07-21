import speech_recognition as sr

# Inicializa o reconhecedor de fala
r = sr.Recognizer()

# Define as palavras-chave que você deseja reconhecer
palavras_chave = ["Socorro"]

# Função para o reconhecimento de palavras-chave
def reconhecer_palavras_chave():
    with sr.Microphone() as source:
        print("Aguardando comando...")
        while True:
            audio = r.listen(source)
 
            try:
                # Utiliza o reconhecedor de fala para obter o texto do áudio
                texto = r.recognize_google(audio, language='pt-BR')
                print("Você disse:", texto)

                # Verifica se alguma palavra-chave foi detectada
                for palavra in palavras_chave:
                    if palavra in texto:
                        print("Palavra-chave detectada:", palavra)
                        print("Em perigo!")

            except sr.UnknownValueError:
                print("Não foi possível entender o áudio.")
            except sr.RequestError as e:
                print("Erro ao obter resultados do serviço de reconhecimento de fala:", str(e))

# Executa a função para o reconhecimento de palavras-chave
reconhecer_palavras_chave()
