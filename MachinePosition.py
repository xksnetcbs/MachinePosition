# -*- coding: utf-8 -*-
import json
import time
from mcdreforged.api.all import *
import re
import os
import random

PLUGIN_METADATA = {
    'id': 'MachinePos',
    'version': '1.0',
    'name': 'A Easy FakePlayer Spawner',
    'author': [
        'DC_Provide'
    ],
    'link': 'Nope...[doge]'
}
port = 0
plnam = 'dc'
worked = 0
class fplayer:
    name = 'None'
    pos = '0 0 0'
    dimensition = 'minecraft:overworld'
    nick = 'None'
@new_thread(PLUGIN_METADATA['name'])
def outread(server, info):
    f = open('./fplayer/' + info.content + 'runt.txt', 'r')
    guit = f.read()
    server.say(f.read())
    server.execute('/' + guit)
    f.close()
    time.sleep(4)
    f = open('./fplayer/' + info.content + 'runt2.txt', 'r')
    guit = f.read()
    server.say(f.read()[1:])
    server.execute('/' + guit)
    f.close()
    f = open('./fplayer/' + info.content + 'mode.txt', 'r')
    work = int(f.read())
    f.close()
    i = 0
    for i in range(work):
        server.say(i)
        f = open('./fplayer/' + info.content + 'mode' + str(i + 1) + '.txt', 'r')
        server.say('./fplayer/' + info.content + 'mode' + str(i + 1) + '.txt')
        guit = f.read()
        server.execute('/' + guit)
        f.close()
def inwrite():
    global worked
    f = open('./fplayer/' + fplayer.nick + 'mode.txt', 'w')
    f.write(str(worked))
    f.close()
    f = open('./fplayer/' + fplayer.nick + 'runt.txt', 'w')
    f.write("player " + fplayer.name + " spawn at 1000 90 1000")
    f.close()
    f = open('./fplayer/' + fplayer.nick + 'runt2.txt', 'w')
    f.write("execute at " + fplayer.name + ' in ' + fplayer.dimensition + ' run tp ' + fplayer.name + ' ' + fplayer.pos)
    f.close()
    f = open('./fplayer/' + fplayer.nick + '.nick','w')
    f.write(fplayer.nick)
    f = open('./fplayer/playerlist.dat', 'a')
    f.write(fplayer.nick + ' ')
    f.close()
def check_info(server, info):
    global port, plnam, worked
    if port == 5:
        server.say("===============================================")
        server.say("     ")
        server.say("       " + info.content + '???????????????????????????   ')
        server.say("     ")
        server.say("===============================================")
        outread(server, info)
        port = 0
    if info.player == plnam and port == 4:
        if info.content == '...':
            server.say("?????????????????????????????????????????????????????????????????????")
            port = 0
            inwrite()
        else:
            server.say("????????????????????????" + info.content)
            worked += 1
            f = open('./fplayer/' + fplayer.nick + 'mode' + str(worked) + '.txt', 'w')
            f.write('player ' + fplayer.name + ' ' + info.content)
            server.say("????????????" + '/player ' + fplayer.name + ' ' + info.content)
            server.say("??????????????????????????????????????????'...'??????")
    if info.player == plnam and port == 1:
        fplayer.name = info.content[info.content.find('[') + 1:info.content.find(']')]
        fplayer.pos = info.content[info.content.find('{') + 1:info.content.find('}')]
        fplayer.dimensition = info.content[info.content.find('(') + 1:info.content.find(')')]
        fplayer.nick = info.content[info.content.find('<') + 1:info.content.find('>')]
        if fplayer.dimensition == '0':
            fplayer.dimensition = 'minecraft:overworld'
        if fplayer.dimensition == '1':
            fplayer.dimensition = 'minecraft:the_nether'
        if fplayer.dimensition == '2':
            fplayer.dimensition = 'minecraft:the_end'
        server.say("?????????" + fplayer.name + "???????????????" + fplayer.pos + "???" + fplayer.dimensition + "?????????")
        port = 4
        server.say("?????????????????????????????????use continuous???????????????'...'????????????")
def on_user_info(server, info):
    global port, plnam
    check_info(server, info)
    if info.content == '!!machine add':
        server.say(str(info.player) + "???????????????????????????")
        server.say("?????????add[bot_name]{bot_position}(bot_dimensition)<bot_nickname>")
        plnam = info.player
        port = 1
    if info.content == '!!machine':
        server.say("????????????????????????????????????!!mlist??????????????????")
        port = 5
    if info.content == '!!mlist':
        server.say("??????????????????????????????????????????")
        f = open("./fplayer/playerlist.dat", 'r')
        fuit = f.read()
        server.say(fuit)
