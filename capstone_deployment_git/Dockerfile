FROM python:3.10.2

COPY ./bert_dic_list.txt /deploy/
COPY ./complete_filtered_train_movie_id_list.txt /deploy/
COPY ./Dockerfile /deploy/
COPY ./filtered_movie_id_mapping_list.txt /deploy/
COPY ./filtered_rank_dic_list.txt /deploy/
COPY ./filtered_user_id_mapping_list.txt /deploy/
COPY ./hybrid_recommender_app.py /deploy/
COPY ./hybrid.h5 /deploy/
COPY ./movie_id_vs_movie_title_list.txt /deploy/
COPY ./requirements.txt /deploy/

WORKDIR /deploy/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "hybrid_recommender_app.py"]
