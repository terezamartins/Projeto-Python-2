# Decida por mim
# Fazer uma pergunta para o programa, para que ele te dê uma resposta

import random


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, faça isso!',
            'Não sei, depende de você.',
            'Não faça isso.',
            'Acho que agora é um bom momento para isso.'
        ]

    def iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.iniciar()