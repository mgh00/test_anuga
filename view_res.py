from netCDF4 import Dataset
import numpy as np
import anuga

fid = 'channel3.sww'
nc = Dataset(fid, mode='r')
b = [1,2,3,4]
#print nc.variables

for var in nc.variables:
    print var, var.units, var.shape
