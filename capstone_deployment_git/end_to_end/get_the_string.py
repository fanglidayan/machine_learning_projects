# get a string for the 10 predicted movies
def get_the_string(predictions, movie_id_title_dic):
    result = ''
    for i, prediction in enumerate(predictions):
        result += "Top {} recommended movie: {}".format(i+1, movie_id_title_dic[prediction])
        result += "\n"
    return result

