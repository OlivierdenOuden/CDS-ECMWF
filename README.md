# CDS-ECMWF ERA5 

The ECMWF ERA5 database has migrated to the Climate data store, CDS https://cds.climate.copernicus.eu/#!/home. To download ERA5 data a couple of steps need te be taken before.

### Install cds - key

Since the database migrated, we have to move with them. Meaning we need a new API-key to request the data. Also some software updates and script modifications are needed:

1. Create account:
https://cds.climate.copernicus.eu/#!/home 
Since ECMWF migrated the database we need an account for this database, and thus an account.
2. Agree licence:
https://cds.climate.copernicus.eu/api-how-to 
Link the account to the licence of agreement.
3. Create API:
Log in, and recieve the API-key. Store this key in the file $HOME/.cdsapirc (in your Unix/Linux environment). 

### Install cds - API software

Besides a new API-key, also a software update/CDS software is required. To do, run in terminal:

<font color=red>pip install cdsapi</font>

### Download data

Now everything is updated and the API-key is stored, we can start changing the original script and get acces to the ECMWF database!

#### Variables

The variables do not change, same names!

https://software.ecmwf.int/wiki/display/CKB/ERA5+data+documentation  
 

|Name Parameter|Units|Short name|
|--|-------------------------------|
|Sea tempreture |K|sst|
|Air temperature (2m) |K|2t|
|Wind u speed (10m)|m s**-1|10u|
|Wind v speed (10m)|m s**-1|10v|
|Wind u speed (100m)|m s**-1|100u|
|Wind v speed (100m)|m s**-1|100v|
|Pressure|Pa|sp|
|Humidity|kg kg**-1|q|

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

In the src folder there are two scripts, based on examples on https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5+data+via+the+ECMWF+Web+API. One script for downloading an entire day (hourly) HRES data (sp/2tr/10u/10v). The other to download and entire day (3hr resolution) of EDA data.
