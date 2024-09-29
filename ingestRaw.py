import pandas as pd

def ingestCongressVote():
    dataTypes = {
        'congress': 'Int64',
        'chamber': str,
        'rollnumber': 'Int64',
        'session': 'Int64',
        'clerk_rollnumber': 'Int64',
        'yea_count': 'Int64',
        'nay_count': 'Int64',
        'nominate_mid_1': float,
        'nominate_mid_2': float,
        'nominate_spread_1': float,
        'nominate_spread_2': float,
        'nominate_log_likelihood': float,
        'bill_number': str,
        'vote_result': str,
        'vote_desc': str,
        'vote_question': str,
        'dtl_desccon': str
    }
    congressVotes_raw = pd.read_csv(
        "data/CongressionalVotes.csv",
        dtype= dataTypes,
        parse_dates= [3],
        low_memory= False
    )
    return congressVotes_raw

def ingestMemberVote():
    dataTypes = {
        'congress': 'Int64',
        'chamber': str,
        'icpsr': 'Int64',
        'state_icpsr': 'Int64',
        'district_code': 'Int64',
        'state_abbrev': str,
        'party_code': 'Int64',
        'occupancy': 'Int64',
        'last_means': 'Int64',
        'bioname': str,
        'bioguide_id': str,
        'born': 'Int64',
        'died': 'Int64',
        'nominate_dim1': float,
        'nominate_dim2': float,
        'nominate_log_likelihood': float,
        'nominate_geo_mean_probability': float,
        'nominate_number_of_votes': 'Int64',
        'nominate_number_of_errors': 'Int64',
        'conditional': str,
        'nokken_poole_dim1': float,
        'nokken_poole_dim2': float
    }
    memberIdeas_raw = pd.read_csv(
        "data/MemberIdeology.csv",
        dtype= dataTypes,
        low_memory= False
    )
    return memberIdeas_raw