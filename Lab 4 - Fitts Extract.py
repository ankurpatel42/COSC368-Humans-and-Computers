import math
import csv

dict_ = {}
dict_2 = {}
dict_3 = {}

file = open("experiment_fitts_log.txt", 'r') #used their one (their fitts.py) to obtain the data/text file
lines = file.readlines()

for line in lines:
    m_line = line.strip("\n")
    s_line = m_line.split(" ")
    k_line = s_line[0].split("\t")
    if (k_line[1], k_line[2], k_line[3]) in dict_:
        dict_[(k_line[1], k_line[2], k_line[3])].append(float(k_line[4]))
    else:
        dict_[(k_line[1], k_line[2], k_line[3])] = [float(k_line[4])]

for key, value in dict_.items():
    for time in value:
        dict_2.setdefault((key[0], key[1]), []).append(time / 1000)  
 
with open('summary.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for key, value in dict_2.items():
        value_without_first_two = value[2:]
        mean_time = round((sum(value_without_first_two) / len(value_without_first_two)), 3) #slicing to ignore first two trials for each block/selection
        ID = round(math.log2((int(key[0])/int(key[1])) + 1), 3)
        spamwriter.writerow([key[0]] + [key[1]] + [ID] + [mean_time])
        dict_3.setdefault(ID, []).append(mean_time)
        
    for key, value in dict_3.items():
        m_time = round((sum(value) / len(value)), 3)
        spamwriter.writerow([key] + [m_time])

