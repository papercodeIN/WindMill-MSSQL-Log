
Used: This code is created to store Individual Wind Trubine Data into MSSQL Server at Interval of 15 Minute.

Note - Interverl is Set into MS Windows Task Scheduler.

Note - Do necessary change before using this code.

Sample CSV Data:

|LocalTime     |Turbine              |WspAvg(m/s)|WindDirAvg(Deg)|NacelPos(Deg)|Power(kW)|SecBrakeActive(s)|SecGridConnection(s)|AmbientTemp(C)|
|--------------|---------------------|-----------|---------------|-------------|---------|-----------------|--------------------|--------------|
|20210816110000|SWSMAM-SC1-GAC12-VM79|3.1        |1.4            |273.2        |-1.3     |0                |0                   |28.6          |
|20210816111000|SWSMAM-SC1-GAC01-VM26|3.3        |-1             |213.2        |-1.8     |0                |0                   |31            |
|20210816111000|SWSMAM-SC1-GAC02-VM28|3.3        |-3.6           |224.7        |-4.1     |0                |0                   |31.6          |
|20210816111000|SWSMAM-SC1-GAC03-VM29|3.2        |-2.1           |212.1        |-1.9     |0                |0                   |32            |
|20210816111000|SWSMAM-SC1-GAC10-VM30|3.3        |8.4            |218.1        |-1.8     |0                |0                   |31            |


MSSQL Databse and Table Result:

![Result Image](https://github.com/papercodeIN/WindMill-MSSQL-Log/blob/main/Result/Result.png)
