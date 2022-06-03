# -*- coding: utf-8 -*-
# https://gtts.readthedocs.io/en/latest/index.html
import json
from gtts import gTTS
import boto3
import re
import os

s3 = boto3.client('s3', aws_access_key_id=os.environ.get(
    'ACCESS_KEY'), aws_secret_access_key=os.environ.get('SECRET_ACCESS'))
language = ''
tldCustom = ''
naoDisponivel = ''


def lambda_handler(event, context):
    texto = event['texto'].strip()
    verificarIdioma(event['idioma'], texto, event['caminho'])
    return {
        'statusCode': 200,
        'body': json.dumps('sucesso')
    }


def verificarIdioma(idioma, texto, caminho):
    try:
     print('idioma: ' + idioma + ', texto: ' + texto + ', caminho: ' + caminho)
     if idioma == 'inglês' or idioma == 'english':
         language = 'en'
         tldCustom = 'com'
         naoDisponivel = 'Audio not available for this page!'
     elif idioma == 'espanhol' or idioma == 'spanish':
         language = 'es'
         tldCustom = 'es'
         naoDisponivel = '¡Audio no disponible para esta página!'
     elif idioma == 'francês' or idioma == 'french':
         language = 'fr'
         tldCustom = 'fr'
         naoDisponivel = 'Audio non disponible pour cette page!'
     elif idioma == 'mandarim' or idioma == 'mandarin':
         language = 'zh-CN'
         tldCustom = 'com'
         naoDisponivel = '该页面没有音频!'
     else:
         language = 'pt'
         tldCustom = 'com.br'
         naoDisponivel = 'Áudio não disponível para essa página!'

     if texto == "":
        texto = naoDisponivel

     print('texto final: ' + texto)
     Processar(texto, caminho, tldCustom, language)
    except Exception as e:
        print(e)


def Processar(texto, caminho, tldCustom, language):
    texto = re.sub(r'(\<img alt=\")(.*?)(\")', r'\2', texto)
    tts = gTTS(text=texto, tld=tldCustom, lang=language)
    tts.save('/tmp/result.mp3')
    s3.upload_file('/tmp/result.mp3', os.environ.get('BUCKET'), caminho)
