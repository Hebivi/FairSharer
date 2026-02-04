def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
In each iteration the highest value in "values" gives a fraction (share)
to both the left and right neighbor. The leftmost field is considered
the neightbor of the rightmost field.
Examples:
fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
Args
values:
1D array of values (list or numpy array)
num_iteration:
Integer to set the number of iterations
"""

    for _ in range(num_iterations):

        # Looking for the highest value and its index in the list
        max_value = max(values)
        max_index = values.index(max_value)

        # Amount given to each neighbor (in this case the highest value * 0.1)
        sharing = max_value * share

        n = len(values)
        # Neighbor indices in circulat way
        left = (max_index - 1) % n
        right = (max_index + 1) % n

        # Add to left and right neighbors and subtract both given amounts from the original max value
        values[left] += sharing
        values[right] += sharing
        values[max_index] -= 2 * sharing

    # Returns new overwritten values
    return values
