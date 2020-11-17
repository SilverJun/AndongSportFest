from notion.client import NotionClient
from notion.block import HeaderBlock, VideoBlock, ImageBlock, CollectionViewBlock
import click
from google_drive_downloader import GoogleDriveDownloader as gdd
from datetime import datetime
import os
import magic
import moviepy.editor as moviepy

TOKEN = "ad0ad723495c3659cae0ea1c65b50778249660a96d8fe3ae7b5fa1cdaa269eca53b22346885d8cf049412178561d66b0e1893c9571cddf2f82c7d1110f2ae9a4cac358d39487373bc99dcc65e972"
PAGE_URL = "https://www.notion.so/silverjun/2020-39c8c4f395a94e828082361da8a7d529"


@click.command()
@click.argument('title')
@click.argument('tag')
@click.argument('video')
@click.option('--images', type=click.STRING, default=None)
def NotionUpload(title, tag, video, images):
    print("Notion Uploader will upload with these:")
    print(title, end=' ')
    print(tag, end=' ')
    print(video, end=' ')
    print(images)
    client = NotionClient(token_v2=TOKEN)
    page = client.get_block(PAGE_URL)
    # print(page.children)

    # archive 데이터베이스 가져오기.
    archiveCollection = page.children.filter(CollectionViewBlock)[-1]
    # print(archiveCollection)

    newVideoRow = archiveCollection.collection.add_row()
    newVideoRow.title = title
    newVideoRow.Tags = tag

    headerBlock = newVideoRow.children.add_new(HeaderBlock)
    headerBlock.title = "영상"

    googleDrivePath = "https://drive.google.com/uc?id="

    now = datetime.now()
    date_time = now.strftime("%Y%m%d_%H%M%S")
    filepostfix = date_time;
    basepath = "/home/azureuser/notion_uploader/downloads/"
    # basepath = "C:/Users/jange/Desktop/downloads/"
    videoPath = basepath + "video_" + filepostfix
    gdd.download_file_from_google_drive(file_id=video.split('id=')[-1], dest_path=videoPath)

    fileType = magic.from_file(videoPath, mime=True)
    print(fileType)
    if fileType.find("mp4") == -1:  # mp4가 아닌경우
        print("convert start")
        clip = moviepy.VideoFileClip(videoPath)
        videoPath += ".mp4"
        clip.write_videofile(videoPath)
        print("convert done")
    else:
        print("no need to convert")
        os.rename(videoPath, videoPath+".mp4")
        videoPath += ".mp4"

    videoBlock = newVideoRow.children.add_new(VideoBlock)
    videoBlock.upload_file(videoPath)
    # video.upload_file() -> 동영상 파일 embed
    # video.set_source_url() -> 유튜브와 같은 url 연결

    if images is None:
        return

    headerBlock = newVideoRow.children.add_new(HeaderBlock)
    headerBlock.title = "사진"

    images = images.split(',')
    images = [img.strip() for img in images]

    for img in images:
        imageBlock = newVideoRow.children.add_new(ImageBlock)
        gdd.download_file_from_google_drive(file_id=img.split('id=')[-1], dest_path=basepath + "image_" + filepostfix)
        imageBlock.upload_file(basepath + "image_" + filepostfix)

    print("clean up...")
    os.system("rm -f " + videoPath)
    os.system("rm -f " + basepath + "image_" + filepostfix)
    print("clean up done")

    print("%s upload done"%title)
    # 구글 드라이브 파일 raw url
    # https://drive.google.com/uc?id=XXX
    # https://drive.google.com/uc?id=1wU0H_5M0CneRBjc-V7YdBbImg9COSB1x

if __name__ == '__main__':
    NotionUpload()
