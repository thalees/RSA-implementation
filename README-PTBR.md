# Implementação RSA <a align="right"><img align="right" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python"></a>


> Implementação simples da lógica  RSA usando puro Python 🔑

<p align="center">
  <a href="#conceito">Conceito</a> • 
  <a href="#instalação-e-requisitos">Instalação e Requisitos</a> • 
  <a href="#como-executar">Como executar</a> •  
  <a href="#testes">Testes</a> • 
  <a href="#licença">Licença</a> •
  <a href="README.md">EN</a>
</p>

## Conceito

O algoritmo RSA se trata de uma criptografia assimétrica; isso significa que ele usa uma chave pública e uma chave privada (ou seja, duas chaves diferentes, matematicamente ligadas). Como seus nomes sugerem, a chave pública é pubicamente compartilhada, enquanto a chave privada é secreta e não deve ser compartilhada com ninguém.

O algoritmo RSA tem o nome daqueles que o inventaram em 1978: ROn Rivest, Adi Shamir e Leonard Adleman.


### Gerando as chaves

1. Selecione dois numeros primos grandes, x e y. Os números primos precisam ser grandes para que seja difícil para alguém decifrá-los.
2. Calcule n = x * y
3. Calcule a função totiet: ϕ(n) = (x−1)*(y−1)
4. Selecione um inteiro *e*, de tal forma que *e* seja co-primo de ϕ(n) e 1 < *e* < ϕ(n). O par de números (n,*e*) constitui a chave pública..
> Dois inteiros são primos se o único inteiro positivo que os divide for 1.

5. Calcule `d` de modo que `e.d = 1 mod ϕ(n)`

**TRANSLATE HERE: Add can be found using the extended euclidean algorithm. The pair (n,d) makes up the private key.**

### Criptografia

Dado um texto simple P, representado como um número, o texto cifrado C é calculado como:

`
C = P^e mod n
`

### Decriptografia
Usando a chave privada (n, d), o texto simples pode ser encontrado usando:

`
P = C^d mod n
`

## Instalação e Requisitos

Essas instruções fornecerão uma cópia do projeto instalado e funcionando em sua máquina local para desenvolvimento. Antes de instalar a aplicação, nós precisamos  dessas ferramentas conifiguradas e instaladas:

- [Python 3.8](https://www.python.org/downloads/)

É bem fácil instalar e fazer o upload do aplicativo. Basta seguir os passos abaixo e tudo ficará bem! 🎉

### Aplicação

Inicialmente, faça o download do projeto:
```
git clone https://github.com/thalees/RSA-implementation.git
cd RSA-implementation
```

Após clonar esse repositório, crie um virtualenv e o ative:
```
python -m virtualenv venv && . venv/bin/activate
```

Finalmente instale as dependências necessárias
```
pip install -r requirements.txt
```

## Como executar

Depois de realizar a configuração inicial, basta executar o aplicativo:

```
python cli.py
```

![Application Gif](application.gif)

## Testes

Para executar os testes, apenas execute o comando abaixo:

```
pytest rsa_implementation_test.py
```

## Licença

Esse projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

---
<p align="center"><b>Obrigado 🎉</b></p>
<p align="center">
  <img width="100" height="100" alt="bye" src="https://media.giphy.com/media/JO3FKwP5Fwx44uMfDI/giphy.gif">
</p>
