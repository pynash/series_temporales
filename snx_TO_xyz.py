#!/usr/bin/env python
# Copyright (c) 2016, Walter Vargas <pynash@gmail.com>

import os


def count_est(lista):
    clean = []
    for i in range(len(lista)):
        # to_save.append(lista[i][2])
        if lista[i][2] not in clean:
            clean.append(lista[i][2])
    return clean

station = []

def read_and_write(file):
    estimate = []
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
        #for i in estimate:
         #   print i
        # estimate = clear_column(estimate)
    write_general(str(file)+ ' Numero de Estaciones: ' + str(len(count_est(estimate)))+'\n')

    dic = dict()

    for i in estimate:
    # select register for keys about an station
        if i[2] in dic:
            dic.setdefault(i[2], []).append([i[5], i[8], i[9]])
        else:
            dic[i[2]] = [[i[5], i[8], i[9]]]
    write_general('estacion \tEPOCA   \tX \t\tSIGMA_X \t\tY \t\tSIGMA_Y \t\tZ \t\tSIGMA_Z\n')
        #write_general(str(i)+'\t'+str(dic[i][0][0])+'\t'+str(dic[i][0][1])+'\t'+str(dic[i][0][2])+'\t'+str(dic[i][1][1])+'\t'+str(dic[i][1][2])+'\t'+str(dic[i][2][1])+'\t'+str(dic[i][2][2]))
    for i in dic:
        with open('./CSVs/XYZ.dat', 'a') as stat:
            stat.write(str(i)+'\t'+str(dic[i][0][0])+'\t'+str(dic[i][0][1])+'\t'+str(dic[i][0][2])+'\t'+str(dic[i][1][1])+'\t'+str(dic[i][1][2])+'\t'+str(dic[i][2][1])+'\t'+str(dic[i][2][2])+'\n')
        if i not in station:
            station.append(i)
            create_files_csv(i)
        with open('./CSVs/'+str(i)+'.csv', 'a') as stat:
            stat.write(str(dic[i][0][0])+'\t'+str(dic[i][0][1])+'\t'+str(float(dic[i][0][2]))+'\t'+str(float(dic[i][1][1]))+'\t'+str(float(dic[i][1][2]))+'\t'+str(float(dic[i][2][1]))+'\t'+str(float(dic[i][2][2]))+'\n')
            #stat.write(str(float(dic[i][0][1]))+' \t '+str(float(dic[i][0][2]))+' \t '+str(float(dic[i][1][1]))+' \t '+str(float(dic[i][1][2]))+' \t '+str(float(dic[i][2][1]))+' \t '+str(float(dic[i][2][2]))+'\n')

def write_general(line):
    with open('./CSVs/XYZ.dat', 'a') as filexyz:
        filexyz.write(line)

def create_files_csv(fname):
    with open('./CSVs/'+fname+'.csv', 'a') as stat:
        stat.write('   fecha\t    \tX\t      \t   SIGMA X\t \t  Y\t   SIGMA Y\t     Z\t\t   SIGMA Z \n')


if __name__=="__main__":
    path = './'
    f = os.listdir(path)
    f.sort()
    #for i in range(len(f)):
    for i in f:
        if i.endswith(".SNX"):
            with open(str(path)+str(i)) as file:
                read_and_write(file)
