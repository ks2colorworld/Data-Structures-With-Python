from match import check_match_brackets


# str = '(2+5)*7-((3-1)/2+7)'
str = '())' # false 
print(check_match_brackets(str))