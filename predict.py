import pandas as pd
import time


def predict_sentiment(user_id,recc_df):
    predict_df=pd.read_csv('sample30_tfidf_predict.csv',index_col='Product')
    dataframe_df=predict_df[predict_df.index.isin(recc_df.loc[user_id].sort_values(ascending=False)[0:20].index)]
    time.sleep(6)
    return dataframe_df 
