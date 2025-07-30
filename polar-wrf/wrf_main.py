import sys
sys.path.append('/data/projects/Polar/2025_CW3E_Intern/program/PWRF_Code/')

from wrf_DataServices import WrfDataServices
import xarray as xr

ds_path = '/data/projects/Polar/2025_CW3E_Intern/PWRF/2022-02-07/'
path_out = '/home/k1sumwalt/clean_data/pwrf/2022-02-07/pwrf_all'
wrf_data = WrfDataServices(ds_path, path_out)
wrf_data.run()

ds_6H = wrf_data.ds_6H
print(ds_6H)
