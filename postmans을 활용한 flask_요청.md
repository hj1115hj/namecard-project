### OpenCv 프로젝트 

* `Flask` 실행
  * mscode 설치
  * postman 설치

> mscode를 설치 한후 다음 코드를 입력한다. 예제코드는 [링크]([https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-3](https://i.kakao.com/docs/skill-response-format#예제-코드-3)) 를 참조.

---



링크를 참조 

```python
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/hi')
def hi():
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "간단한 텍스트 요소입니다."
                    }
                }
            ]
        }
    }
```

* postman으로 응답 유형을 확인

  * get 방식 응답, post 방식으로 응답

    ```python
    from flask import Flask, escape, request
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        name = request.args.get("name", "World")
        return f'Hello, {escape(name)}!'
    
    #post방식과 get방식의 요청에 대한 응답이 가능하다.
    @app.route('/hi',methods = ['POST', 'GET'])
    def hi():
        return {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "간단한 텍스트 요소입니다."
                        }
                    }
            
                ]
            }
        }
    ```

    set FLASK_APP=main.py # 실행할 앱등록

    flask run # 수정된 코드 적용하기

    

    ```
    (base) C:\Users\student\Documents>flask run
     * Serving Flask app "main.py"
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```

    

     

  * postman  확인

     New Collection클릭해서 폴더를 생성하고 New버튼을 클릭해 요청을 만든다 

    get에 요청 url을 넣고 확인 

    ![image-20200115171701513](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200115171701513.png)

  * 요청 확인하기

    http://127.0.0.1:5000/ hi 를입력한다

    

* 구글링 팁  

> 찾기 기능이 없는 문서에서 구글 검색하기

```txt
site:url [검색키워드]
```



* json  request 받고 json으로 응답하기

  * 코드 및 postman 요청화면

  ```python
  
  from flask import Flask, escape, request
  # set FLASK_APP=main.py
  # flask run
   
  app = Flask(__name__)
   
  db = {}
  id = 0
  @app.route('/users', methods=['POST'])
  def create_user():
      global id
      body = request.json
      print(body)
      body['id'] = id
      # todo body에 id를 넣어준다.
      db[str(id)]=body
      id+=1
      return body
  
  @app.route('/users/{id}', methods = ['GET'])
  def select_user():
      return db[id]
  
  def deleted_user():
      pass
  
  def update_user():
      pass
  
  #http응답
  @app.route('/')
  def hello():
      name = request.args.get("name", "World")
      return '<h1>sssss</h1>'
  
  
  
  @app.route('/hi',methods = ['POST', 'GET'])
  def hi():
      return {
          "version": "2.0",
          "template": {
              "outputs": [
                  {
                      "simpleText": {
                          "text": "간단한 텍스트 요소입니다."
                      }
                     
                    
                      
                      
                  }
              ]
          }
      }
  ```

![image-20200115172538187](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20200115172538187.png)



* update,delete 적용 전체코드

```python

from flask import Flask, escape, request
# set FLASK_APP=main.py
# flask run
 
app = Flask(__name__)
 
db = {}
id = 0
@app.route('/users', methods=['POST'])
def create_user():
    global id
    body = request.json
    print(body)
    body['id'] = id
    # todo body에 id를 넣어준다.
    db[str(id)]=body
    id+=1
    return body

#postman 요청 url
# http://127.0.0.1:5000/users/0 
# get 방식으로 key와 value를 만들어서 보내려면 form 에서 요청이 들어와야한다?
@app.route('/users/<id>', methods = ['GET'])
def select_user(id):
    return db[id]


@app.route('/users_/<id>', methods = ['DELETE'])
def deleted_user(id):
    print("삭제할 사용자 : ")
    print(db[id])
    del db[id]
    return db

@app.route('/users', methods=['PATCH'])
def update_user():
    body = request.json
    newid = body['id']
    print(db[newid])
    # todo body에 id를 넣어준다.
    db[newid]=body
    print(db[newid])
    return db[newid]

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return '<h1>sssss</h1>'



@app.route('/hi',methods = ['POST', 'GET'])
def hi():
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "간단한 텍스트 요소입니다."
                    }
                }
            ]
        }
    }

```

