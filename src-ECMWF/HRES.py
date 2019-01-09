#####################################################
#                                                   #
#       CDS/ECMWF ERA5 download HRES                #
#                                                   #
#       Olivier den Ouden                           #
#       Royal Netherlands Meteorological Institute  #
#       RD Seismology and Acoustics                 #
#                                                   #
#       https://cds.climate.copernicus.eu/#!/home   #
#                                                   #
#####################################################

#Modules
import cdsapi
c = cdsapi.Client()

#Request data - store it as netCDF
c.retrieve('reanalysis-era5-complete', {
    'class'   : 'ea',
    'expver'  : '1',
    'stream'  : 'oper',
    'type'    : 'an',
    'step'    : '0',
    'param'   : 'sp/10u/10v/2t',
    'levtype' : 'sfc',
    'date'    : '2013-01-01',
    'time'    : '00/to/23/by/1',
    'area'    : 'global', 
    'grid'    : '0.3/0.3', 
    'format'  : 'netcdf', 
}, 'temp-fc-ml.nc')

