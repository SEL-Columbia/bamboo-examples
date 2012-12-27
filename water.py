#! /usr/bin/env python

import time
from pybamboo.dataset import Dataset

d = Dataset(path='water_points.csv')

print 'dataset id: %s' % d.id
time.sleep(2)

info = d.get_info()

print 'num_columns: %s' % info['num_columns']
print 'num_rows: %s' % info['num_rows']

print 'columns: %s' % info['schema'].keys()

water_points = d.get_data(select=['communities_villages','water_functioning'])
print 'return all water points where water is functioning %s' % water_points

broken_water_points =d.get_data(select=['communities_villages'],query={'water_functioning': False})
#print 'Villages with broken water points %s' % len(broken_water_points)

summary = d.get_summary()

print 'Water point lift mechanism type summary %s' % summary['water_lift_mechanism_type']

