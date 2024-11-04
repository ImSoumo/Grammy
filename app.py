from pyrogram.client import Client

class Pyrogram:
    app = Client(
        name="Soumo",
        api_id=29400566,
        api_hash="8fd30dc496aea7c14cf675f59b74ec6f",
        session_string="BQHAnfYAlviETjEp77nFPQv1Wc6qOZYasRnPXWLXZypy6XOXHlXKwhLcLK7wEtx-LAKQeDmvQnlLB4hKsH7Jva1I9ZJje0s1-aI9irIJc09Ctl1a2mDoMc9U2ndlGfa0XJvSV7NajQx-j5buv5Auqqn0Mj_FevtqbLcbL6kRDotmHiqkcx3due2Uk8geGNTGbe_xU9pYDD9FX4qx9gbNthevEeT4DCeR14ezSaKdJ5-mG7O7vsxaPS_oGbrJa_svPAv5muxMCmm_qvpxc_srTiPkgHGQofmyL5YS5kwwPtb81F6CyT4O_SBMDvMS2sQ-Xmuhtwd_5AZNSlN5z7HAaKe5PBmCFAAAAAGAI4AQAA",
        plugins=dict(root="Packages"),
        in_memory=True
    )
app = Pyrogram.app

import os
import sys
import Config
import datetime
import traceback
from pyrogram import filters
from io import BytesIO, StringIO
from subprocess import getoutput
from traceback import format_exc
from inspect import getfullargspec
from pyrogram.types import Message
from asyncio import create_subprocess_shell, subprocess
from pyrogram.errors import MessageTooLong, EntityBoundsInvalid

def ReplyCheck(message: Message):
    reply_id = None
    if message.reply_to_message:
        reply_id = message.reply_to_message.id
    elif not message.from_user.is_self:
        reply_id = message.id
    return reply_id

async def aexec(code, app, msg, sticker, reply, data, chat, user):
    sys.tracebacklimit = 0
    exec( 
        "async def __aexec(app, msg, sticker, reply, data, chat, user): "
        + "\n p = print"
        + "".join(f"\n {a}" for a in code.split("\n")) 
    ) 
    return await locals()["__aexec"](app, msg, sticker, reply, data, chat, user) 

async def editReply(msg: Message, **kwargs): 
    func = msg.edit_text if msg.from_user.is_self else msg.reply 
    spec = getfullargspec(func.__wrapped__).args 
    await func(**{k: v for k, v in kwargs.items() if k in spec})

async def pyro_Excute_Func(app:app, msg:Message, db:Database):
    if len(msg.command) < 2: 
        return await editReply(msg, text="**ɪɴᴘᴜᴛ ɴᴏᴛ ғᴏᴜɴᴅ ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴏᴅᴇ ᴛᴏ ᴇxᴄᴜᴛᴇ !**")
    source = await msg.reply("**ᴘʀᴏᴄᴇssɪɴɢ.**")
    await source.edit("**ᴘʀᴏᴄᴇssɪɴɢ..**")
    await source.edit("**ᴘʀᴏᴄᴇssɪɴɢ...**")
    try:
        command = msg.text.split(maxsplit=1)[1] 
    except IndexError: 
        return await msg.reply("**🔐 ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴡʜɪʟᴇ ᴇxᴄᴜᴛɪɴɢ !**") 
    when = datetime.datetime.now()
    reply_by = msg
    if msg.reply_to_message:
        reply_by = msg.reply_to_message
    old_stderr = sys.stderr 
    old_stdout = sys.stdout 
    redirected_output = sys.stdout = StringIO() 
    redirected_error = sys.stderr = StringIO() 
    stdout, stderr, exc = None, None, None 
    try:
        sticker = reply_by.sticker.file_id if hasattr(reply_by, 'sticker') and reply_by.sticker else None
        user = reply_by.from_user if hasattr(reply_by, 'from_user') and reply_by.from_user else reply_by
        reply = msg.reply_to_message or None
        chat = msg.chat
        await aexec(command, app, msg, sticker, reply, db, chat, user) 
    except Exception: 
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue() 
    stderr = redirected_error.getvalue() 
    sys.stdout = old_stdout 
    sys.stderr = old_stderr 
    evaluation = "" 
    if stderr: 
        evaluation += stderr 
    elif stdout: 
        evaluation += stdout 
    else: 
        evaluation += "Sᴜᴄᴄᴇss !"
    end = datetime.datetime.now()
    pong = (end-when).microseconds / 1000
    try:
        if not exc:
            success = "<b>ɪɴᴘᴜᴛ ᴇxᴘʀᴇssɪᴏɴ:</b>\n"
            success += f"<pre language='python'>{command}</pre>\n"
            success += "<b>ᴏᴜᴛᴘᴜᴛ ʀᴇsᴜʟᴛ:</b>\n"
            success += f"<pre>{evaluation}</pre>\n"
            success += f"<b>ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:</b> <code>{pong}</code> <b>ᴍs</b>"
        else:
            success = "<b>⚠️ ᴇʀʀᴏʀ ᴇxᴇᴄᴜᴛɪɴɢ sɴɪᴘᴘᴇᴛ !</b>\n\n"
            success += "<b>ᴏᴜᴛᴘᴜᴛ ʀᴇsᴜʟᴛ:</b>\n"
            success += f"<pre>{exc}</pre>\n"
            success += f"<b>ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:</b> <code>{pong}</code> <b>ᴍs</b>"
        await source.edit(success)
    except MessageTooLong:
        with BytesIO(str.encode(success)) as Zeep:
            Zeep.name = "ExecTerm.txt"
            await msg.reply_document(
                document=Zeep,
                caption=f"**ᴇᴠᴀʟ:**\n<pre language='python'>{command}</pre>\n\n**ʀᴇsᴜʟᴛ:**\nᴀᴛᴛᴀᴄʜᴇᴅ ᴅᴏᴄᴜᴍᴇɴᴛ ɪɴ ғɪʟᴇ !",
                disable_notification=True,
                reply_to_message_id=reply_by.id
            )
        await source.delete()
    return

@app.on_message(filters.command(["py"], [".", "/", "?", "!", "$"]))
@app.on_edited_message(filters.command(["py"], [".", "/", "?", "!", "$"]))
async def exec_Pyro(app:app, msg:Message):
    await pyro_Excute_Func(app, msg, None)


@app.on_message(filters.command("sh", [".", "/", "?", "!", "$"]))
@app.on_edited_message(filters.command("sh", [".", "/", "?", "!", "$"]))
async def shCode_Func(app:app, msg:Message):
    when = datetime.datetime.now()
    if len(msg.text.split()) == 1:
        return await msg.reply("**sʜᴇʟʟ ǫᴜᴇʀʏ ɴᴏᴛ ғᴏᴜɴᴅ !**")
    source = await msg.reply("**ᴘʀᴏᴄᴇssɪɴɢ...**")
    command = msg.text.split(maxsplit=1)[1]
    reply_by = msg
    if msg.reply_to_message:
        reply_by = msg.reply_to_message
    process = await create_subprocess_shell(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    eor = stderr.decode().strip()
    if not eor:
        eor = "ɴᴏ ᴇʀʀᴏʀ ғᴏᴜɴᴅ !"
    coc = stdout.decode().strip()
    if not coc:
        coc = "ɴᴏ ᴏᴜᴛᴘᴜᴛ ғᴏᴜɴᴅ !"
    out = coc
    end = datetime.datetime.now()
    pong = (end-when).microseconds / 1000
    success = ""
    success += f"<b>sʜᴇʟʟ ǫᴜᴇʀʏ:</b>\n<pre>{command}</pre>\n"
    success += f"<b>ᴘʀᴏᴄᴇss ᴘɪᴅ:</b> <code>{process.pid}</code>\n"
    success += f"<b>ᴏᴜᴛᴘᴜᴛ sᴛᴅᴇʀʀ:</b>\n<pre>{eor}</pre>\n"
    success += f"<b>ᴏᴜᴛᴘᴜᴛ sᴛᴅᴏᴜᴛ:</b>\n<pre>{out}</pre>\n"
    success += f"<b>ᴘʀᴏᴄᴇss ᴛɪᴍᴇ:</b> <code>{pong}</code> <b>ᴍs</b>"
    try:
        await source.edit(success)
    except (MessageTooLong, EntityBoundsInvalid):
        with BytesIO(str.encode(success)) as Zeep:
            Zeep.name = "PyroShell.txt"
            await msg.reply_document(
                document=Zeep,
                caption=f"<b>sʜᴇʟʟ:</b>\n<pre>{command}</pre>",
                disable_notification=True,
                reply_to_message_id=reply_by.id,
            )
        await source.delete()
    return

app.run()
