"""
Código desenvolvido como complemento ao tutorial
de uso de Py Auto GUI para criação de RPA
Aulas em vídeo disponíveis no canal Python DS:
https://www.youtube.com/playlist?list=PL0XxTDj23A1H-1NxZiOVKkMeCS44EIxih
"""
import pyautogui
import os
import cv2

from time import sleep

#Configurações do experimento
#Substitua a linha abaixo pelo seu diretório de trabalho
caminho = r'C:\Users\p527488\Downloads\PycharmProjects\pythonProject'
os.chdir(caminho)
global local

#Substitua a linha abaixo pelo nome da imagem a ser localizada
arquivo = 'C:\\Users\\p527488\\Downloads\\PycharmProjects\\pythonProject\\box2.PNG'

#Variáveis para controle da condição de parada
k = 0
n = 50

while True:
    print ("Procura a imagem")
    #local = pyautogui.locateCenterOnScreen(arquivo)

    try:
        local = pyautogui.locateOnScreen(arquivo, confidence=0.8, grayscale=True)
        print('Found it!')
        # Se imagem for localizada
        if local != None:
            pyautogui.moveTo(local)
            pyautogui.click()
            print(f'Imagem localizada na posiçõa: {local}')
            break
    except:
        pass



    #Após n tentativas o programa encerra
    if k >= n:
        print('Imagem não localizada')
        break

    #Aguarda um pouco para tentar novamente
    sleep(0.25)
    k += 1
