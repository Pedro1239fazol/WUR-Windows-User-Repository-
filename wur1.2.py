import requests
import subprocess


PROGRAMS = {

    "TFiles": [

        {
            "versao": "0.2-1",
            "arquivo": "TFiles 0.2-1_Setup.exe",
            "url": "https://sourceforge.net/projects/tfiles/files/TFiles%200.2-1_Setup.exe/download"
        },

        {
            "versao": "0.1",
            "arquivo": "TFiles 0.1_Setup.exe",
            "url": "https://sourceforge.net/projects/tfiles/files/"
        }

    ],


    "MBrowser": [

        {
            "versao": "1.0 Estavel",
            "arquivo": "MBrowser_Setup.exe",
            "url": "https://sourceforge.net/projects/mbrowser/files/MBrowser_Setup.exe/download"
        }

    ],


    "Firefox": [

        {
            "versao": "Atual",
            "arquivo": "Firefox Setup.exe",
            "url": "https://download.mozilla.org/?product=firefox-latest&os=win64"
        }

    ],


    "Chrome": [

        {
            "versao": "Atual",
            "arquivo": "Chrome Setup.exe",
            "url": "https://dl.google.com/chrome/install/latest/chrome_installer.exe"
        }

    ]

}



def baixar(programa):

    print(
        "\nBaixando:",
        programa["arquivo"]
    )


    resposta = requests.get(
        programa["url"],
        headers={
            "User-Agent": "WUR/1.0"
        },
        allow_redirects=True
    )


    with open(
        programa["arquivo"],
        "wb"
    ) as arquivo:

        arquivo.write(
            resposta.content
        )


    print(
        "Download concluído!"
    )


    return programa["arquivo"]




def instalar(programa):

    arquivo = baixar(
        programa
    )


    print(
        "Executando instalador..."
    )


    subprocess.run(
        arquivo,
        shell=True
    )




def menu():

    nomes = list(
        PROGRAMS.keys()
    )


    while True:

        print("""
==============================
 WUR - Windows User Repository
==============================

Programas disponíveis:
""")


        for i,nome in enumerate(
            nomes,
            1
        ):

            print(
                f"{i} - {nome}"
            )


        print(
            "0 - Sair"
        )


        escolha = input(
            "\nEscolha: "
        )


        if escolha == "0":

            print(
                "Encerrando WUR..."
            )

            break


        try:

            programa_nome = nomes[
                int(escolha)-1
            ]


            versoes = PROGRAMS[
                programa_nome
            ]


            print(
                f"\n{programa_nome} - Versões:\n"
            )


            for i,versao in enumerate(
                versoes,
                1
            ):

                print(
                    f"{i} - Versão {versao['versao']}"
                )


            escolha_versao = int(
                input(
                    "\nEscolha a versão: "
                )
            )


            programa = versoes[
                escolha_versao - 1
            ]


            instalar(
                programa
            )


        except Exception as erro:

            print(
                "Erro:",
                erro
            )




if __name__ == "__main__":

    menu()
