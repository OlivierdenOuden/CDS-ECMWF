#####################################################
#                                                   #
#       CDS/ECMWF ERA5 download EDA                 #
#                                                   #
#       Olivier den Ouden                           #
#       Royal Netherlands Meteorological Institute  #
#       RD Seismology and Acoustics                 #
#                                                   #
#       https://cds.climate.copernicus.eu/#!/home   #
#                                                   #
#####################################################

#Moduel
import cdsapi
c = cdsapi.Client()

#Request data - store it as netCDF
c.retrieve('reanalysis-era5-single-levels',{
        'product_type':     'ensemble_mean',
        'format':           'netcdf',
        'variable':[        '10m_u_component_of_wind',
                            '10m_v_component_of_wind',
                            '2m_temperature',
                            'surface_pressure'],
        'year':             '2015',
        'month':            '01',
        'day':              '01',
        'time':[            '00:00','03:00','06:00',
                            '09:00','12:00','15:00',
                            '18:00','21:00']
},'download.nc')