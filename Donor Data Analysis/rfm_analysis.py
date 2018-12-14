""" Performs an RFM analysis on data from CSV file """

import csv
import numpy as np
import pandas as pd
from itertools import tee

NUM_SEGMENTS = 4

def recency(donation_amts):
    """ Calculates the most recent year that a donor made a contribution, and 
    gives each donor a recency score.

    Recency score is calculated by splitting the timespan of the data into equal
    segments, with donors who contributed within the bounds of the most recent 
    segment receiving the highest score.
    
    Args:
        donation_amts: A DataFrame with the amount each donor contributed, by 
        year, with donor IDs as the index.

    Returns: A DataFrame containing two columns: years since last donation, and 
        recency score.
    """

    most_recent_donations = {}
    years_in_timespan = donation_amts.columns

    # Create a dictionary that maps the most recent donation to a donor ID
    for index, row in donation_amts.iterrows():
        most_recent_donations[index] = get_most_recent_donation(row)

    years_since_last_donation = pd.Series(
                                         most_recent_donations, 
                                         name='years_since_last_donation')

    # Create a list of evenly spaced groups within the timespan of the data. 
    # i.e. : [(0,2.5), (2.5,5), (5,7.5), (7.5,10)]
    score_groups = list(pairwise(np.linspace(0,len(years_in_timespan), NUM_SEGMENTS + 1)))

    # Use apply function to generate a series of recency scores for each donor 
    # based on the score_groups created above.
    recency_scores = pd.Series(
                              years_since_last_donation.apply(recency_score, 
                              args=(score_groups,)), 
                              name='recency')
    return pd.concat([years_since_last_donation, recency_scores], axis=1)

def frequency(donation_counts):
    """ Calculates how many times a donor made a contribution over the time 
    period of the input data, and gives each donor a frequency score.
    
    Frequency score is calculated by splitting the number of possible donations
    (i.e. the timespan of the data) into equal segments, with those donating the
    most receiving the highest score.

    Args:
        donation_counts: A DataFrame with the number of times each donor 
            contributed, by year, with donor IDs as the index. (This should work 
            equally well with donation amount data, since we are just seeing if 
            they donated at all for a given year.
            
    Returns: A DataFrame containing two columns: number of years donated, and 
        frequency score.
    """
    
    # Create True/False array for DataFrame based on if a donor donated or not 
    # in a given year, and then sum the True responses.
    years_donated = pd.Series(
                             donation_counts.astype(bool).sum(axis=1), 
                             name='years_donated')

    # Create a list of evenly spaced groups within the timespan of the data.                              
    num_possible_years = len(donation_counts.columns)

    # Create score_groups based on maximum number of donations possible over the
    # timespan of the data.
    score_groups = list(pairwise(np.linspace(
                                            0, 
                                            num_possible_years, 
                                            NUM_SEGMENTS + 1)))

    # Use apply function to generate a series of frequency scores for each donor 
    # based on the score_groups created above.
    frequency_scores = pd.Series(
                                years_donated.apply(
                                                   score,
                                                   args=(score_groups,)), 
                                                   name='frequency')
    return pd.concat([years_donated, frequency_scores], axis=1)

def monetary_value(donation_amts):
    """ Calculates the amount of money a donor has contributed, and gives each 
    donor a monetary value score.
    
    Monetary value score is calculated by grouping the donations by percentile, 
    with donors in the highest percentile group receiving the highest score.
    
    Args:
        donation_amts: A DataFrame with the amount each donor contributed, by 
        year, with donor IDs as the index.
        
    Returns: A DataFrame with 2 columns: the total donations for each donor of
        the timespan of the data, and their monetary value score.
    """

    # Sum the yearly donations for each donor, excluding those who did not 
    # donate.
    total_donations = pd.Series(
                               donation_amts.sum(axis=1), 
                               name='total_donations')
    zero_excluded_donations = total_donations[total_donations > 0]

    # Create list of quantiles (and their values for given data) that you are 
    # interested in examining.
    quantile_ranges = get_quantile_ranges(zero_excluded_donations, NUM_SEGMENTS)

    # Use the apply function to generate monetary value scores based on 
    # percentile ranges.
    monetary_value_scores = pd.Series(
                                     total_donations.apply(
                                                            score, 
                                                            args=(quantile_ranges,)), 
                                     name='monetary_value')
    return pd.concat([total_donations, monetary_value_scores], axis=1)

def get_most_recent_donation(row):
    """ Gets the most recent donation for a donor when the columns are donations
    by year.

        Args:
            row: A row in a DataFrame.
        
        Returns:
            years_since_last_donation: The number of years since the last 
            donation for a given donor. Returns NaN if there in no record of any
            donations.
    """

    years_since_last_donation = 0
    for item in row:            
        if(item > 0):         
            return years_since_last_donation
        years_since_last_donation += 1
    return np.nan

def get_quantile_ranges(data, num_segments):
    quantiles = np.linspace(0,1,num_segments + 1)
    quantile_values = data.quantile(quantiles).values
    return list(pairwise(quantile_values))

def pairwise(iterable):
    """ Taken from https://docs.python.org/3.6/library/itertools.html#recipes
    Useful tool to iterate over list using a "sliding window" 2 items wide.
    "s -> (s0,s1), (s1,s2), (s2, s3), ..." 
    """
    
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def score(x, ranges):
    """ Calculates a frequency or monetary value score for a given data point.

    Args:
        x: A data point (total donation, number of donations) from a Series
        ranges: List of tuples containing the upper and lower bounds for 
        segments.

    Returns: The score based on the range in which a data point (x) is 
    contained.
    """
    for index, item in enumerate(ranges):
        if(x == 0):
            return 0
        if(item[0] <= x and x <= item[1]):
            return index + 1

def recency_score(x, ranges):
    """ Calculates the recency score for a given data point.

    Args:
        x: A data point corresponding to the years since last donation
        ranges: List of tuples containing the upper and lower bounds for 
        segments.

    Returns: The recency score based on the range in which a data point (x) is 
    contained. Returns NaN if the donor never donated in the timespan of the 
    data.
    """

    for index, item in enumerate(ranges):
        if(np.isnan(x)):
            return 0
        if(item[0] <= x and x < item[1]):
            return 4 - index   
    
donation_amts = pd.read_csv('gift_amounts_by_year.csv', 
    index_col='Constituent ID')
donation_counts = pd.read_csv('gift_counts_by_year.csv', 
    index_col='Constituent ID')

rfm_data = pd.concat([recency(donation_amts),
    frequency(donation_counts), 
    monetary_value(donation_amts)], axis=1)
rfm_data['rfm_score'] = (rfm_data['monetary_value'] 
    + rfm_data['frequency'] + rfm_data['recency'])
print(rfm_data)