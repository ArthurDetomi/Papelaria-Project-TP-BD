"""Módulo NumberUtil.

Contém funções utilitárias para a leitura e validação de números inteiros e reais.
"""

from termcolor import colored


def get_int(msg: str, min=None, max=None, max_msg=None) -> int:
    """
    Solicita a entrada de um número inteiro, validando os limites.

    :param msg: Mensagem exibida para solicitar o número.
    :param min: Valor mínimo permitido (opcional).
    :param max: Valor máximo permitido (opcional).
    :param max_msg: Mensagem a ser exibida se o valor exceder o máximo.
                      Se não fornecida, uma mensagem padrão será utilizada.
    :return: Número inteiro inserido pelo usuário.
    """
    if max_msg is None:
        max_msg = f"Valor deve ser menor ou igual a {max}." if max is not None else "Valor excedido."

    while True:
        try:
            value = int(input(colored(msg, 'green')))
            if min is not None and value < min:
                print(colored(f"Valor deve ser maior ou igual a {min}.", 'red', attrs=['bold']))
                continue
            if max is not None and value > max:
                print(colored(max_msg, 'red', attrs=['bold']))
                continue
            return value
        except ValueError:
            print(colored("Valor inválido! Por favor, digite um número inteiro.", 'red', attrs=['bold']))


def get_float(msg: str, min=None, max=None) -> float:
    """
    Solicita a entrada de um número real (float), validando os limites.

    :param msg: Mensagem exibida para solicitar o número.
    :param min: Valor mínimo permitido.
    :param max: Valor máximo permitido.
    :return: Número real inserido pelo usuário.
    """
    while True:
        try:
            value = float(input(msg))
            if min is not None and value < min:
                print(colored(f"Valor deve ser maior ou igual a {min}.", 'red', attrs=['bold']))
                continue
            if max is not None and value > max:
                print(colored(f"Valor deve ser menor ou igual a {max}.", 'red', attrs=['bold']))
                continue
            return value
        except ValueError:
            print(colored("Valor inválido! Por favor, digite um número real.", 'red', attrs=['bold']))
