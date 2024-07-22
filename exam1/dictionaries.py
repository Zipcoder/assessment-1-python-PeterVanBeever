#import counter
from collections import Counter

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    # del keys
    for key in keylist:
        # if found
        if key in datadict:
            # delete from dict @ key
            del datadict[key]
    return datadict
        

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    # return (key in datadict.key)
    return (key in datadict.values())
    pass

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    # get min 
    return min(ddd, key = ddd.get)
    pass

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return max(ddd, key = ddd.get)
    pass

def letterfreq(word):
    '''
    # Write a function that returns a dictionary of letter frequencies from a word
    '''
    # use counter, import
    return Counter(word)
    pass