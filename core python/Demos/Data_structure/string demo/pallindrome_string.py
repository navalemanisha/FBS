def chkpallindromestring(str):
    rev_str =''
    for char in str:
        rev_str = char + rev_str
        # print(rev_str)
    if(str == rev_str):
        print('the srting is pallindrome.')
    else:
        print('the srting is not pallindrome.')

str = 'madam'
chkpallindromestring(str)
            