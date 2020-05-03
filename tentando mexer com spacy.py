
import csv
import pandas
import string
import seaborn
import matplotlib.pyplot as plt
import numpy
import spacy
from spacy import displacy
from spacy.lang.pt.stop_words import STOP_WORDS

stopwords = STOP_WORDS
nlp = spacy.load("pt_core_news_sm")
alunos = []
mensagens = []
tokenFrase = []
pontuacao = string.punctuation

#with open('ANALISE DOS DADOS\CHATS\Chat_ATIV_01_04\Chat_ATIV_01_04.csv','r') as csv_file:
#        csv_reader = csv.reader(csv_file, delimiter=';')
#        linhas = []
#        for row in csv_reader:
#            if line_count == 0:
#                print(f'Column names are {", ".join(row)}')
#               line_count += 1
#            else:
#                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#                line_count += 1
#        print(f'Processed {line_count} lines.')

dicionario = {}


with open('DICIONÁRIOS\oplexicon_v3.0\oplexicon.csv', encoding='utf8') as csvfile:
     lines = csv.reader(csvfile, delimiter=';')
     oplexico = list(lines)
     for i in range(len(oplexico)):
         if i > 0:
             palavra = oplexico[i][0]
             polaridade = oplexico[i][1]
             print(palavra, polaridade)
             dicionario[palavra] = polaridade



with open('DICIONÁRIOS\lexiconPT-master\data-raw\lexicon.csv', encoding='utf8') as csvfile:
    lines = csv.reader(csvfile, delimiter=';')
    lexicon = list(lines)
    for i in range(len(lexicon)):
        if i > 0:
            palavra = lexicon[i][0]
            polaridade = lexicon[i][1]
            print(palavra, polaridade)
            dicionario[palavra] = polaridade



with open('DICIONÁRIOS\wordNetAffect\wordnet.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter=';')
    wordnet = list(lines)
    for i in range(len(wordnet)):
        if i > 0:
            palavra = wordnet[i][0]
            polaridade = wordnet[i][1]
            print(palavra, polaridade)
            dicionario[palavra] = polaridade



with open('DICIONÁRIOS\senticnet-1.3\senticnet_pt.csv', encoding='utf8') as csvfile:
    lines = csv.reader(csvfile, delimiter=';')
    senticnet = list(lines)
    for i in range(len(senticnet)):
        if i > 0:
            palavra = senticnet[i][0]
            polaridade = senticnet[i][1]
            #print(palavra, polaridade)
            dicionario[palavra] = polaridade



chat0104 = pandas.read_csv('ANALISE DOS DADOS\CHATS\Chat_ATIV_01_04\Chat_ATIV_01_04-2.csv', encoding='utf8', delimiter=';', low_memory=False)
chat0107 = pandas.read_csv('ANALISE DOS DADOS\CHATS\Chat_ATIV_01_07\Chat_ATIV_01_07-2.csv', encoding='utf8', delimiter=';', low_memory=False)
chat0507 = pandas.read_csv('ANALISE DOS DADOS\CHATS\Chat_ATIV_05_07\Chat_ATIV_05_07-2.csv', encoding='utf8', delimiter=';', low_memory=False)
chat0810 = pandas.read_csv('ANALISE DOS DADOS\CHATS\Chat_ATIV_08_10\Chat_ATIV_08_10-2.csv', encoding='utf8', delimiter=';', low_memory=False)

#chat0104 = chat0104.astype(str)
#with open('ANALISE DOS DADOS\CHATS\Chat_ATIV_01_04\Chat_ATIV_01_04.csv', 'r', encoding='utf8') as chat0104:
#    chat0104 = csv.reader(chat0104, delimiter=';')
#    #dados = [][]
#    cont_linha = 0
#    for row in chat0104:
#        if cont_linha == 0 :
#            cont_linha += 1
#        else :
#            cont_linha += 1
#            alunos.append(row[2])
#            mensagens.append(row[4])



#Pré-processamento
def Preprocessamento(texto):
    texto = str(texto)
    texto = texto.lower()
    documento = nlp(texto)
    lista = []
    #Tokenizacao
    for token in documento:
        #lista.append(token.text)
        lista.append(token.lemma_)
    lista = [palavra for palavra in lista if palavra not in stopwords and palavra not in pontuacao and not palavra.isdigit()] # retira stopwords
    #lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()]) # retira digitos
    return lista


#TUDO
def Tudo(frase):
    for token in frase:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)

#POS
def POS (frase):
    for token in frase:
        print(token.text, token.pos_)

#Procura de entidades
def Entidades (frase):
    for entidade in frase.ents:
        print(entidade.text, entidade.label_)

#STOPWORDS
def Stopwords (frase):
    print('Stopwords:')
    for token in frase:
        if not token.is_stop:
            frase.append(token)
        else:
            print(token)

#POLARIDADE DA PALAVRA
def Polaridade (frase):
    frasepolaridade = []
    for i in frase:
        print(i)
        frasepolaridade.append(float(dicionario.get(i, 0)))
        #print(frasepolaridade)
    score = sum(frasepolaridade)
    return score

#ANALISE DE SENTIMENTO
def analises(frase):
    print('Frase: ' + frase)
    fraseprocessada = Preprocessamento(frase)
    fraseprocessada2 = ' '.join([str(elemento) for elemento in fraseprocessada])
    scorefrase = Polaridade(fraseprocessada)
    #print('Score da frase: ' + str(scorefrase))
    if scorefrase > 0:
        print('Positiva')
    elif scorefrase == 0:
        print('Neutra')
    elif scorefrase < 0:
        print('Negativo')
    print(fraseprocessada2 + ' , ' + str(scorefrase))
    return scorefrase

scores = []
scores = chat0104['MENSAGEM'].apply(analises)
chat0104dic = pandas.DataFrame(chat0104)
chat0104dic['POLARIDADE'] = scores
chat0104dic.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_01_04\Chat_ATIV_01_04-analise.csv', index = False)
#chat0107['MENSAGEM'] = chat0107['MENSAGEM'].apply(Preprocessamento)
#chat0107.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_01_07\Chat_ATIV_01_07-lemma.csv', index = False)
#chat0507['MENSAGEM'] = chat0507['MENSAGEM'].apply(Preprocessamento)
#chat0507.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_05_07\Chat_ATIV_05_07-lemma.csv', index = False)
#chat0810['MENSAGEM'] = chat0810['MENSAGEM'].apply(Preprocessamento)
#chat0810.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_08_10\Chat_ATIV_08_10-lemma.csv', index = False)
#frase = nlp(mensagens[2])
#displacy.serve(frase, style='dep')
#Tokenizar(frase)
#Stopwords(frase)
#Lematizacao(frasePOS)





