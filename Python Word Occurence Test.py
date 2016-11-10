"""Count words."""
import collections
def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s
    words = s.split()
    counts = []
    for i in range(len(words)):
        counts.append(words.count(words[i]))
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)

    # create word list with no duplicates
    # create accompanying count list
    # remove duplicates and sort both lists based on occurrence
    indices = sorted(range(len(counts)), key=lambda k: counts[k], reverse=True)
    word_list = []
    count_list = []
    for i in indices:
        if words[i] not in word_list:
            word_list.append(words[i])
            count_list.append(counts[i])
    # for each count, create a temp array containing only words with greatest amount of occurrence
    sorted_list = []
    sentinel = count_list[0]
    while sentinel > 0:
        if sentinel in count_list:
            temp = []
            for i in range(len(count_list)):
                if sentinel == count_list[i]:
                    temp.append(word_list[i])
            # sort temp by alphabet
            temp.sort()
            print "in temp: " + str(temp)
            # package both temp word and count values as tuples and append to sorted_list
            if not temp:
                continue
            else:
                for word in temp:
                    item = (word, sentinel)
                    sorted_list.append(item)
            sentinel -= 1
        else:
            sentinel -= 1
            continue
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return sorted_list[:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("london bridge is falling down falling down falling down london bridge is falling down my fair lady", 5)


if __name__ == '__main__':
    test_run()
