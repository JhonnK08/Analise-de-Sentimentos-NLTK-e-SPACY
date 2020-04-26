import nltk
import csv

from nltk.stem import WordNetLemmatizer

alunos = []
mensagens = []

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

with open('ANALISE DOS DADOS\CHATS\Chat_ATIV_01_04\Chat_ATIV_01_04.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    #dados = [][]
    cont_linha = 0
    for row in csv_reader:
        if cont_linha == 0 :
            cont_linha += 1
        else :
            cont_linha += 1
            alunos.append(row[2])
            mensagens.append(row[4])
            print(mensagens)


