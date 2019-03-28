opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(col_num):
    column_data = []
    for row in apps_data[1:]:
        column = row[col_num]
        column_data.append(column)
    return column_data

genres = extract(11)


# something newwww