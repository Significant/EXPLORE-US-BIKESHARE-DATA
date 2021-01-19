import time as tm
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = {1:'sunday', 2:'monday', 3:'tuesday', 4:'wednesday', 5:'thursday', 6:'friday', 7:'saturday'}

def req_month():
    month = str(input('Which month? "January", "February", "March", "April", "May", "June", or "All": ').lower())
    while True:
        if month in months:
            break
        else:
            month=str(input('Please Enter one of the following months: "January", "February", "March", "April", "May", "June",or "All": ').lower())
            continue
    return month        

def req_day():     
   while True:
    try:
        day = int(input('Which day? Please Type your response as an integer (e.g. 1=Sunday 7=Saturday): '))
    except:
        continue
    if day in days.keys():
        break
    else:
        print('Unrecognized Input!!\n')
        continue
   return day
        
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # if for some reason the user entered none for the filter_type, set variables to default values for testing
    city, month, day = '', '', 0
    filter_type = ['both', 'month', 'day', 'none']
    while True:
        city_entered = str(input('Would you like to see data for "Chicago", "New york city" or "Washington": ').lower())    
        if city_entered in CITY_DATA.keys():
            city = city_entered
            break
        else:
            print('Unrecognized Input!!\n')
            continue
    
    
    while True:
        filter_entered = str(input('Would you like to filter data by "Month", "Day", "Both" or not at all, type "None" for for no time filter: ').lower())
        if filter_entered in filter_type:
            if filter_entered == 'both':
                # get user input for month (all, january, february, ... , june)
                month = req_month()
                # get user input for day of week (all, monday, tuesday, ... sunday)
                day = req_day()
                break
            elif filter_entered == 'month':
                # get user input for month (all, january, february, ... , june)
                month = req_month()
                break
            elif filter_entered == 'day':
                # get user input for day of week (all, monday, tuesday, ... sunday)
                day = req_day()
                break
            elif filter_entered == 'none':
                break
        else:
            print('Unrecognized Input!!!')
            continue
            
    print('_' * 100)
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
    df = pd.read_csv(CITY_DATA[city])
        
    # convert 'Start Time Column to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month from Start Time to create a new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all' and month != '':
        month = months.index(month) + 1
        df = df.loc[df['month'] == month]
    
    if day != 'all' and day != 0:
        df = df.loc[df['day_of_week'] == days[day].title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = tm.time()

    # TO DO: display the most common month
    print('The most common month is:        ',df['month'].mode()[0]) # value_counts().head(1))

    # TO DO: display the most common day of week
    print('The most common day of week is:  ', df['day_of_week'].mode()[0]) # value_counts().head(1))

    # TO DO: display the most common start hour
    print('the most common start hour is:   ', df['Start Time'].dt.hour.mode()[0]) # value_counts().head(1))

    print("\nThis took %s seconds." % (tm.time() - start_time))
    print('-'*100)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = tm.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used End station is:   ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    # df['Start to End'] = df['Start Station'] + df['End Station']
    
    print('The most frequent combination of start station and end station is: ', (df['Start Station'] + ' --> ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (tm.time() - start_time))
    print('-'*100)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = tm.time()

    # TO DO: display total travel time
    print('Total travel time is:    ', str(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time is: ', (df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (tm.time() - start_time))
    print('-'*100)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = tm.time()

    # TO DO: Display counts of user types
    print('The counts of user types are:  \n', str(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if city in ['chicago', 'new york city']:
        print('The counts of Genders are: \n', str(df['Gender'].value_counts()))

        # A miss indentation here made the next 3 code lines go out of the IF-statment scope and caused an error, 
        # since Washington Data file doesn,t contain a 'Gender' or 'Birth Year' records
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliestmost common year of birth is:    ', int(df['Birth Year'].min()))
        print('The most recent common year of birth is:     ', int(df['Birth Year'].max()))
        print('The most common year of birth is:            ', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (tm.time() - start_time))
    print('-'*100)

def display_data(df):
    """
    Displays the dataframe 5 rows by 5 rows as per user request

    Parameters
    ----------
    df : Dataframe

    Returns
    -------
    None.

    """
    index = 0
    view_data = str(input('\nWould you like to view the top 5 rows of individual trip data? Enter yes or no: ')).lower()

    while((view_data == 'yes') and (index < df.shape[0])):
        print(df.iloc[index:index+5])
        index += 5
        view_data = str(input('\nWould you like to view the Next 5 rows of individual trip data? Enter yes or no: ')).lower()
        if view_data == 'yes':
            continue
        break
