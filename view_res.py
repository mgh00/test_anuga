from netCDF4 import Dataset
import numpy as np

fid = 'channel3.sww'
nc = Dataset(fid, mode='r')

#print nc.variables

#for var in nc.variables:
#    print var, var.units, var.shape
