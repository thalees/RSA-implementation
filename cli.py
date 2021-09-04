import click
import six

from termcolor import colored
from pyfiglet import figlet_format

from rsa_implementation import (generate_key_pairs, encrypt, dencrypt, save_keys, get_keys_from_file)

from PyInquirer import (Token, prompt, style_from_dict)

style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})

def log(string, color="yellow", font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)

def ask(questions):
    return prompt(questions, style=style)

def ask_rsa_informations(): 
    return ask([
        {
            'type': 'list',
            'name': 'method',
            'message': 'Would you like to encrypt or decrypt?',
            'choices': ['Encrypt', 'Decrypt'],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'input',
            'name': 'message',
            'message': 'Type a message:',
        }
    ])

def ask_save_keys(): 
    return ask([
        {
            'type': 'confirm',
            'name': 'save',
            'message': 'Do you want to save the public and private key that were generated?'
        }
    ])

def ask_use_keys(): 
    return ask([
        {
            'type': 'confirm',
            'name': 'option',
            'message': 'Do you want to use the previously generated public and private keys?'
        }
    ])

@click.command()
def main():
    """
    RSA Algorithm Implementation with CLI
    """
    
    public_key = ""
    private_key = ""

    log("RSA Implementation", color="blue", figlet=True)
    log("Welcome to RSA Algorithm Implementation", color="green")

    if ask_use_keys().get("option", False):
        public_key, private_key = get_keys_from_file()
    else:
        public_key, private_key = generate_key_pairs() 
        if ask_save_keys().get("save", False):
            save_keys(public_key, private_key)

    rsa_options = ask_rsa_informations()

    message = rsa_options.get("message")
    
    if rsa_options.get("method") == "encrypt":
        text = encrypt(message, public_key)
        log(f'ecrypted = {text}')
        # log(f"ecrypted = {''.join(map(lambda x: str(x), text))}")
    else:

        text = dencrypt(message, private_key)
        log(f'decrypted = {text}')

if __name__ == '__main__':
    main()
