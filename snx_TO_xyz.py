#!/usr/bin/env python

import os


def debug_cero(list_head):
    # change decimal and add cero
    for i in range(len(list_head)):
        list_head[i][9] = '0' + list_head[i][9]
        if list_head[i][8].startswith('.'):
            list_head[i][8] = str(0) + list_head[i][8]
        elif list_head[i][8].startswith('-'):
            y = ''
            list_tmp = list(list_head[i][8])
            print list_tmp[i]
            list_tmp[i].insert(8, '0')
            list_head[i][8] = y
    return list_head


def count_est(lista):
    clean = []
    for i in range(len(lista)):
        # to_save.append(lista[i][2])
        if lista[i][2] not in clean:
            clean.append(lista[i][2])
    return clean


def clear_column(listado):
    # call for... estimate = clear_column(estimate)
    # copy and join text, then del two value
    tmp = listado[0][8]+'_'+listado[0][9]
    del(listado[0][8])
    del(listado[0][8])
    # insert on 8position
    listado[0].insert(8, tmp)
    return listado[1:]


def main():
    estimate = []
    path = './'
    f = os.listdir(path)
    # for i in range(len(f)):
    with open(str(path)+str(f[-1])) as file:
        # Text before, dont read:
        for line in file:
            if line.strip() == '+SOLUTION/ESTIMATE':
                # Or whatever test is needed
                break
        # Reading the text at the end
        for line in file:  # This keeps reading the file
            if line.strip() == '-SOLUTION/ESTIMATE':
                break
            estimate.append(line.split())
        estimate = estimate[1:]
        for i in estimate:
            print i
        # estimate = clear_column(estimate)
        print f[-1] + ' Numero de Estaciones: ' + str(len(count_est(estimate)))

        dic = dict()

        for i in estimate:
            # select register for keys about an station
            if i[2] in dic:
                dic.setdefault(i[2], []).append([i[5], i[8], i[9]])
            else:
                dic[i[2]] = [[i[5], i[8], i[9]]]
        print 'estacion \tEPOCA   \tX \t\tSIGMA_X \t\tY \t\tSIGMA_Y \t\tZ \t\tSIGMA_Z'
        for i in dic:
            print str(i)+'\t'+str(dic[i][0][0])+'\t'+str(dic[i][0][1])+'\t'+str(dic[i][0][2])+'\t'+str(dic[i][1][1])+'\t'+str(dic[i][1][2])+'\t'+str(dic[i][2][1])+'\t'+str(dic[i][2][2])


main()
