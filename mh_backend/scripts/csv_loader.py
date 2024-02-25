import csv

from quickstart.models import Branch

def run():
    """
    Initial script of loading the csv into postgresql.
    """
    try:
        f = open('dataset.csv', encoding='utf-8-sig')
        reader = csv.reader(f)
    except:
        print("Error: dataset.csv file not found. Run data_scraping/data_scraping.py to generate the file.")

    # Clear DB
    Branch.objects.all().delete()

    # Load data
    for row in reader:
        Branch(name = row[0], address = row[1], operating_hours = row[2], waze_link = row[3], latitude = row[4], longitude = row[5]).save()
        print(row)

