# Serve model as a flask application

import end_to_end
import get_the_string as gts

end_to_end.user = end_to_end.tot_user_num
result1 = end_to_end.get_prediction()
result2 = gts.get_the_string(list(end_to_end.filtered_rank_dic.keys())[:10],\
        end_to_end.movie_id_title_dic) 

if result1 == result2:
    print('unit_test_1 is passed')
else:
    print('unit_test_1 failed')
