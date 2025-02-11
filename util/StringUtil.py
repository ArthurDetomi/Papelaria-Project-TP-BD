"""Módulo StringUtil.

Contém funções utilitárias para manipulação de strings.
"""


def is_blank(s: str = "") -> bool:
    """
    Verifica se uma string está vazia ou contém apenas espaços em branco.

    :param s: String a ser verificada.
    :return: True se a string estiver vazia ou for composta apenas por espaços, False caso contrário.
    """
    return not s.strip()
