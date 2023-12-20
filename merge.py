#!/bin/env python3

import csv

def read_numbers_from_file(file_path):
    numbers_map = {}
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            numbers_map[number] = True
    return numbers_map

def read_numbers_from_csv(file_path):
    numbers_map = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            string_value = row[0]
            integer_value = int(row[1])
            if integer_value not in numbers_map:
                numbers_map[integer_value] = []
            numbers_map[integer_value].append(string_value)
    return numbers_map

map_path = 'map.csv'
posters_file_path = 'allpostersids.txt'

posters_map = read_numbers_from_file(posters_file_path)
posts_map = read_numbers_from_csv(map_path)

# Find items in post_map that match each item in posters_map
matching_items = {}
for item in posters_map:
    if item in posts_map:
        matching_items[item] = posts_map[item]





