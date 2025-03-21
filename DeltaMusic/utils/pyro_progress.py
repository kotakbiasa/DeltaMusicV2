#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

import asyncio
import math
import time

from pyrogram.errors import FloodWait, MessageIdInvalid, MessageNotModified


async def progress_for_pyrogram(current, total, ud_type, message, start, dc_id):
    """generic progress display for Telegram Upload / Download status"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        elapsed_time = round(diff)
        if elapsed_time == 0:
            return
        speed = current / diff
        time_to_completion = round((total - current) / speed)
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = time_formatter(elapsed_time)
        estimated_total_time = time_formatter(estimated_total_time)

        progress = "[{0}{1}] \nP: {2}%\n".format(
            "".join(["●" for _ in range(math.floor(percentage / 5))]),
            "".join(["○" for _ in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )

        tmp = (
            progress
            + "{0} <b>of</b> {1}\n<b>Speed:</b> {2}/s\n<b>DC ID:</b> {3}\n<b>ETA:</b> {4}</b>\n".format(
                humanbytes(current),
                humanbytes(total),
                humanbytes(speed),
                dc_id,
                estimated_total_time if estimated_total_time != "" else "0 s",
            )
        )
        try:
            await message.edit(f"{ud_type}\n {tmp}")
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await message.edit(f"{ud_type}\n {tmp}")
        except (MessageNotModified, MessageIdInvalid):
            pass


def humanbytes(size: int) -> str:
    """converts bytes into human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    number = 0
    dict_power_n = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        number += 1
    return f"{str(round(size, 2))} {dict_power_n[number]}B"


def time_formatter(seconds: int) -> str:
    result = ""
    v_m = 0
    remainder = seconds
    r_ange_s = {"days": (24 * 60 * 60), "hours": (60 * 60), "minutes": 60, "seconds": 1}
    for age, divisor in r_ange_s.items():
        v_m, remainder = divmod(remainder, divisor)
        v_m = int(v_m)
        if v_m != 0:
            result += f" {v_m} {age} "
    return result