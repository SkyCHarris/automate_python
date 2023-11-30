
#! Ideas for Similar Programs

# Identifying patterns of text (and possibly substituting them with the sub() method) has many different potential applications:

#* Find website URLs that begin with http:// or https://
#* Clean up dates in different date formats (such as 3/14/2019, 03-14-2019, and 2015/3/19) by replacing them with dates in a single, standard format
#* Remove sensitive information such as Social Security or credit card numbers
#* Find common typos such as multiple spaces between words, accidentally repeating words, or multiple exclamation marks at the end of sentences


#! Summary

# A computer can search for text quickly, but it must be told precisely what to look for
# Regexes allow you to specify the pattern of characters you're looking for, rather than the exact text itself
# Some word processing and spreasheet apps provide find-and-replace features that allow you to search using regexes

# The re module lets you compile Regex objects
# These objects have several methods:
    # search() -> find a single match
    # findall() -> find all matching instances
    # sub() -> do a find-and-replace substitution of text