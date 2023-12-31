def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?
    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered more than three items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    """

    number_of_items = len(item_prices)  # The variable number_of_items is the length of the list
    
    if number_of_items >= 3:    # If that list is greater than or equal to 3,
                                # return the cheapest item at the lowest from the list
        
        cheapest_item = min(item_prices)

        return cheapest_item
    else:
        return 0    # Else return 0

if __name__ == '__main__':
    main()