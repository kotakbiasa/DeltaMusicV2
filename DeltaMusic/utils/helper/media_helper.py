import asyncio
import os

from telegraph.aio import Telegraph

from DeltaMusic import BOT_USERNAME

async def post_to_telegraph(is_media: bool, title=None, content=None, media=None):
    telegraph = Telegraph()
    if telegraph.get_access_token() is None:
        await telegraph.create_account(short_name=BOT_USERNAME)
    if is_media:
        # Create a Telegram Post Foto/Video
        response = await telegraph.upload_file(media)
        return f"https://img.yasirweb.eu.org{response[0]['src']}"
    # Create a Telegram Post using HTML Content
    response = await telegraph.create_page(
        title,
        html_content=content,
        author_url=f"https://t.me/{BOT_USERNAME}",
        author_name=BOT_USERNAME,
    )
    return f"https://te.legra.ph/{response['path']}"