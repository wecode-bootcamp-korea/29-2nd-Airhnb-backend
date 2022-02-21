import csv
import os
import django
import sys 

from pathlib   import Path 

#BASE_DIR = Path(__file__).resolve().parent.parent 

#print(BASE_DIR)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airhnb.settings')
django.setup()

from houses.models   import Country, City, Ghost, House, HouseImage, HouseType

CSV_PATH_COUNTRY = './countries.csv'
CSV_PATH_CITY = './cities.csv'
CSV_PATH_GHOST = './ghosts.csv'
CSV_PATH_HOUSE_IMAGE = './house_images.csv'
CSV_PATH_HOUSE = './houses3.csv'
CSV_PATH_HOUSE_TYPE = './house_types.csv'

def insert_country():
    with open(CSV_PATH_COUNTRY) as in_file:
        reader= csv.reader(in_file)
        next(reader,None)
        for row in reader:
            Country.objects.create(
                name = row[0]
            )
            print(row)

def insert_city():
    with open(CSV_PATH_CITY) as in_file:
        reader= csv.reader(in_file)
        next(reader,None)
        for row in reader:
            City.objects.create(
                country_id = row[0],
                name = row[1]
            )
            print(row)

def insert_house_type():
    with open(CSV_PATH_HOUSE_TYPE) as in_file:
        reader= csv.reader(in_file)
        next(reader,None)
        for row in reader:
            HouseType.objects.create(
                name = row[0]
            )
            print(row)

def insert_ghost():
    with open(CSV_PATH_GHOST) as in_file:
        reader= csv.reader(in_file)
        next(reader,None)
        for row in reader:
            Ghost.objects.create(
                name = row[0]
            )
            print(row) 

def insert_house():
    with open(CSV_PATH_HOUSE) as in_file:
        reader= csv.reader(in_file)
        next(reader,None)
        for row in reader:
            House.objects.create(
                name = row[0],
                description=row[1],
                latitude=row[2],
                longitude=row[3],
                max_guest=row[4],
                trap=row[5],
                exit=row[6],
                ghost_id=row[7],
                city_id=row[8],
                house_type_id=row[9]
            )
            print(row)  

def insert_house_image():
    with open(CSV_PATH_HOUSE_IMAGE) as in_file:
        reader= csv.reader(in_file)
        next(reader,None)
        for row in reader:
            HouseImage.objects.create(
                house_id = row[0],
                image_url = row[1]
            )
            print(row)                                           
            
insert_country()
insert_city()
insert_house_type()
insert_ghost()
insert_house()
insert_house_image()