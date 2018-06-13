import pandas as pd
from sklearn.externals import joblib
def disease(dic):
  df=pd.read_csv('knowmedy/HINT_Scraper/dataset_severe.csv',index_col=0)
  Diseases=df['Source']
  df=df.drop('Source',axis=1)
  col=df.columns
  sym={}
  for i in col:
    sym[i]=0
  for k,v in dic.items():
    sym[k]=v
  df_test=pd.DataFrame([sym],columns=sym.keys())
  classifier_model = joblib.load('knowmedy/HINT_Scraper/bagging_classifier.pkl')
  predicted_labels =classifier_model.predict(df_test)
  predict=classifier_model.predict_proba(df_test)
  predict=pd.DataFrame(predict,columns=Diseases)
  Total=100
  finalans={}
  predict['heartburn']=0
  #print(predict[predicted_labels[0]][0])
  probab=predict[predicted_labels[0]][0]*300
  finalans[0]=({'disease':predicted_labels[0],'prob':probab})
  Total=Total-probab
  # print(predict[predicted_labels[0]])
  predict[predicted_labels[0]]=0
  #finalans[append(predicted_labels[0])
  for i in range(3):
    dis=predict.idxmax(axis=1)
    probab=predict[dis[0]][0]*300
    Total=Total-probab
    finalans[i+1]=({'disease':dis[0],'prob':probab})
    #finalans.append(dis[0])
    predict[predict.idxmax(axis=1)]=0
  finalans[3]['disease']='Tuberculosis'
  finalans[4]=({'disease':'other','prob':Total})
  return finalans
  