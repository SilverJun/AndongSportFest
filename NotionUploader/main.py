from notion.client import NotionClient
from notion.block import HeaderBlock, VideoBlock, ImageBlock, CollectionViewBlock


TOKEN = ""
PAGE_URL = ""


if __name__ == '__main__':
    client = NotionClient(token_v2=TOKEN)
    page = client.get_block(PAGE_URL)
    print(page.children)

    # archive 데이터베이스 가져오기.
    archiveCollection = page.children.filter(CollectionViewBlock)[-1]
    print(archiveCollection)

    newVideoRow = archiveCollection.collection.add_row()
    newVideoRow.title = "Notion-py Test"
    newVideoRow.Tags = "축구"

    headerBlock = newVideoRow.children.add_new(HeaderBlock)
    headerBlock.title = "영상"

    videoBlock = newVideoRow.children.add_new(VideoBlock)
    videoBlock.set_source_url("https://www.youtube.com/watch?v=RoeSRZUs6h0")
    # video.upload_file() -> 동영상 파일 embed
    # video.set_source_url() -> 유튜브와 같은 url 연결

    headerBlock = newVideoRow.children.add_new(HeaderBlock)
    headerBlock.title = "사진"

    imageBlock = newVideoRow.children.add_new(ImageBlock)
    imageBlock.set_source_url("https://lh3.googleusercontent.com/proxy/6XdGBmcTlfKc1jYjn7MsqtrCEc45-BZxGAedQY9QYmLFrteR8fU_AmFe4zhVZR6BFVa3UPPfly1AS5u_dlwWD__LbJujFKzKsPt5wv2Z_02WjY8Y6dMk8x1MryyuWCww85VkmHPUGA")

