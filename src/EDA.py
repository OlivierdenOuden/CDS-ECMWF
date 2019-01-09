#####################################################
#                                                   #
#       CDS/ECMWF ERA5 download enda                #
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
    'stream'  : 'enda',
    'type'    : 'em',
    'step'    : '0',
    'param'   : 'sp/2t/10u/10v',
    'levtype' : 'sfc',
    'date'    : '2013-01-01',
    'time'    : '00/to/23/by/3',
    'area'    : 'global', 
    'grid'    : '0.6/0.6', 
    'format'  : 'netcdf', 
}, 'temp-fc-ml.nc')








