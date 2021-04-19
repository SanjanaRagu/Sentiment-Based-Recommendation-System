from flask import Flask,render_template,request
import pickle
import pandas as pd
from model import result_predict

reccomendation_system=pickle.load(open('reccomendation_system_cosine_new.pickle', "rb"))

app = Flask(__name__)


@app.route("/",methods =["POST","GET"])
def home():
    if request.method == "POST":
        user_id = request.form.get("username")
        user_id=user_id.lower().strip()
        if len(user_id)==0:
            return render_template('Home.html') + 'User Id Empty'
        if user_id not in reccomendation_system.index:
            return render_template('Home.html') + 'Invalid User Id OR User Id Not Presnet'
        else:  
            product_name=reccomendation_system.loc[user_id].sort_values(ascending=False)[0:20].index.tolist()
            result_df=pd.DataFrame(columns=['Product','Positive%','Negative%'])
            for prod in product_name:
                postivper,negativper=result_predict(prod)
                result_df = result_df.append({'Product':prod,'Positive%':postivper,'Negative%':negativper},ignore_index = True)
            result_df.sort_values(by=['Positive%'], inplace=True,ascending=False)
            return render_template('result.html',predict=result_df.head(5),user=user_id) 

    else:
        return render_template('Home.html')  
    

if __name__ == "__main__":
    app.run(debug=True)