import pandas as pd

def get_dur(launch, deadline):
    '''
    Calculate time delta from launch and deadline dates
    '''
    launch_dt = pd.to_datetime(launch)
    deadline_dt = pd.to_datetime(deadline)
    duration = deadline_dt - launch_dt
    duration = duration.dt.days

    return duration

def get_monthyear(date):
    '''
    Pull month and year from datetime object
    '''
    date_dt = pd.to_datetime(date)
    month = date_dt.dt.month
    year = date_dt.dt.year

    return month, year

def predict_to_string(array):
    '''
    Convert model prediction to a string value
    '''

    if array[0][0] == 0:
        return 'The kickstarter is not predicted to succeed.'
    if array[0][0] == 1:
        return 'The kickstarter is predicted to succeed!'
    else:
        return 'ERROR: predict_to_string function not properly formatted.'