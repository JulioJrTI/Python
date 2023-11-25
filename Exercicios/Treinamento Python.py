def notas(*n,sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com varias informações sobre a situação da turma.
    """
    
    r = dict()

    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n) / len(n)

    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Media'] >= 5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'

    return r

#Programa principal
resp=notas(5.5,1.2,sit=True)
print(resp)
help(notas) 