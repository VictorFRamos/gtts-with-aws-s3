# gtts-with-aws-s3

Português:

Este projeto é uma aplicação lambda em que o usuário envia um texto, audio é gerado e enviado para um nucket no s3 de forma simples e descomplicada.

English:

This project is a lambda application in which the user sends a text, audio is generated and sent to a nucket on s3 in a simple and uncomplicated way.


Example:

``` json
{
  "idioma": "português",
  "caminho": "textToSpeech/teste.mp3",
  "texto": "Era uma vez...um menininho simples, de uma região simples, morando em uma casa simples, nascido em uma família simples.Era a simplicidade em pessoa.Seu nome: SIMPLESMENTE.Sim, isso mesmo: SIMPLESMENTE.Era um garotinho ingênuo, singelo, bem natural, espontâneo."
}
```

References:

https://pypi.org/project/gTTS/

https://docs.aws.amazon.com/pt_br/lambda/latest/dg/lambda-python.html

