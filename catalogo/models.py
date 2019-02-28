from django.db import models


# Criando model
# Começando a criar o Banco de Dados

class Filme(models.Model):
    # Deve ter o mesmo padrao, se tem 3 letras todos devem ter 3 letras, no caso são duas.
    genero_acao = 'ac'
    genero_aventura = 'av'
    genero_ficcao = 'fc'
    genero_terror = 'tr'
    genero_comedia = 'cm'
    genero_drama = 'dr'
    genero_romance = 'ro'

    genero_opcoes = [
        (genero_acao, 'Ação'),
        (genero_aventura, 'Aventura'),
        (genero_ficcao, 'Ficção'),
        (genero_terror, 'Terror'),
        (genero_comedia, 'Comédia'),
        (genero_drama, 'Drama'),
        (genero_romance, 'Romance'),
    ]

    nome = models.CharField(max_length=120)
    # São dois, pois a minha lista de genero possuem duas letras
    genero = models.CharField(max_length=2, choices=genero_opcoes, default=None)
    sinopse = models.TextField()
    lancamento = models.DateField()
    duracao = models.PositiveIntegerField()
    classificacao_indicativa = models.PositiveIntegerField()
    # Pasta na raiz para subir as imagens
    cartaz = models.ImageField(upload_to='media')

    # Essa função retorna o nome do filme que foi definido em -->a nome = models.CharField(max_length=120)
    def __str__(self):
        return self.nome