# RSA Implementation <a align="right"><img align="right" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python"></a>


> Simple implementation of RSA logic using pure python 🔑

<p align="center">
  <a href="#concept">Concept</a> • 
  <a href="#installation-and-requirements">Installation and Requirements</a> • 
  <a href="#how-to-run">How to run</a> •  
  <a href="#tests">Tests</a> • 
  <a href="#license">License</a> • 
  <a href="README-PTBR.md">pt-BR</a>
</p>

## Concecpt

The RSA algorithm is an asymmetric cryptography algorithm; this means that it uses a public key and a private key (i.e two different, mathematically linked keys). As their names suggest, a public key is shared publicly, while a private key is secret and must not be shared with anyone.

The RSA algorithm is named after those who invented it in 1978: Ron Rivest, Adi Shamir, and Leonard Adleman.

### Generating the keys

1. Select two large prime numbers, x and y. The prime numbers need to be large so that they will be difficult for someone to figure out.
2. Calculate n = x * y
3. Calculate the totient function: ϕ(n) = (x−1)*(y−1)
4. Select an integer *e*, such that *e* is co-prime to ϕ(n) and 1 < e < ϕ(n). The pair of numbers (n,e) makes up the public key.
> Two integers are co-prime if the only positive integer that divides them is 1.

5. Calculate `d` such that `e.d = 1 mod ϕ(n)`

The `d` can be found using the extended euclidean algorithm. The pair (n,d) makes up the private key.

### Encryption
Given a plaintext P, represented as a number, the ciphertext C is calculated as:

`C = P^e mod n`

### Decryption
Using the private key (n,d), the plaintext can be found using:

`P = C^d mod n`

## Installation and Requirements

These instructions will get you a copy of the project up and running on your local machine for development. Before we install the application we need these tools configured and installed:

- [Python 3.8](https://www.python.org/downloads/)

It is very easy to install and upload the application. Just follow the steps below and everything will be fine! 🎉

### Application

Initially download the project:
```
git clone https://github.com/thalees/RSA-implementation.git
cd RSA-implementation
```

After cloning that repository, create a virtualenv and activate:
```
python -m virtualenv venv && . venv/bin/activate
```

Finally install the necessary dependencies:
```
pip install -r requirements.txt
```

## How to run

After performing the initial setup, just run the application:
```
python cli.py
```
![Application Gif](application.gif)
## Tests

To run the tests, just run the command below:
```
pytest rsa_implementation_test.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
<p align="center"><b>Thanks 🎉</b></p>
<p align="center">
  <img width="100" height="100" alt="bye" src="https://media.giphy.com/media/JO3FKwP5Fwx44uMfDI/giphy.gif">
</p>
