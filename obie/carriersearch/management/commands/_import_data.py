import csv

from carriersearch.models import *


def csv_to_list():
    # todo: funciton takes filepath, checks type, and imports csv into dict, not list of lists
    data = []
    with open('/home/ev/Desktop/projects/obie/obie/carriersearch/management/commands/data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append([val for val in row])
    return data


def create_offering(policy, carrier, state):
    offering = Offering.objects.get_or_create(
        policy=policy,
        carrier=carrier,
        state=state
    )


def create_objects(data_list):
    # create states in csv if don't exist
    for elem in data_list[0][1:]:
        State.objects.get_or_create(name=elem)
    for row in data_list[1:]:
        # get create carrier
        carrier = Carrier.objects.get_or_create(name=row[0].lower())
        for index, elem in enumerate(row[1:]):
            # todo: break this out into separate funciton. so messy
            state = State.objects.get(name=data_list[0][index])
            if elem.strip().lower() == 'both' or elem.strip().lower() == 'fire':
                policy = Policy.objects.get_or_create(name='fire')
                create_offering(policy=policy, carrier=carrier, state=state)
            if elem.strip().lower() == 'both' or elem.strip().lower() == 'auto':
                policy = Policy.objects.get_or_create(name='auto')
                create_offering(policy=policy, carrier=carrier, state=state)


def main():
    data_list = csv_to_list()
    create_objects(data_list)
