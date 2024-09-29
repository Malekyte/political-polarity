# narrow data to clear voting circumstances; reduce inconsistent interpretation with sufficient data size
def transformCongressVote(rawdata):
    resultExclude = ['Passed', 'Failed']
    congressVotes_clean = rawdata.query(
        f"vote_result in {resultExclude}"
    )
    congressVotes_clean = congressVotes_clean.drop(
        columns= [
            'session',
            'rollnumber',
            'clerk_rollnumber',
            'vote_question',
            'vote_desc',
            'dtl_desc'
        ]
    )