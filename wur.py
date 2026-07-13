import os
import sys
import subprocess
import requests


PROGRAMS = {

    "TFiles": {

        "versoes": [

            {
                "versao": "0.2-1",
                "arquivo": "TFiles_Setup.exe",
                "url": "https://sourceforge.net/projects/tfiles/files/TFiles%200.2-1_Setup.exe/download",
                "dependencias": []
            }

        ]

    },


    "MBrowser": {

        "versoes": [

            {
                "versao": "1.0",
                "arquivo": "MBrowser_Setup.exe",
                "url": "https://sourceforge.net/projects/mbrowser/files/MBrowser_Setup.exe/download",

                "dependencias": [
                    "python",
                    "PyQt6",
                    "PyQt6-WebEngine",
                    "tkinter"
                ]
            }

        ]

    },


    "Firefox": {

        "versoes": [

            {
                "versao": "Atual",
                "arquivo": "Firefox_Setup.exe",
                "url": "https://download.mozilla.org/?product=firefox-latest&os=win64",

                "dependencias": []
            }

        ]

    }

}



def verificar_dependencias(lista):

    if not lista:
        return


    print("\nVerificando dependências...\n")


    for dep in lista:

        if dep == "python":

            print("[OK] Python")



        elif dep == "PyQt6":

            try:
                import PyQt6
                print("[OK] PyQt6")

            except:

                print("[INSTALAR] PyQt6")

                subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "pip",
                        "install",
                        "PyQt6"
                    ]
                )



        elif dep == "PyQt6-WebEngine":

            try:
                import PyQt6.QtWebEngine
                print("[OK] Qt WebEngine")

            except:

                print("[INSTALAR] Qt WebEngine")

                subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "pip",
                        "install",
                        "PyQt6-WebEngine"
                    ]
                )



        elif dep == "tkinter":

            try:
                import tkinter
                print("[OK] Tkinter")

            except:

                print(
                    "[AVISO] Tkinter não encontrado"
                )



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
        allow_redirects=True,
        stream=True
    )


    with open(
        programa["arquivo"],
        "wb"
    ) as arquivo:


        for bloco in resposta.iter_content(
            8192
        ):

            if bloco:
                arquivo.write(bloco)



    print(
        "\nDownload concluído!"
    )


    return programa["arquivo"]




def instalar(programa):

    verificar_dependencias(
        programa["dependencias"]
    )


    arquivo = baixar(
        programa
    )


    print(
        "\nExecutando instalador..."
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
            break


        try:

            nome = nomes[
                int(escolha)-1
            ]


            versoes = PROGRAMS[nome]["versoes"]


            print(
                f"\n{nome} - Versões disponíveis:\n"
            )


            for i,v in enumerate(
                versoes,
                1
            ):

                print(
                    f"{i} - {v['versao']}"
                )


            escolha_v = int(
                input(
                    "\nEscolha a versão: "
                )
            )


            programa = versoes[
                escolha_v-1
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
