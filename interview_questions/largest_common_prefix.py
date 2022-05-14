# Given a list of strings, find the longest prefix they have in common.
# If there is no common prefix return an empty string
#
# Problem constraints
# 1. There will always be at least one string in the list

# Our approach for this problems is going to be to start
# the first word as the common prefix and then remove
# letters that don't match in subsequent words.
#
# The alternative would be to build a proper prefix tree
# but that's overkill for this situation

def longest_common_prefix(strs: list[str]) -> str:
    common_prefix = strs[0]
    # We have already processed the first item in the list,
    # only need to process the remaining list items
    for i in range(1, len(strs)):
        new_common_prefix = ''
        for j in range(len(strs[i])):
            if j < len(common_prefix):
                if strs[i][j] == common_prefix[j]:
                    # Note a match with the common prefix
                    new_common_prefix += common_prefix[j]
                else:
                    # We no long match, break early
                    break
            else:
                # No more letters left in the common prefix
                break
        # We carry forward the longest match for this iteration
        common_prefix = new_common_prefix
    
    return common_prefix