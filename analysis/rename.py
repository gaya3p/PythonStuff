import os
#import csv
  
#season_details = {}
    
'''with open('b99.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    for row in reader:
        if row['Season'] == '7':
            eno, etitle = row['Episode'].zfill(2), row['Title']
            season_details[eno] = etitle'''
            
os.chdir(r"F:\movies\brooklyn\")

for f in os.listdir():
    fname, s = os.path.splitext(f)
    
    

    os.rename(f, new_name)