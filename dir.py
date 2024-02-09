import git
from cookiecutter.main import cookiecutter
from git.exc import GitCommandError, InvalidGitRepositoryError

def clone_repository(repo_url, repo_path):
    try:
        git.Repo.clone_from(repo_url, repo_path)
        print(f'Repositório clonado em {repo_path}')
    except GitCommandError as e:
        print(f'Erro ao clonar o repositório: {e}')

def generate_code(template_path, repo_path):
    try:
        cookiecutter(template_path, output_dir=repo_path)
        print('Código gerado pelo Cookiecutter.')
    except Exception as e:
        print(f'Erro ao gerar código com o Cookiecutter: {e}')

def commit_and_push(repo_path):
    try:
        repo = git.Repo(repo_path)
        repo.git.add('--all')
        repo.git.commit('-m', 'Adiciona código gerado pelo Cookiecutter')
        repo.git.push()
        print('Alterações adicionadas, commitadas e enviadas para o repositório.')
    except GitCommandError as e:
        print(f'Erro ao realizar commit e push: {e}')

# Substitua com seus valores específicos
repo_url = 'https://seu-usuario@bitbucket.org/seu-usuario/seu-repositorio.git'
repo_path = 'caminho/local/do/repositorio'
template_path = 'caminho/do/template'

try:
    clone_repository(repo_url, repo_path)
    generate_code(template_path, repo_path)
    commit_and_push(repo_path)
except InvalidGitRepositoryError:
    print('Diretório do repositório inválido.')
except Exception as e:
    print(f'Erro desconhecido: {e}')

