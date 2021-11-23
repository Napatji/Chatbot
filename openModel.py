import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import joblib

def thumnaii(num,start=None,stop = None):
     model = None
     if start == 0 and stop == 9:
          model = joblib.load(open('10_model.sav', 'rb'))
     elif start == 10 and stop == 19:
          model = joblib.load(open('10-19_model.sav', 'rb'))
     elif start == 20 and stop == 29:
          model = joblib.load(open('20-29_model.sav', 'rb'))
     elif start == 30 and stop == 39:
          model = joblib.load(open('30-39_model.sav', 'rb'))
     elif start == 40 and stop == 49:
          model = joblib.load(open('40-49_model.sav', 'rb'))
     elif start == 50 and stop == 59:
          model = joblib.load(open('50-59_model.sav', 'rb'))
     elif start == 60 and stop == 69:
          model = joblib.load(open('60-69_model.sav', 'rb'))
     elif start == 70 and stop == None:
          model = joblib.load(open('70_model.sav', 'rb'))
     ii = num                                                 #1-80 คือ ข้อมูลเรา เรื่มทำนาย 81 จะตรงวันวันที่ 11 เดือน11 2021
     idxlist =[]
     for i in range (20):                                     #ทำนายเป็นช่วง ปรับช่วงตรงrange
          idxlist.append(ii) 
          ii += 1
     
     xx = np.array(idxlist).reshape(-1,1)                    # reshape
     degTemp = 2                                             # ปรับ degree ให้ตรงกับ model
     poly_features = PolynomialFeatures(degree=degTemp)      
     xxpol = poly_features.fit_transform(xx)                 #เอาตัวแปรมารับค่าหลังแปลง degree
     pre = model.predict(xxpol)  
     return pre[0][0]

#โหลดmodel มาเก็บไว้ในตัวแปร
# model = joblib.load(open('Chatbot/20-29_model.sav', 'rb'))
# ii = 81                                                 #1-80 คือ ข้อมูลเรา เรื่มทำนาย 81 จะตรงวันวันที่ 11 เดือน11 2021
# idxlist =[]
# for i in range (20):                                     #ทำนายเป็นช่วง ปรับช่วงตรงrange
#      idxlist.append(ii) 
#      ii += 1
    
# xx = np.array(idxlist).reshape(-1,1)                    # reshape
# degTemp = 2                                             # ปรับ degree ให้ตรงกับ model
# poly_features = PolynomialFeatures(degree=degTemp)      
# xxpol = poly_features.fit_transform(xx)                 #เอาตัวแปรมารับค่าหลังแปลง degree

# pre = model.predict(xxpol)                              #เอาตัวแปรมารับผลการทำนาย
# a=0
# print(pre[0][0])
# for i in pre:                                             #แสดงค่า
#     print(f'ผลการทำนายวันที่่ {idxlist[a]-70} พ.ย. 2021 -> {int(*i)}')
#     a+=1
