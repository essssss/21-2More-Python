def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # copy_list =[]
    # for item in lst:
    #     if item:
    #         copy_list.push(item)
    # return copy_list

    return [item for item in lst if item]