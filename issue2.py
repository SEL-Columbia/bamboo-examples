#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

import sys
import time

from pybamboo.dataset import Dataset

DATASET_ID = sys.argv[-1]
CSV_URL = u"https://github.com/modilabs/bamboo-examples/raw/master/data/water_points.csv"

WAIT_INTERVAL = 10
WAIT_MAX = 180

if DATASET_ID:
    print("Retrieving dataset from UUID %s" % DATASET_ID)
    dataset = Dataset(dataset_id=DATASET_ID)
else:
    print(u"Creating dataset from %s" % CSV_URL)
    dataset = Dataset(url=CSV_URL)

waited = 0
while(dataset.get_info().get(u'state', 'ready') != 'ready'):
    if waited >= WAIT_MAX:
        print(u"Unable to get dataset ready in time. Exiting.")
        sys.exit()

    print(u"Dataset not ready. Waiting 10s...")
    time.sleep(WAIT_INTERVAL)
    waited += WAIT_INTERVAL

print(u"---")
print(dataset.get_info())
print(u"---")

print(u"Creating calculations")
dataset.add_aggregation(formula='water_points=count()', groups=['district'])
dataset.add_aggregation(formula='district_pop=sum(community_pop)', groups=['district'])
dataset.add_calculation(formula='district_pop_to_wp=district_pop/water_points')
print(u"---")

print(u"Listing calculations")
print(dataset.get_calculations())
print(u"---")
print(u"Listing aggregate datasets:")
print(u"\n".join([u"\t%s: %s" % (dsk, ds.get_info().get('id', 'n/a'))
                  for dsk, ds in dataset.get_aggregate_datasets().items()]))

print(u"---")
print(u"District Populations to Water Points")
district_dataset = dataset.get_aggregate_datasets()['district']
from pprint import pprint as pp ; pp(district_dataset.get_data())
