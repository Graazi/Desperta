#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install SpeechRecognition')
get_ipython().system('pip install PyAudio')
get_ipython().system('pip install secure-smtplib')


# In[4]:


import speech_recognition as sr
import pyaudio
import smtplib
import email.message

def abrir_microfone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, fale alguma coisa!!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse: " + texto)
        return texto
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala.")
    except sr.RequestError as e:
        print("Erro ao conectar-se ao serviço de reconhecimento de fala: {0}".format(e))

    return None

def enviar_email():
    corpo_email = """
    <p>Prezados, </p>
    <p>Socorro! Alguma coisa está errada.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Socorro!"
    msg['From'] = "milenia.00000847231@unicap.br"
    msg['To'] = "rosendomilenia4@gmail.com"
    password = "slbklazbctfzsthb"  # senha do email do remetente gerada pelo Google
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

def main():
    while True:
        opcao = input("Escolha uma opção:\n1. Abrir microfone\n2. Sair\n")

        if opcao == "1":
            texto_falado = abrir_microfone()
            if texto_falado:
                print("Texto falado: " + texto_falado)
                if "socorro" in texto_falado.lower():
                    enviar_email()
            else:
                print("Não foi possível reconhecer a fala.")
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()


# In[ ]:
