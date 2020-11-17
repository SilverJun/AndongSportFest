from flask import Flask, request
from flask_restful import Resource, Api
from os import system

from datetime import datetime

app = Flask(__name__)
api = Api(app)


class NotionUploadRequest(Resource):
    def post(self):
        # 리퀘스트 내용
        content = request.json
        print(content)
        command = "python3 notion_uploader.py"
        command += " \"" + content['title'] + "\""
        command += " " + content['tag']
        command += " " + content['video']
        if 'images' in content:
            command += " --images=\"" + content['images'] + "\""

        command += " &"

        print(command)
        system(command)
        return {'result': 'ok'}


api.add_resource(NotionUploadRequest, '/upload')
app.run(host="0.0.0.0")

# python3 notion_uploader.py "복주초 남자줄넘기 5학년 김은규" 줄넘기 https://drive.google.com/open?id=176X1z1rEkREPUepUejZsxnUaIGPAqP2D --images="https://drive.google.com/open?id=1JJEfx_EXRTzeSsnAHNmpqqShZ3iI4d7y"
