from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause",
            description="Jeda streaming yang sedang diputar di video chat.",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume",
            description="Lanjutkan streaming yang dijeda di video chat.",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Skip",
            description="Lewati streaming yang sedang diputar di video chat dan pindah ke streaming berikutnya.",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End",
            description="Akhiri streaming yang sedang diputar di video chat.",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Shuffle",
            description="Acak lagu yang ada di daftar putar.",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Loop",
            description="Ulangi trek yang sedang diputar di video chat.",
            thumb_url="https://te.legra.ph/file/df8fa2868f8a277718a47.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
