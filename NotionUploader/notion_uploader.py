from notion.client import NotionClient
from notion.block import HeaderBlock, VideoBlock, ImageBlock, CollectionViewBlock
import click


TOKEN = ""
PAGE_URL = ""


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

    videoBlock = newVideoRow.children.add_new(VideoBlock)
    videoBlock.set_source_url(googleDrivePath+video.split('id=')[-1])
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
        imageBlock.set_source_url(googleDrivePath+img.split('id=')[-1])

    print("%s upload done"%title)
    # 구글 드라이브 파일 raw url
    # https://drive.google.com/uc?id=XXX
    # https://drive.google.com/uc?id=1wU0H_5M0CneRBjc-V7YdBbImg9COSB1x

if __name__ == '__main__':
    NotionUpload()
