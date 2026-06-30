class Inventario:
    def __init__(self):
        self.chaves = []
        self.kits = []
        self.dicas = []

    def adicionar_chave(self, chave):
        self.chaves.append(chave)
        print("chave coletada: " + chave.nome)
        print("total de chaves: " + str(len(self.chaves)) + "/3")

    def adicionar_kit(self, kit):
        self.kits.append(kit)
        print("kit medico coletado!")
        print("total de kits: " + str(len(self.kits)))

    def adicionar_dica(self, dica):
        self.dicas.append(dica)
        print("dica coletada: " + dica.nome)
        print("total de dicas: " + str(len(self.dicas)) + "/3")

    def tem_chave(self, nome):
        for c in self.chaves:
            if c.nome == nome:
                return True
        return False

    def jogo_vencido(self):
        return len(self.chaves) >= 3
