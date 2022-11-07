import csv
import numpy as np

on_list = []
in_preservica = []

# 'messages.csv' isn't definitive list of what's in Preservica, it's a record
# of what's been ingested within a rolling window, even if the csv downloaded
# is unfiltered, the oldest recorded ingest is May 2021 (OCt 2022)

def get_checklist():
    with open('checklist.txt', 'r') as checklist:
        refs = checklist.readlines()
        refs = [ref.strip() for ref in refs]
        on_list.append(refs)
        return refs


def check_ingest_csv(ref_no):
    with open('messages.csv', 'r') as ingest_csv:
        reader = csv.reader(ingest_csv)

        for row in reader:
            entity_title = row[6]
            if ref_no == entity_title:
                if not entity_title in in_preservica:
                    in_preservica.append(entity_title)

def main():
    for ref_no in get_checklist():
        check_ingest_csv(ref_no)
    not_ingested = np.setdiff1d(on_list, in_preservica)
    if len(not_ingested) == 0:
        print('All input refs found on ingest csv :)')
    else:
        print('Missing from ingest: ')
        for ref in not_ingested:
            print(f'== {ref}')


if __name__ == "__main__":   
    main()
