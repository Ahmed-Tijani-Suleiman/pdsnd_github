import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    data_list = {'city':['chicago', 'new york city', 'washington'],
                 'month':['none', 'january', 'february', 'march', 'april', 'may', 'june'],
                 'day': ['none', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday','sunday']
                 }
    data_value= []
    for index, value in data_list.items():
        while True:
            try:
                data_input = input('please select a {}. select none for no filter \n'.format(index)).lower().strip()
                if data_input not in value:
                    raise Exception
                data_value.append(data_input)
                break
            except:
                print('Enter a valid {} name'.format(index))
    city, month, day= data_value                  
    print('-'*40)
    return city, month, day
def filters(month_value, day_value):
    if month_value =='none' and day_value != 'none':
        value= 'day'
    elif month_value != 'none' and day_value == 'none':
        value= 'month'
    elif month_value != 'none' and day_value != 'none':
        value = 'both'
    else:
        value= 'no filter'
    return value

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month']= df['Start Time'].dt.month_name()
    df['day']= df['Start Time'].dt.day_name()
    df['hour']= df['Start Time'].dt.hour
    if month != 'none':
        df = df[df['month'] == month.title()]
    if day != 'none':
        df = df[df['day'] == day.title()]


    return df



def time_stats(df, filter_value):
   
    """Displays statistics on the most frequent times of travel.
       Displays:
       Most common month, day and Hour.
    
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    list1= ['month', 'day', 'hour']
    for i in list1:
        start_time = time.time()
        value= df[i].mode()[0]
        count = (df[i] == df[i].mode()[0]).sum()
        print(' The most common {} is:{}, with a count of: {}. filter: {}'.format(i,value, count,filter_value))
        print("This took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df, filter_value):
    """Displays statistics on the most popular stations and trip.
       Displays:
       most commonly used start station
       most commonly used end station
       most frequent combination of start station and end station trip
    """
    print('Calculating The Most Popular Stations and Trip...\n')
    list2 = ['Start Station', 'End Station']
    for i in list2:
        start_time = time.time()
        value = df[i].mode()[0]
        count = (df[i] == df[i].mode()[0]).sum()
        print(' The most common {} is:{}, with a count of: {}. filter: {}'.format(i,value, count,filter_value))
        print("This took %s seconds.\n" % (time.time() - start_time))
    # TO DO: display most commonly used start station
    # TO DO: display most commonly used end station
    # TO DO: display most frequent combination of start station and end station trip
    start_time = time.time()
    frequent_combo = (df['Start Station'] +' to '+ df['End Station']).mode()[0]
    count = (df['Start Station'] +' to '+ df['End Station'] == (df['Start Station'] +' to '+ df['End Station']).mode()[0]).sum()
    print(' The most common frequent combination  of start station and end station trip is:{}, with a count of: {}. filter: {}'.format(frequent_combo,count,filter_value))
    print("This took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, filter_value):
    """Displays statistics on the total and average trip duration.
       Displays:
       total travel time
       mean travel time
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = (df['End Time'] - df['Start Time']).sum()
    print(' The total travel time is:{}, filter: {}'.format(total_travel_time,filter_value))
    print("This took %s seconds.\n" % (time.time() - start_time))
    # TO DO: display mean travel time
    mean_travel_time = (df['End Time'] - df['Start Time']).mean()
    print(' The mean travel time is:{}, filter: {}'.format(mean_travel_time,filter_value))
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, filter_value):
    """ Displays statistics on bikeshare users.
        Displays:
        counts of user types
        counts of gender
        earliest, most recent, and most common year of birth
    """
    print('\nCalculating User Stats...\n')
    list3= ['User Type', 'Gender']
    for i in list3:
        start_time = time.time()
        value = df[i].value_counts()
        print(' Value count for {}: {}, filter: {}'.format(i,value,filter_value))
        print("This took %s seconds.\n" % (time.time() - start_time))
   
    start_time = time.time()
    earliest = df['Birth Year'].min()
    most_recent = df['Birth Year'].max()
    most_common= df['Birth Year'].mode()[0]
    print('The Earliest birth year is: {}, Most recent is : {} and Most common is: {}. Filter: {}'.format(earliest, most_recent, most_common,filter_value))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        filter_value= filters(month,day)
        time_stats(df,filter_value )
        station_stats(df, filter_value)
        
        trip_duration_stats(df, filter_value)
        if city in ['chicago', 'new_york_city']:
            user_stats(df, filter_value)
        
        start_index=0
        end_index=5
        data_view= input('\nWould you like to see raw data? Enter yes or no.\n').lower()
        while data_view == 'yes':
            print(df.iloc[start_index:end_index])
            data_view= input('\nWould you like to see more raw data? Enter yes or no.\n').lower()
            if data_view == 'no':
                break
            start_index += 5
            end_index +=5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
