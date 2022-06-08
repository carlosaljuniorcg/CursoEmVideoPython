def notas(*n, sit=False):
    """
    -> Funçào para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas do alunos (aceita várias).
    :param sit: (Opcional) Indica se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'

    return r

#Programas principal
resp = notas(4.5, 5.2, 5, 8.3, sit=True)
print(resp)
help(notas)