# our main file.

import speech_recognition as sr

# Criar um reconhecedor
r = sr.Recognizer()

# Abrir o microfone para captura
with sr.Microfone() as source:
  audio =  r.listen(source) # Define microfone como fonte de áudio

    print(r.recognize_google(audio))
