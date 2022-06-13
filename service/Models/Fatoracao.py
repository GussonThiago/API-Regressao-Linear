def fat(num, show=False):
    """
    -> Realiza o calculo do fatorial de um número
    :param num: Número para realizar os calculos
    :param show: (opcional) Exibir ou não os calculos
    :return: O valor do fatorial de um número n
    """
    f = 1
    numero = int(num)
    for c in range(numero, 0, -1):
        if show:
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
        f = f * c
        n = str(f)
    return n
