opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(col_num):
    column = []    
    
    for row in apps_data[1:]:
        value = row[col_num]
        column.append(value)
        
    ft_dict = {}
    
    for x in column:
        if x in ft_dict:
            ft_dict[x] += 1
        else:
            ft_dict[x] = 1
    
    return ft_dict

ratings_ft = freq_table(7)