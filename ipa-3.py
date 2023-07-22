'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    from_mem_info = social_graph[from_member]
    to_mem_info = social_graph[to_member]

    from_mem_following = from_mem_info["following"]
    to_mem_following = to_mem_info["following"]

    if (to_member in from_mem_following) and (from_member in to_mem_following):
        return "friends"
    elif (to_member in from_mem_following):
        return "follower"
    elif (from_member in to_mem_following):
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #horizontal
    for row in board:
        if len(set(row)) == 1:
            if set(row) == {''}:
                return 'NO WINNER'
            else:
                return row[0]
        
    #vertical
    for col in range(len(board[0])):
        column = [board[row][col] for row in range(len(board))]
        if len(set(column)) == 1:
            if set(column) == {''}:
                return 'NO WINNER'
            else:
                return column[0]

    #diagonal   
    diagonal = [board[i][i] for i in range(len(board))]
    if len(set(diagonal)) == 1:
        if set(diagonal) == {''}:
            return 'NO WINNER'
        else:
            return diagonal[0]
    
    diagonal2 = [board[i][len(board) - 1 - i] for i in range(len(board))]
    if len(set(diagonal2)) == 1:
        if set(diagonal2) == {''}:
            return 'NO WINNER'
        else:
            return diagonal2[0]
    
    return 'NO WINNER'

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    start_leg_index = ""
    legs_keys = tuple(route_map.keys())

    # finding where start stop is first stop
    for leg in range(len(legs_keys)):
        if legs_keys[leg][0] == first_stop:
            start_leg_index = leg
    
    # if input is not im map
    if start_leg_index == "": 
        eta = 'First stop not found. Please try again.'
    
    # getting eta
    current_leg = start_leg_index
    eta = 0

    while legs_keys[current_leg - 1][1] != second_stop:
        eta = eta + route_map[legs_keys[current_leg]]["travel_time_mins"]
        if current_leg + 1 >= len(legs_keys): # destination has already been passed 
            current_leg = 0
        elif current_leg + 1 < len(legs_keys):
            current_leg = current_leg + 1

    return eta
    