class Inventario:
    def __init__(self):
        self.chaves = []

    def adicionar_chave(self, chave):
        self.chaves.append(chave)
        print("chave coletada: " + chave.nome)
        print("total de chaves: " + str(len(self.chaves)) + "/3")

    def tem_chave(self, nome):
        for c in self.chaves:
            if c.nome == nome:
                return True
        return False

    def jogo_vencido(self):
        return len(self.chaves) >= 3
