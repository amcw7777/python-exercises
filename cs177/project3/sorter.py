################################### SORTER ######################################
# This function sorts the entries starting from startRow to endRow (inclusive)
# of the given table with respect to the given column according to the
# given order ('ascending' or 'descending').

# @Parameter: table
#   - List of list of the format [[str, int, int],...,[str, int, int]]
# @Parameter: column
#   - Function: Column index of the table
#   - Data typle: Integer
# @Parameter: startRow
#   - Function: Row number where sorting will be started
#   - Data typle: Integer
# @Parameter:
#   - Function: Row number up to which sorting will be done
#   - Data typle: Integer
# @Parameter: order
#   - Data Type: String string datatype.
#   - Possible values: 'ascending', 'descending'
# @Returns the sorted table
#   - List of of list of the format [[str, int, int],...,[str, int, int]]
#
# Example:
# Lets assume a table is like following:
#
# | Italy     | 6 | 1 |
# | Spain     | 4 | 2 |
# | Argentina | 4 | 2 |
# | Brazil    | 1 | 4 |
#
# column = 0 (i.e., the 0-th column)
# startRow = 1
# endRow = 2
# order = 'descending'
#
# sortTable() returns the following:
# | Italy     | 6 | 1 |
# | Argentina | 4 | 2 |
# | Spain     | 4 | 2 |
# | Brazil    | 1 | 4 |
# In this case, sortTable() sorts the table starting from row 1 to row 2
# (inclusive) with respect to column 0 in the descending order. Here, sorting
# will not change the order of row 0 and row 3. Only, rows 1, and 2 will be
# sorted. Finally, returns the updated table
def sortTable(table, column, startRow, endRow, order):

    for i in range(startRow, endRow+1):
        m_index = i
        m_value = table[i][column]
        for j in range(i+1, endRow+1):
            if(order == 'ascending'):
                if(table[j][column] < m_value):
                    m_index = j
                    m_value = table[j][column]
            if(order == 'descending'):

                if(table[j][column] > m_value):
                    m_index = j
                    m_value = table[j][column]
        # swap rows i and max_index
        t = table[i]
        table[i] = table[m_index]
        table[m_index] = t
    return table
