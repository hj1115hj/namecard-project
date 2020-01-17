
from flask import Flask, escape, request
from ocr import ocr
import pprint
import urllib.request
import pytesseract
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
                        "text": "스킬임.."
                    }
                }
            ]
        }
    }



@app.route('/test',methods = ['POST', 'GET'])
def test():
    body = request.json
    #pprint.pprint(body)
    url=body['action']['detailParams']['secureimage']['origin']
    #replaceAll= text.replace(",","")
    newurl=url.replace("List(","").replace(")","")
    #print(url)
    #print(newurl)
    return {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    "imageUrl": newurl,
                    "altText": "재전송"
                }
            }
        ]
    }
}




@app.route('/card', methods=['GET','POST'])
def test2():
    body = request.json
    #pprint.pprint(body)
    
    image_url = body['action']['detailParams']['namecard']['origin']
    
    #image_url =image_url.startswith('http://dn-m.talk.kakao.com/talkm')
    #print(image_url)
    with urllib.request.urlopen(image_url) as input:
        with open('./image.jpeg', 'wb') as output:
            output.write(input.read())

    
    result_file = ocr('./image.jpeg')
    #print(result_file)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    result_string =pytesseract.image_to_string(result_file,lang = 'kor+eng')

    result_string=result_string.strip().replace(' ','')
    print(result_string)
    return  {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleText": {
                    "text":result_string
                }
            }
        ]
    }
}


'''
def ocr(file):
    print(file+"명암추출중")
    return ''


if __name__ == 'main':
#flask로 실행하면 이 파일을 참조해서 쓰는 것으로 인식되기 때문에 실행이 안됨
#info = ocr('./img.jpeg')
    ocr("hello")
    print("---")
    #print(info)
'''