from pyrogram import Client

class Pyrogram:
    app2 = PyGram(
    name="pyUB2",
    api_id=29400566,
    api_hash="8fd30dc496aea7c14cf675f59b74ec6f",
    in_memory=True,
    session_string="BQHAnfYAlviETjEp77nFPQv1Wc6qOZYasRnPXWLXZypy6XOXHlXKwhLcLK7wEtx-LAKQeDmvQnlLB4hKsH7Jva1I9ZJje0s1-aI9irIJc09Ctl1a2mDoMc9U2ndlGfa0XJvSV7NajQx-j5buv5Auqqn0Mj_FevtqbLcbL6kRDotmHiqkcx3due2Uk8geGNTGbe_xU9pYDD9FX4qx9gbNthevEeT4DCeR14ezSaKdJ5-mG7O7vsxaPS_oGbrJa_svPAv5muxMCmm_qvpxc_srTiPkgHGQofmyL5YS5kwwPtb81F6CyT4O_SBMDvMS2sQ-Xmuhtwd_5AZNSlN5z7HAaKe5PBmCFAAAAAGAI4AQAA",
    plugins=dict(root="Linux")
      in_memory=True
    )
    Soumo = Client(
        name="Soumo",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="Packages"),
        in_memory=True
    )
App = Pyrogram.Soumo
