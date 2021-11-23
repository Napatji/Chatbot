#Import Library
import json
import os
from flask import Flask
from flask import request
from flask import make_response
from openModel import thumnaii as th
from datetime import datetime
# Flask
app = Flask(__name__)
@app.route('/', methods=['POST']) 

def MainFunction():

    #รับ intent จาก Dailogflow
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)

    #เรียกใช้ฟังก์ชัน generate_answer เพื่อแยกส่วนของคำถาม
    answer_from_bot = generating_answer(question_from_dailogflow_raw)
    
    #ตอบกลับไปที่ Dailogflow
    r = make_response(answer_from_bot)
    r.headers['Content-Type'] = 'application/json' #การตั้งค่าประเภทของข้อมูลที่จะตอบกลับไป

    return r

def generating_answer(question_from_dailogflow_dict):
    #Print intent ที่รับมาจาก Dailogflow
    print(json.dumps(question_from_dailogflow_dict, indent=4 ,ensure_ascii=False))

    #เก็บค่า ชื่อของ intent ที่รับมาจาก Dailogflow
    intent_group_question_str = question_from_dailogflow_dict["queryResult"]["intent"]["displayName"] 

    #ลูปตัวเลือกของฟังก์ชั่นสำหรับตอบคำถามกลับ
    if intent_group_question_str == 'ทักทาย':
        answer_str = conversation()
    elif intent_group_question_str == 'ให้น้องทำนายกัน': 
        answer_str = predictCovid(question_from_dailogflow_dict)
    else: answer_str = "หนูไม่เข้าใจ คุณต้องการอะไร"

    #สร้างการแสดงของ dict 
    answer_from_bot = {"fulfillmentText": answer_str}
    
    #แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    
    return answer_from_bot

def conversation():
    word = 'อยากทราบสถานการณ์ช่วงวันที่เท่าไหร่ดีคะ(-^〇^-) เช่น วัน/เดือน/2021'
    answer_function = word
    return answer_function

def predictCovid(respond_dict):
    #เก็บค่าวันที่
    day = int(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["day.original"])
    month = int(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["month.original"])
    year = int(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["year.original"])
    start_age = int(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["start.original"])
    stop_age = int(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["stop.original"])
    #กรณีคนแกล้งน้องทำนาย
    if start_age > stop_age:
        temp = start_age
        start_age = stop_age
        stop_age = temp
    index = 80 + compareDate(day,month,year)
    # answer_function = f'{day}/{month}/{year} = {index}'
    #แสดงการคำตอบ
    if start_age == 70:
        check_covid = int(th(index,start_age))
    else:
        check_covid = int(th(index,start_age,stop_age))
    if check_covid > 0:
        answer_function = f'จะมีผู้ติดเชื้อโควิดโดยประมาณ {check_covid}  คนค่ะ'
    else:
        answer_function = f'น้องทำนายว่าน่าจะไม่มีผู้ติดเชื้อแล้วค่าาา'
    return answer_function

def compareDate(day,month,year):
    d = day
    m = month
    y = year
    date_format = "%m/%d/%Y"
    a = datetime.strptime('11/10/2021', date_format)
    b = datetime.strptime(f'{m}/{d}/{y}', date_format)
    delta = b - a
    return delta.days # that's it

#Flask Main
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)