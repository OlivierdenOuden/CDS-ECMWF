# CDS-ECMWF ERA5 

### Install cds - key

We need a new API-key to request the data. Also some software updates and script modifications are needed:

1. Create account:
https://cds.climate.copernicus.eu/#!/home 
2. Agree licence:
https://cds.climate.copernicus.eu/api-how-to 
3. Create API:
Log in, and recieve the API-key. Store this key in the file $HOME/.cdsapirc (in your Unix/Linux environment). 

### Install cds - API software

Besides a new API-key, also a software update/CDS software is required. To do, run in terminal:

<font color=red>**pip install cdsapi**</font>

### Download data

Variables:
https://software.ecmwf.int/wiki/display/CKB/ERA5+data+documentation  

#### Product type

There are two types of models we can request; HRES (High RESolution) and EDA (Ensemble Data Assamblation).

The difference is in scripts, see below, by the stream and type of data you request:

HRES
stream = oper (operational)
type = an (analysis)

EDA
stream = enda (ensemble)
type = em (ensemble mean)

#### Temporal resolution

The temporal difference between HRES and EDA is:
HRES = hourly data
EDA = 3hr data

#### Spatial resolution

Also the spatial resolution is different:
HRES = 0.3/0.3 degrees
EDA = 0.68/0.68 degrees


### Code

In the src-ECMWF folder there are two scripts based on https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5+data+via+the+ECMWF+Web+API. In the src-CDS folder there are two scripts based on https://cds.climate.copernicus.eu/#!/home. One script for downloading an entire day (hourly) HRES data (sp/2tr/10u/10v). The other to download and entire day (3hr resolution) of EDA data. I recommend to use CDS database.

### VirtualBox - Linux

When there is trouble downloading/using the scripts, a VirtualBox can be used. I created a VirtualBox which works, when intressted contact me.
