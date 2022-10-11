import numpy as np
import pandas as pd
# import the datetime module
import datetime
from datetime import datetime
from scipy.signal import find_peaks
import calendar




def ts2peak(data,smoothing_coef):
    
    #data contains the  view logs
    #smoothing_coef used to smooth the data



    #Smoothing
    df1=data.rolling(smoothing_coef).mean().iloc[smoothing_coef-1:,:]

    df_peak_timestamps=pd.DataFrame()
    
    # loop through all events in df1 and extract Timestamps,'prominences', 'left_bases', 
    #'right_bases', 'widths', 'width_heights', 'left_ips', 'right_ips' of the peaks in each event

    for event in df1.columns:
        ts = df1[event].index
        ys = df1[event].values
        df = pd.DataFrame({'Timestamp':ts, 'Value':ys})

        idx, properties = find_peaks(df['Value'], prominence=2, width=0.01)

        peak_x = df['Timestamp'][idx].values
        peak_y = df['Value'][idx].values

        peak_timestamp=pd.DataFrame()
        peak_timestamp['Timestamps']=df['Timestamp'][idx].values
        peak_timestamp['right_ips'] = properties["right_ips"]
        peak_timestamp['left_ips'] = properties["left_ips"]
        peak_timestamp['right_bases'] = properties["right_bases"]
        peak_timestamp['left_bases'] = properties["left_bases"]
        peak_timestamp['prominences'] = properties["prominences"]
        peak_timestamp['Value'] = df['Value'][idx].values
        peak_timestamp['widths'] = properties["widths"]
        peak_timestamp['width_heights'] = properties["width_heights"]
        peak_timestamp['days']=[calendar.day_name[my_date.weekday()] for my_date in peak_timestamp['Timestamps'] ]
        peak_timestamp['months']=[h.month for h in peak_timestamp['Timestamps'] ]
        peak_timestamp['year']=[h.year for h in peak_timestamp['Timestamps'] ]

        peak_timestamp['event']=event


        df_peak_timestamps = pd.concat([df_peak_timestamps, peak_timestamp], axis=0)



        #weekAvg=peak_timestamp.groupby(['days','months']).size()/peak_timestamp.groupby('months')['days'].size()
        #weekAvg_df=pd.DataFrame(weekAvg)
        #weekAvg_df.columns=[event]
        #df_peaks = pd.concat([df_peaks, weekAvg_df], axis=1)

        #df_peaks=df_peaks.reset_index()
        df_peak_timestamps['distance_2_peak']=df_peak_timestamps.Timestamps.diff()
        
    return df_peak_timestamps
