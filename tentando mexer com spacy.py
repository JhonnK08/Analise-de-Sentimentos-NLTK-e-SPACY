
import csv
import pandas
import string
import seaborn
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

#WORDNET AFFECT
#with open('D:\Github\TCC\DICIONÁRIOS\wordNetAffect\wordnetaffectbr_valencia.csv', 'r', encoding='utf8') as wordnet:

#wordnet = pandas.read_csv('D:\Github\TCC\DICIONÁRIOS\wordNetAffect\wordnetaffectbr_valencia2.csv', encoding='utf8')

#wordnet.shape
#print(wordnet.head())

#lexicon-pt
#with open('D:\Github\TCC\DICIONÁRIOS\lexiconPT-master\data-raw\lexico_v2.txt', 'r', encoding='utf8') as lexicon:
#    lexicon = csv.reader(lexicon, delimiter=',')

#oplexicon
#with open('D:\Github\TCC\DICIONÁRIOS\oplexicon_v3.0\lexico_v3.0.txt', 'r', encoding='utf8') as oplexicon:
#    oplexicon = csv.reader(oplexicon, delimiter=',')

lexicon = pandas.read_csv('DICIONÁRIOS\lexiconPT-master\data-raw\lexico_v2.txt', encoding='utf8', delimiter=',', low_memory=False)
oplexicon = pandas.read_csv('DICIONÁRIOS\oplexicon_v3.0\lexico_v3.0.txt', encoding='utf8', delimiter=',', low_memory=False)


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
def Preprocessamento(texto) :
    texto = str(texto)
    texto = texto.lower()
    documento = nlp(texto)
    lista = []
    #Tokenizacao
    for token in documento:
        #lista.append(token.text)
        lista.append(token.lemma_)
    lista = [palavra for palavra in lista if palavra not in stopwords and palavra not in pontuacao] # retira stopwords
    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()]) # retira digitos

    return lista


#TUDO
def Tudo(frase) :
    for token in frase :
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)


#POS
def POS (frase) :
    for token in frase :
        print(token.text, token.pos_)
#Procura de entidades
def Entidades (frase) :
    for entidade in frase.ents :
        print(entidade.text, entidade.label_)

#STOPWORDS
def Stopwords (frase):
    print('Stopwords:')
    for token in frase :
        if not token.is_stop :
            frase.append(token)
        else :
            print(token)



chat0104['MENSAGEM'] = chat0104['MENSAGEM'].apply(Preprocessamento)
chat0104.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_01_04\Chat_ATIV_01_04-lemma.csv', index = False)
chat0107['MENSAGEM'] = chat0107['MENSAGEM'].apply(Preprocessamento)
chat0107.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_01_07\Chat_ATIV_01_07-lemma.csv', index = False)
chat0507['MENSAGEM'] = chat0507['MENSAGEM'].apply(Preprocessamento)
chat0507.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_05_07\Chat_ATIV_05_07-lemma.csv', index = False)
chat0810['MENSAGEM'] = chat0810['MENSAGEM'].apply(Preprocessamento)
chat0810.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_08_10\Chat_ATIV_08_10-lemma.csv', index = False)
#frase = nlp(mensagens[2])
#displacy.serve(frase, style='dep')
#Tokenizar(frase)
#Stopwords(frase)
#Lematizacao(frasePOS)



