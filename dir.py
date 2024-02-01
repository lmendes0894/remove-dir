import os
import shutil

def varrer_diretorios(diretorio_raiz, lista_nomes):
    for root, dirs, files in os.walk(diretorio_raiz, topdown=False):
        for nome_dir in lista_nomes:
            if nome_dir in dirs:
                caminho_dir = os.path.join(root, nome_dir)
                print(f'Removendo diretório: {caminho_dir}')
                try:
                    shutil.rmtree(caminho_dir)
                    print(f'Diretório removido com sucesso: {caminho_dir}')
                except Exception as e:
                    print(f'Erro ao remover diretório {caminho_dir}: {e}')

if __name__ == "__main__":
    diretorio_raiz = input("Digite o caminho do diretório raiz do projeto: ")
    
    lista_nomes = ["nome_dir1", "nome_dir2", "nome_dir3"]  # Substitua com os nomes que você deseja remover
    
    varrer_diretorios(diretorio_raiz, lista_nomes)

