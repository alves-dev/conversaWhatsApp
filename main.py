# -*- coding: <UTF-8> -*-
import lerConversa as con

conversa = con.Conversa(fileConversa="ConversaMa.txt")
conversa.identificarEnvolvidos()

conversa.deletarLinhas()
conversa.juntarDuplicadas()

conversa.separarDataMensagem()

