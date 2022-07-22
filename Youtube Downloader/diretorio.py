import os, re, platform
from pathlib import Path

class Diretorio:

    @staticmethod
    def existe_disco(disco):

        op = platform.system().lower()

        if op == 'windows':

            padrao = '[A-Za-z]{1,}[^A-Za-z]'

            procura = re.findall(padrao, disco)
            try:
                existe = os.path.isdir(procura[0])

            except IndexError:
                existe = False

            return existe

        else:

            padrao = '[^A-Za-z]{1}[A-Za-z]{1,}[^A-Za-z]'

            procura = re.findall(padrao, disco)

            try:
                existe = os.path.isdir(procura[0])

            except IndexError:
                existe = False

            return existe

    @staticmethod
    def existe_diretorio(caminho):
        return os.path.isdir(caminho)

    def diretorio(self, nome):

        amarelo = '\033[1;33m'
        reset = '\033[0;0m'

        op = platform.system().lower()
        if op == 'windows':
            caminho = Path(Path.home(), 'yt downloader', f'{nome}'.lower())
            caracteres_invalios = '\nO nome da pasta não pode conter esses caracteres:' + \
                                  ' :' + ' *' + ' ?' + ' "' + " '" + ' <' + ' >' + ' |'

            local_invalido = '\nO disco local informado não existe...'

        elif op == 'linux':
            caminho = Path(Path.home(), 'yt_downloader', f'{nome}'.lower())
            caracteres_invalios = '\nO nome da pasta não pode conter esses caracteres:' + \
                                  ' !' + ' @' + ' #' + ' $' + ' %' + ' ^' + ' &' + ' *' + ' (' + ' )\n' + \
                     (' ' * 49) + ' [' + ' ]' + ' {' + ' }' + " '" + ' "' + ' |' + ' ;' + ' <' + ' >'

            local_invalido = '\nLocal para download não permitido ou inexistente.'

        else:
            caminho = Path(Path.home(), 'yt downloader', f'{nome}'.lower())
            caracteres_invalios = '\nO nome da pasta não pode conter esses caracteres:' + \
                                  ' :' + ' *' + ' ?' + ' "' + " '" + ' <' + ' >' + ' |'

        print(f'\nPasta padrão para o download: {caminho}')

        cond = 0

        while cond == 0:

            sim = ['sim', 's']
            nao = ['não', 'nao', 'n']
            pergunta = input('Mudar pasta?' + (amarelo + '(S/n)' + reset) + ': ').lower().strip()

            diretorio = Path(Path.home(), 'YT Downloader', f'{nome}')
            diretorio = os.path.normpath(diretorio)
            diretorio = os.path.normcase(diretorio)

            if pergunta in nao:
                return diretorio

            if pergunta in sim:
                cond = 0

                while cond == 0:

                    diretorio = (input(amarelo + '\n>>> ' + reset).strip())

                    diretorio = os.path.normpath(diretorio)
                    diretorio = os.path.normcase(diretorio)

                    existe_disco = Diretorio.existe_disco(diretorio)

                    if existe_disco:

                        verifica_diretorios = Diretorio.existe_diretorio(diretorio)

                        if verifica_diretorios == True:
                            return diretorio

                        else:
                            try:
                                novo = os.mkdir(diretorio)
                                print('oi')
                                return diretorio

                            except OSError:
                                print(caracteres_invalios)
                                continue

                    if not existe_disco:
                        print(local_invalido)
                        continue

                    cond += 1

            else:
                continue

            cond += 1
