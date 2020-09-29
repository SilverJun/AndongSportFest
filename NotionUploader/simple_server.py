from flask import Flask, request
from flask_restful import Resource, Api
from os import system

app = Flask(__name__)
api = Api(app)


class NotionUploadRequest(Resource):
    def post(self):
        # 리퀘스트 내용
        content = request.json
        print(content)
        command = "python3 notion_uploader.py"
        command += " " + content['title']
        command += " " + content['tag']
        command += " " + content['video']
        if 'images' in content:
            command += " --images=\"" + content['images'] + "\""

        command += " &"

        print(command)
        system(command)
        return {'result': 'ok'}


api.add_resource(NotionUploadRequest, '/upload')

# if __name__ == '__main__':
#     app.run(debug=True)
