import os
import sqlite3
from hoshino import Service
from nonebot.message import CQEvent

sv = Service('祖安宝典')

BANNED_WORD = (
    'rbq', 'RBQ', '憨批', '废物', '死妈', '崽种', '傻逼', '傻逼玩意',
    '没用东西', '傻B', '傻b', 'SB', 'sb', '煞笔', 'cnm', '爬', 'kkp',
    'nmsl', 'D区', '口区', '我是你爹', 'nmbiss', '弱智', '给爷爬', '杂种爬', '爪巴', '滚', 'gun'
)
db_path = os.path.join(os.path.dirname(__file__), 'data.db')


class db:
    def __init__(self):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def get_word(self):
        with self.connect() as conn:
            r = conn.execute(
                "SELECT * FROM `main` ORDER BY RANDOM() limit 1").fetchall()
            r2 = r[0]
        return r2


_db = db()


@sv.on_fullmatch(BANNED_WORD, only_to_me=True)
async def zuan(bot, ev: CQEvent):
    word = _db.get_word()[1]
    await bot.send(ev, word)
