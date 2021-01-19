# https://numpy.org/doc/stable/reference/index.html
# https://pandas.pydata.org/pandas-docs/stable/reference/
# https://stackoverflow.com/questions/tagged/pandas

import pandas as pd
import functions as func

def main():
    print('\t'*3, '#'*29)
    print('\t'*3, '# Explore US BikeShare Data #')
    print('\t'*3, '#'*29)
        
    while True:         
        city, month, day = func.get_filters()
        #print(city, month, day)
        df = func.load_data('new york city', '', 0)
        df = func.load_data(city, month, day)
        #print(df)
        func.time_stats(df)
        func.station_stats(df)
        func.trip_duration_stats(df)
        func.user_stats(df, city)
        
		# I was not aware that I have to display the dataframe 5 rows at a time as per user request
        # SORRY, I must have missed that during reading the project requirements
        func.display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()
