"""

Used: This code is created to store Individual Wind Trubine Data into MSSQL Server at Interval of 15 Minute.

Note - Interverl is Set into MS Windows Task Scheduler.
Note - Do necessary change before using this code.

Sample CSV Data:

LocalTime,Turbine,WspAvg(m/s),WindDirAvg(Deg),NacelPos(Deg),Power(kW),SecBrakeActive(s),SecGridConnection(s),AmbientTemp(C)
20210816110000,SWSMAM-SC1-GAC12-VM79,3.1,1.4,273.2,-1.3,0,0,28.6
20210816111000,SWSMAM-SC1-GAC01-VM26,3.3,-1,213.2,-1.8,0,0,31
20210816111000,SWSMAM-SC1-GAC02-VM28,3.3,-3.6,224.7,-4.1,0,0,31.6
20210816111000,SWSMAM-SC1-GAC03-VM29,3.2,-2.1,212.1,-1.9,0,0,32
20210816111000,SWSMAM-SC1-GAC10-VM30,3.3,8.4,218.1,-1.8,0,0,31

Created By: Nakum Urvish

"""

# Import Necessary Library
import pandas as pd
from sqlalchemy import create_engine
import urllib
import pyodbc
import os
import glob

# Get list of all file from given location
# Change the folder location from where you want to take last created file from your system
list_of_files = glob.glob(r"D:\Notebooks\Windmill\FTP_Files\*")
# Get name of last created file
latest_file = max(list_of_files, key=os.path.getctime)
# Read last created file and convert csv file into Pandas Dataframe
raw_csv = pd.read_csv(latest_file)

# Find unique turbine list from last created file
Unique_Turbine = list(raw_csv.Turbine.unique())

# Run a loop : for each unique turbine 
for Unique_VM in Unique_Turbine:

    # Create new temp dataframe for each Windmill
    rslt_df = raw_csv[raw_csv['Turbine'] == Unique_VM ] 

    # Create Connection with MSSQL Server 
    # Change SERVER
    # Change DATABASE
    quoted = urllib.parse.quote_plus(r"DRIVER={SQL Server};SERVER=DESKTOP-0HSOJCR\PARROT;DATABASE=DATA_DB")
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    conn = pyodbc.connect(r'Driver={SQL Server};'
                              'Server=DESKTOP-0HSOJCR\PARROT;'
                              'Database=DATA_DB;')
    cursor = conn.cursor()
    
    # Dump Dataframe data into MSSQL table according to Windmill name
    rslt_df.to_sql(f'{Unique_VM}', schema='dbo', con = engine, chunksize=650, method='multi', index=False, if_exists='append')

    # Close connection with pyodbc engine
    engine.dispose()

