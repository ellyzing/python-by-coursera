import os
import csv
import re
flag = False

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.flag=True
        self.brand = brand
        result = re.match(r'\w+(.jpg|.jpeg|.png|.gif){1}', photo_file_name)

        if (result is not None) and (len(photo_file_name)==len(result.group(0))):

            self.photo_file_name = result.group(0)
        else:

            self.photo_file_name = ""
            self.flag = False

        try:
            #print(self.carrying)
            self.carrying = float(carrying)
            #print(self.carrying)
        except ValueError:
            self.flag=False
            self.carrying = 0.0


    def get_photo_file_ext(self):
        return(os.path.splitext(self.photo_file_name)[-1])


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type="car"
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            self.passenger_seats_count = 0
            self.flag=False



class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.car_type="truck"
        super().__init__(brand, photo_file_name, carrying)
        self.flagT = True
        if body_whl:
            self.body_whl = body_whl
        else:
            self.body_whl = "0x0x0"
        try:
            self.body_length, self.body_width, self.body_height = body_whl.split("x")
            self.body_length, self.body_width, self.body_height = float(self.body_length), float(self.body_width), float(self.body_height)
            flagT=True
        except ValueError:
            self.body_length, self.body_width, self.body_height = float(0), float(0), float(0)
            flagT=False
    def get_body_volume(self):
        if self.flagT:

            volume=self.body_length*self.body_width*self.body_height
            return volume
        else:
            return ""


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type="spec_machine"
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.extra = str(extra)
        except ValueError:
            self.extra = ""



def parse_row(row):
    if len(row) != 7:
        return None

    car = None
    if (row[0] == 'car' or row[0] == "'car'"):
        car = Car(row[1], row[3], row[5], row[2])
        #print(car.brand, car.passenger_seats_count, car.photo_file_name, car.carrying)
        if ("" in (car.brand, car.passenger_seats_count, car.photo_file_name, car.carrying)) or (0 in (car.brand, car.passenger_seats_count, car.photo_file_name, car.carrying)):
            car = None

    elif row[0] == 'truck' or row[0] == "'truck'":
        car = Truck(row[1], row[3], row[5], row[4])
        if ("" in (car.brand, car.photo_file_name, car.body_whl, car.carrying)) or (0 in (car.brand, car.photo_file_name, car.body_whl, car.carrying)):

            car = None

    elif row[0] == 'spec_machine' or row[0] == "'spec_machine'":
        car = SpecMachine(row[1], row[3], row[5], row[6])
        if ("" in (car.brand, car.photo_file_name, car.carrying, car.extra)) or (0 in (car.brand, car.photo_file_name, car.carrying, car.extra)):

            car = None



    return car

def get_car_list(filename):
    cars = list()
    with open(filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) # skip csv header
        for row in reader:
            #print(row)
            car = parse_row(row)

            #print(car)
            if car != None:
                #print(car)
                cars.append(car)

    return cars




#Отладка
#car = Car('Nissan', 'g1.jpg', '1.3', '4')
#print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')

#truck = Truck('Nissan', 't1.jpg', '2.5', '')
#print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')

#spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
#print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')

#print(spec_machine.get_photo_file_ext())

#cars = get_car_list("cars_week3.csv")
#
#print(cars)
#   print(len(cars))

#truck = Truck('Nissan', '1.jpg', '2.5', '0x0x0')
#truck.get_body_volume()
