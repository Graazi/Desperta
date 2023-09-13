# Desperta

O código em Python utiliza a biblioteca SpeechRecognition para ouvir a entrada de áudio de um microfone e converte essa entrada de áudio em texto e, se a palavra que foi falada estiver contida na lista, envia um e-mail de alerta. Aqui está uma explicação detalhada do código:

1. Importação de Bibliotecas:
   - O código começa importando as bibliotecas necessárias:
     - `speech_recognition` (importada como `sr`): Esta biblioteca é usada para reconhecimento de fala.
     - `pyaudio`: Esta biblioteca é usada para interagir com o dispositivo de áudio do computador, permitindo a gravação de áudio.
     - `smtplib`: Esta biblioteca é usada para enviar e-mails.

2. Criação de lista:
   - Criar lista com palavras chave de assédio e violência.
   - Perguntar se a lista contém aquilo que foi falado.

3. Definição da Função `abrir_microfone`:
   - Esta função é responsável por abrir o microfone, capturar a entrada de áudio e convertê-la em texto.
   - Usa o `Recognizer` da biblioteca SpeechRecognition para reconhecimento de fala.
   - Ajusta automaticamente o reconhecimento para o ruído ambiente.
   - Captura a entrada de áudio com um microfone.
   - Tenta reconhecer a fala usando o Google Speech Recognition em português.
   - Se a fala for reconhecida com sucesso, imprime o texto reconhecido e retorna o texto. Caso contrário, imprime uma mensagem de erro.

4. Definição da Função `enviar_email`:
   - Esta função é usada para enviar um e-mail de alerta.
   - Define o corpo do e-mail em formato HTML.
   - Cria um objeto de mensagem de e-mail, configura o assunto, remetente e destinatário.
   - Define a senha da conta de e-mail do remetente (deve ser substituída pela senha real).
   - Configura o cabeçalho do e-mail como texto HTML e define o corpo do e-mail.
   - Estabelece uma conexão com o servidor SMTP do Gmail e envia o e-mail para o destinatário.
   - Imprime uma mensagem de confirmação após o envio do e-mail.

5. Função `main`:
   - Entra em um loop infinito que permite ao usuário escolher entre duas opções:
     - Abrir o microfone (opção 1): Isso chama a função `abrir_microfone`.
       - Se a palavra que for detectada na fala estiver contida na lista, a função `enviar_email` é chamada para enviar um e-mail de alerta.
     - Sair do programa (opção 2).
   - Qualquer outra opção digitada resultará em uma mensagem de "Opção inválida".

6. Execução do Programa:
   - O programa inicia a execução chamando a função `main()` dentro de um bloco `if __name__ == "__main__"`.
   - O programa continuará em execução até que o usuário escolha a opção 2 (Sair).

Certifique-se de que as bibliotecas mencionadas no início do código estão instaladas no seu ambiente Python.
