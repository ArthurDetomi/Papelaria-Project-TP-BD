from termcolor import colored

def get_int(msg : str, min = None, max = None, max_msg=f"Valor deve ser menor ou igual a {max}.") -> int:
    value = 0

    while True:
        try:
            value = int(input(colored(msg, 'green')))

            if min is not None and value < min:
                print(colored(f"Valor deve ser maior ou igual a {min}.", 'red', attrs=['bold']))
                continue

            if max is not None and value > max:
                print(colored(max_msg, 'red', attrs=['bold']))
                continue

            break
        except ValueError as e:
            print(colored("Valor inválido! Por favor, digite um número inteiro.", 'red', attrs=['bold']))
            continue

    return value

def get_float(msg : str, min, max) -> float:
    value = 0

    while True:
        try:
            value = float(input(msg))

            if min is not None and value < min:
                print(colored(f"Valor deve ser maior ou igual a {min}.", 'red', attrs=['bold']))
                continue

            if max is not None and value > max:
                print(colored(f"Valor deve ser menor ou igual a {max}.", 'red', attrs=['bold']))
                continue

            break
        except ValueError as e:
            print(colored("Valor inválido! Por favor, digite um número inteiro.", 'red', attrs=['bold']))
            continue

    return value

