import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
	print('test for refactoring')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities=["chicago", "new york city", "washington"]
        city=input("Please enter the desired city: \n").lower()
        if city in cities:
            break
        else:
            print(city + " city is not available")
    print(city)

        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months=["all", "january", "february", "march", "april", "may", "june"]
        month=input("Please enter the desired month: \n").lower()
        if month in months:
            break
        else:
            print(month +" is not available")
    print(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        week_days=["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day=input("Please enter the desired day of week: \n").lower()
        if day in week_days:
            break
        else:
            print(day +" is not available")
    print(day)

    print('-'*40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df.month.mode()[0])

    # TO DO: display the most common day of week
    print(df.day_of_week.mode()[0])

    # TO DO: display the most common start hour
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0])
    

    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])
    
    # TO DO: display most frequent combination of start station and end station trip
    df["combine"]=df["Start Station"]+" "+df["End Station"]
    print(df["combine"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())
    #mean

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    if city in ['new york city','chicago']:   
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print(df['Birth Year'].min())
    
        print(df['Birth Year'].max())
    
        print(df['Birth Year'].mode())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        print_value=input("Would you like to print raw data?\n").lower()
        index=0
        while True:
            if print_value == "yes":
                print(df.iloc[index:index+5])
                index+=5
                print_value=input("Would you like to print raw data?\n").lower()
            elif print_value=="no":
                break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
