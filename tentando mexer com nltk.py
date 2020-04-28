import nltk
import csv
import csv
import pandas
import string
import seaborn
import numpy
import pickle

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import tokenize
from nltk.corpus import brown
from nltk.stem import WordNetLemmatizer



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


chat0104 = pandas.read_csv('ANALISE DOS DADOS\CHATS\Chat_ATIV_01_04\Chat_ATIV_01_04-2.csv', encoding='utf8', delimiter=';', low_memory=False)
chat0107 = pandas.read_csv('ANALISE DOS DADOS\CHATS\Chat_ATIV_01_07\Chat_ATIV_01_07-2.csv', encoding='utf8', delimiter=';', low_memory=False)
chat0507 = pandas.read_csv('ANALISE DOS DADOS\CHATS\Chat_ATIV_05_07\Chat_ATIV_05_07-2.csv', encoding='utf8', delimiter=';', low_memory=False)
chat0810 = pandas.read_csv('ANALISE DOS DADOS\CHATS\Chat_ATIV_08_10\Chat_ATIV_08_10-2.csv', encoding='utf8', delimiter=';', low_memory=False)


pontuacao = string.punctuation
stopwords = nltk.corpus.stopwords.words('portuguese')
stemmer = nltk.stem.RSLPStemmer()
#tokens = word_tokenize(sentenca)
#tags = pos_tag(tokens)

#Pré-processamento
def Preprocessamento(texto) :
    texto = str(texto)
    texto = texto.lower()
    #documento = word_tokenize(texto)
    documento = tokenize.word_tokenize(texto, language='portuguese')
    lista = []
    #Tokenizacao
    for token in documento:
        lista.append(stemmer.stem(token))
    lista = [palavra for palavra in lista if palavra not in stopwords and palavra not in pontuacao] # retira stopwords
    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()]) # retira digitos

    return lista



chat0104['MENSAGEM'] = chat0104['MENSAGEM'].apply(Preprocessamento)
chat0104.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_01_04\Chat_ATIV_01_04-stem.csv', index = False)
chat0107['MENSAGEM'] = chat0107['MENSAGEM'].apply(Preprocessamento)
chat0107.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_01_07\Chat_ATIV_01_07-stem.csv', index = False)
chat0507['MENSAGEM'] = chat0507['MENSAGEM'].apply(Preprocessamento)
chat0507.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_05_07\Chat_ATIV_05_07-stem.csv', index = False)
chat0810['MENSAGEM'] = chat0810['MENSAGEM'].apply(Preprocessamento)
chat0810.to_csv(r'ANALISE DOS DADOS\CHATS\Chat_ATIV_08_10\Chat_ATIV_08_10-stem.csv', index = False)
