from xgboost import XGBRegressor
import pandas as pd
import pickle
data=pd.read_csv('processed_house_data.csv')
xgb=XGBRegressor(learning_rate=0.1, max_depth=4, n_estimators=1000)
print(data.shape)
x=data.drop(columns='price')
y=data['price']
xgb.fit(x,y)
pickle.dump(xgb,open('model.pkl','wb'))
