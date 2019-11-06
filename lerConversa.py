# -*- coding: <UTF-8> -*-
from io import open


class Conversa():

    def __init__(self, fileConversa):
        self.fileConversa = fileConversa
        self.pessoa1 = None
        self.pessoa2 = None
        self.conversa = None

    def identificarEnvolvidos(self):
        ref_conversa = open(self.fileConversa, "r", encoding="utf-8")
        self.conversa = ref_conversa.readlines()
        ref_conversa.close()

        envolvidos = []
        for i in self.conversa:
            if " - " in i:
                temp = i.split(" - ")
                if ":" in temp[1]:
                    temp = temp[1].split(":")
                    if temp[0] not in envolvidos:
                        envolvidos.append(temp[0])
        print(envolvidos)
        if len(envolvidos) != 2:
            return f"Erro, envolvidos diferente de 2 : {envolvidos}"
        else:
            self.pessoa1 = envolvidos[0]
            self.pessoa2 = envolvidos[1]

    def deletarLinhas(self):
        ref_conversa = open(self.fileConversa, "w", encoding="utf-8")
        for l in self.conversa:
            if "<Arquivo de mídia oculto>" not in l:
                if ":" in l:
                    if " - " + self.pessoa1 in l:
                        ref_conversa.write(l)
                    if " - " + self.pessoa2 in l:
                        ref_conversa.write(l)

        ref_conversa.close()

    def juntarDuplicadas(self):
        ref_conversa = open(self.fileConversa, "r", encoding="utf-8")
        self.conversa = ref_conversa.readlines()
        ref_conversa = open(self.fileConversa, "w", encoding="utf-8")
        p1 = p2 = 0
        l = ""
        texto = ""

        for l in self.conversa:
            print(l)
            if self.pessoa1 in l:
                p1 += 1
                if p2 > 0:
                    ref_conversa.write(texto + "\n")
                    texto = ""
                p2 = 0
            if self.pessoa2 in l:
                p2 += 1
                if p1 > 0:
                    ref_conversa.write(texto + "\n")
                    texto = ""
                p1 = 0
            l = l.replace("\n", "")
            if texto != "":
                temp = l.split(":")
                texto = texto + ", " + temp[2]
            else:
                texto = l
        ref_conversa.close()

    def separarDataMensagem(self):
        ref_conversa = open(self.fileConversa, "r", encoding="utf-8")
        self.conversa = ref_conversa.readlines()
        ref_conversa = open(self.fileConversa, "w", encoding="utf-8")

        for l in self.conversa:
            l = l.split(":")
            ref_conversa.write(l[2])

        ref_conversa.close()