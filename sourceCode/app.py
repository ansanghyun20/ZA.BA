
import numpy as np
import time
import tensorflow as tf
import ssl
import time
import pymysql
import concurrent.futures

from threading import Thread
from flask_cors import CORS
from tensorflow.keras.models import load_model # 인공지능 관련 라이브러리

from flask import Flask, request
from flask_restx import Resource, Api # flask 서버 관련 라이브러리
import threading

squatModel = load_model('../Model/model_squat.h5') # 스쿼트 포즈 추정모델을 사용하기 위함
pushupModel = load_model('../Model/model_pushup.h5') # 푸쉬업 모델
plankModel = load_model('../Model/model_plank.h5')
situpModel = load_model('../Model/model_situp.h5')
lungeModel = load_model('../Model/model_lunge.h5') 

app = Flask(__name__)
api = Api(app)

CORS(app)

todos = {}
count = 1
result = {}

def AI(userName, exercise, name, postData):
    conn = pymysql.connect(
    user = 'zaba',
    passwd = '0000',
    host = '211.253.100.186',
    port = 8081,
    db = 'health',
    charset = 'utf8'
)
    
    if exercise == "kind_squat":
            reshapeData = np.array(list(map(int,postData)))
            modelPredict = squatModel.predict(np.reshape(reshapeData, (1,2,14)))
            cnt = 0
            
            if list(modelPredict[0]).index(max(modelPredict[0])) == 0:
                if result.get(name) == "Squat":
                        curs = conn.cursor()
                        #sql = "UPDATE CountExercise set Squat = Squat + 1 where UserName = %s"
                        sql = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s,1,0,0,0,0)"
                        userName = userName.replace(" ","")
                        curs.execute(sql, userName)
                        conn.commit()
                        conn.close()
                        cnt += 1
                result[name] = "Stand"
            elif list(modelPredict[0]).index(max(modelPredict[0])) == 1:
                result[name] = "Squat"
            elif list(modelPredict[0]).index(max(modelPredict[0]))==2:
                result[name] = "Bent"
            print(result[name])
            print(userName)

    if exercise == "kind_pushup":
            reshapeData = np.array(list(map(int,postData)))
            modelPredict = pushupModel.predict(np.reshape(reshapeData, (1,2,14)))
            if list(modelPredict[0]).index(max(modelPredict[0])) == 0:
                if result.get(name) == "Good":
                        curs = conn.cursor()
                        #sql = "UPDATE CountExercise set Squat = Squat + 1 where UserName = %s"
                        sql = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s,0,0,1,0,0)"
                        userName = userName.replace(" ","")
                        curs.execute(sql, userName)
                        conn.commit()
                        conn.close()
                        cnt += 1
                result[name] = "Ready"
            elif list(modelPredict[0]).index(max(modelPredict[0])) == 1:
                result[name] = "Good"
            elif list(modelPredict[0]).index(max(modelPredict[0]))==2:
                result[name] = "Bad"
# 쓰레드 풀, 동작 원리 작성 (메뉴ㄹ얼)                
    if exercise == "kind_plank":
            reshapeData = np.array(list(map(int,postData)))
            modelPredict = plankModel.predict(np.reshape(reshapeData, (1,2,14)))
            if list(modelPredict[0]).index(max(modelPredict[0])) == 0:
                result[name] = "Ready"
            elif list(modelPredict[0]).index(max(modelPredict[0])) == 1:
                
                result[name] = "Good"
                #curs = conn.cursor()
                #sql = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s,0,1,0,0,0)"
                #userName = userName.replace(" ","")
                #curs.execute(sql, userName)
                #conn.commit()
                #conn.close()
                #cnt += 1
            elif list(modelPredict[0]).index(max(modelPredict[0]))==2:
                result[name] = "Bad"

    if exercise == "kind_situp":
            reshapeData = np.array(list(map(int,postData)))
            modelPredict = situpModel.predict(np.reshape(reshapeData, (1,2,14)))
            if list(modelPredict[0]).index(max(modelPredict[0])) == 0:
                if result.get(name) == "Good":
                        curs = conn.cursor()
                        #sql = "UPDATE CountExercise set Squat = Squat + 1 where UserName = %s"
                        sql = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s,0,0,0,0,1)"
                        userName = userName.replace(" ","")
                        curs.execute(sql, userName)
                        conn.commit()
                        conn.close()
                        cnt += 1
                result[name] = "Ready"
            elif list(modelPredict[0]).index(max(modelPredict[0])) == 1:
                result[name] = "Good"
            elif list(modelPredict[0]).index(max(modelPredict[0]))==2:
                result[name] = "Bad"

    if exercise == "kind_lunge":
            reshapeData = np.array(list(map(int,postData)))
            modelPredict = lungeModel.predict(np.reshape(reshapeData, (1,2,14)))
            if list(modelPredict[0]).index(max(modelPredict[0])) == 0:
                result[name] = "Ready"
               # if result.get(name) == "Good":
                       # curs = conn.cursor()
                        #sql = "UPDATE CountExercise set Squat = Squat + 1 where UserName = %s"
                       # sql = "INSERT INTO count_table(user_name, squat, plank, pushup, lunge, situp) values(%s,0,0,0,1,0)"
                       # userName = userName.replace(" ","")
                       # curs.execute(sql, userName)
                       # conn.commit()
                       # conn.close()
                       # cnt += 1
                
            elif list(modelPredict[0]).index(max(modelPredict[0])) == 1:
                result[name] = "Good"
            elif list(modelPredict[0]).index(max(modelPredict[0]))==2:
                result[name] = "Bad"

@api.route('/todos')
class TodoPost(Resource):
    def post(self):
        global count
        global todos
        global result
        idx = count
        count += 1

        exercise = request.json.get('kind')
        name = request.json.get('name')
        postData = request.json.get('data')
        userName = request.json.get('userName')

        if not userName:
            pass
        else:
            thread = concurrent.futures.ThreadPoolExecutor(max_workers=5)
            thread.submit(AI, userName,exercise,name,postData)
            #thread = Thread(target=args, AI=(userName,exercise,name,postData))
            #thread.daemon = True
            #thread.start()
            print("ExerciseKind:", exercise)
            print("userName:", userName)
            userName=""

        #return {
        #    'name': name,
        #    'data': postData
        #}

        
@api.route('/todos/result')
class TodoSimple(Resource):
    def get(self):
        return {
            'AllData': result,
        }


    

if __name__ == "__main__":
 #   ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
#    ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    app.run(debug=True, host='10.0.2.15' ,port = 5000, threaded = True) #, ssl_context=ssl_context)
