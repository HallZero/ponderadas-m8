import re

def vai_para_ponto(x):
    print("Indo ali: ", x)


intencoes = {
    r"\b[Vv][áa](?:\spara)?\s?[oa]?\s(.+)": "destino",
    r"\b[Dd][i]r[íi]ja-se\s[aao]?\s?(.+)": "destino",
    r"\b[Mm]e\s?[lL]eve(?:-me)?\s?[aaopara]?\s?(.+)": "destino"
}

acoes = {
    "destino": vai_para_ponto
}
def main():
    comando = input("Digite ser comando: ")

    for chave, valor in intencoes.items():
        pattern = re.compile(chave)
        grupos = pattern.findall(comando)
        if grupos:
            print(grupos)
            acoes[valor](grupos[0])

if __name__ == '__main__':
    main()