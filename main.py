# -*- coding: <UTF-8> -*-
import lerConversa as con

conversa = con.Conversa(fileConversa="Conversa.txt")
conversa.identificarEnvolvidos()

conversa.deletarLinhas()
conversa.juntarDuplicadas()

conversa.separarDataMensagem()

