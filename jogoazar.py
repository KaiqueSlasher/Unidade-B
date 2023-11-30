class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, jogo_id):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id = jogo_id

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Taxa de Entrada: {self.taxa_entrada}, ID: {self.id}"


class Plataforma:
    def __init__(self):
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)
        print(f"Jogo '{jogo.nome}' adicionado à plataforma.")

    def remover_jogo(self, jogo_id):
        for jogo in self.jogos:
            if jogo.id == jogo_id:
                self.jogos.remove(jogo)
                print(f"Jogo '{jogo.nome}' removido da plataforma.")
                return
        print(f"Jogo com ID {jogo_id} não encontrado na plataforma.")

    def listar_jogos(self):
        if not self.jogos:
            print("A plataforma não possui jogos no momento.")
            return
        print("Jogos na plataforma:")
        for jogo in self.jogos:
            print(jogo)

    def __str__(self):
        return f"Plataforma com {len(self.jogos)} jogos."


# Exemplo de uso
if __name__ == "__main__":
    jogo1 = Jogo("Pôquer", "Cartas", 10.0, 1)
    jogo2 = Jogo("Caça-Níqueis", "Máquinas", 5.0, 2)
    jogo3 = Jogo("Roleta", "Mesa", 15.0, 3)

    plataforma = Plataforma()

    plataforma.adicionar_jogo(jogo1)
    plataforma.adicionar_jogo(jogo2)
    plataforma.adicionar_jogo(jogo3)

    plataforma.listar_jogos()

    plataforma.remover_jogo(2)

    plataforma.listar_jogos()

    print(plataforma)