import pytest
from mcipc.rcon.je import Biome, Client
import os
import logging

logger = logging.getLogger(os.path.basename(__file__))


def test_give_stuff():
    # user = 'python_bricks'  #
    user = 'duderdaddude'
    with Client('127.0.0.1', 25575, passwd='minecraft') as client:
        # logger.info(client.run('tp', 'python_bricks', 'duderdaddude'))
        # logger.info(client.run('give', user, 'minecraft:light_blue_bed', '2'))
        # logger.info(client.run('give', user, 'minecraft:diamond_pickaxe', '1'))
        # logger.info(client.run('give', user, 'minecraft:flint_and_steel', '1'))
        # logger.info(client.run('give', user, 'minecraft:obsidian', '6'))
        # logger.info(client.run('give', user, 'minecraft:diamond', '64'))
        # logger.info(client.run('give', user, 'minecraft:elytra', '2'))
        # logger.info(client.run('give', user, 'minecraft:netherite_ingot', '64'))
        # logger.info(client.run('give', user, 'minecraft:netherite_chestplate', '1'))
        # logger.info(client.run('give', user, 'minecraft:netherite_boots', '1'))
        # logger.info(client.run('give', user, 'minecraft:netherite_helmet', '5'))
        # logger.info(client.run('give', user, 'minecraft:netherite_block', '64'))
        # logger.info(client.run('give', user, 'minecraft:netherite_leggings', '1'))
        # logger.info(client.run('give', user, 'minecraft:iron_ingot', '64'))
        # logger.info(client.run('give', user, 'minecraft:vine', '64'))
        # logger.info(client.run('give', user, 'minecraft:jungle_planks', '64'))
        # logger.info(client.run('give', user, 'minecraft:jungle_planks', '64'))
        #
        # logger.info(client.run('give', user, 'minecraft:stick', '10'))
        # logger.info(client.run('give', user, 'minecraft:torch', '64'))
        # logger.info(client.run('give', user, 'minecraft:soul_lantern', '64'))
        # logger.info(client.run('give', user, 'minecraft:lantern', '64'))
        # logger.info(client.run('give', user, 'minecraft:firework_rocket', '5'))
        # logger.info(client.run('give', user, 'minecraft:iron_pickaxe', '2'))
        # logger.info(client.run('ability', user, 'mayfly', 'true'))
        # diamond_chestplate
        logger.info(client.run('op', user))



@pytest.mark.skip()
def test_rcon():
    with Client('127.0.0.1', 25575, passwd='minecraft') as client:
        logger.info(client.seed)  # Get the server's seed.
        # logger.info(client.locate('duderdaddude'))

        logger.info(client.locatebiome(Biome.BADLANDS))  # Get the next location of a badlands biome.
        logger.info(dict(client.list()))
        logger.info(dict(client.locate('village')))
        # logger.info(dict(client.locate('desert')))
        logger.info(dict(client.locate('igloo')))
        # logger.info(dict(client.locate('jungle')))
        # logger.info(dict(client.locate('swamp')))
        logger.info(dict(client.locate('monument')))
        # logger.info(dict(client.locate('ocean')))
        # logger.info(dict(client.locate('shipwreck')))
        # logger.info(dict(client.locate('end city')))
        # logger.info(dict(client.locate('slime')))
        # logger.info(dict(client.locate('bastion')))
        # logger.info(dict(client.locate('fortress')))
        logger.info(dict(client.locate('mansion')))
        # logger.info(dict(client.locate('wither storm')))
        # logger.info(dict(client.locate('fossil')))
        # logger.info(dict(client.locate('portal')))
        # logger.info(client.run('me'))
        logger.info(client.run('give', 'python_bricks', 'minecraft:command_block'))
        logger.info(client.run('give', 'duderdaddude', 'minecraft:command_block'))

        logger.info(client.run('tag', '@r', 'add', 'cookie'))
        logger.info(client.run('give', '@a[tag=cookie]', 'minecraft:cookie', '5'))
        logger.info(client.run('say', '@a[tag=cookie]', 'has been given 5 cookies!'))
        # logger.info(client.run('tag', '@a[tag=cookie]' 'remove cookie'))

        logger.info(client.run('teleport', '@p[name=duderdaddude]', 'mansion'))
        logger.info(client.run('give', 'duderdaddude', 'minecraft:stone'))
        logger.info(client.run('tp', 'python_bricks', 'duderdaddude'))
        # response = client.run('help', 'teleport')
        # print(response)
        # response = client.run('title')
        # print(response)
        players = client.list()
        for player in players:
            print(player)


def give_resource(resource_name=None, player_name=None, quantity=1):
    with Client('127.0.0.1', 25575, passwd='minecraft') as client:
        logger.info(client.run('tag', '@r', 'add', resource_name))
        logger.info(client.run('give', f'@a[tag={resource_name}]', f'minecraft:{resource_name}', quantity))
        logger.info(client.run('say', f'@a[tag={resource_name}]', f'has been given 5 {resource_name}!'))


@pytest.mark.skip('not now')
def test_give_resource():
    give_resource('sword', 'duderdaddude', 1)


def summon(resource_name=None):
    with Client('127.0.0.1', 25575, passwd='minecraft') as client:
        # logger.info(client.run('summon', 'lightning_bolt', '~-10 ~ ~'))
        # logger.info(client.run('summon', 'wolf ~ ~ ~ minecraft:on_tame'))

        commands = """
            {Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~5 ~-3 ~5 ~15 ~4 ~15 planks 0 hollow"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~6 ~0 ~10 wall_sign 5 replace 
            {Text1:\"{\\\"text\\\":\\\"Created by\\\"}\",Text2:\"{\\\"text\\\":\\\"DigMinecraft.com\\\"}\"}"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~9 ~-1 ~14 torch 4"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~11 ~-2 ~14 torch 4"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~9 ~-3 ~6 torch 3"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~11 ~-4 ~6 torch 3"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~14 ~-5 ~11 torch 2"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~14 ~-6 ~9 torch 2"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~6 ~-7 ~11 torch 1"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~6 ~-8 ~9 torch 1"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~4 ~-9 ~11 torch 2"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~4 ~-10 ~9 torch 2"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~4 ~-11 ~10 wall_sign 4 replace 
            {Text1:\"{\\\"text\\\":\\\"Created by\\\"}\",Text2:\"{\\\"text\\\":\\\"DigMinecraft.com\\\"}\"}"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~14 ~-14 ~14 ~14 ~-14 ~13 chest"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~5 ~-10 ~5 ~15 ~-10 ~15 stone_slab 3"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~14 ~-16 ~6 crafting_table"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~10 ~-17 ~7 bed 2"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~10 ~-18 ~6 bed 10"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~6 ~-20 ~6 ~14 ~-20 ~14 cobblestone"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~5 ~-18 ~7 ~5 ~-18 ~8 glass_pane"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~5 ~-19 ~12 ~5 ~-19 ~13 glass_pane"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~15 ~-20 ~7 ~15 ~-20 ~8 glass_pane"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~15 ~-21 ~12 ~15 ~-21 ~13 glass_pane"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~7 ~-22 ~5 ~8 ~-22 ~5 glass_pane"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~12 ~-23 ~5 ~13 ~-23 ~5 glass_pane"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~7 ~-24 ~15 ~8 ~-24 ~15 glass_pane"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~12 ~-25 ~15 ~13 ~-25 ~15 glass_pane"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~5 ~-28 ~10 dark_oak_door 0"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/setblock ~5 ~-28 ~10 dark_oak_door 8"},Passengers:
            [{id:falling_block,Block:command_block,Time:1,TileEntityData:
            {Command:"/fill ~ ~-30 ~-1 ~ ~40 ~-1 redstone_block"},Passengers:
            [{id:falling_block,Block:redstone_block,Time:1}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}
            """
        # logger.info(client.run('tp', 'duderdaddude', '~ ~ ~'))
        # logger.info(client.locate('python_bricks'))
        logger.info(client.list())
        logger.info(client.run('weather', 'clear'))
        logger.info(client.run('data', 'get', 'entity', 'duderdaddude'))
        logger.info(client.run('data', 'get', 'entity', 'python_bricks'))
        logger.info(client.run('cb', 'help'))
        # logger.info(client.run('tp', 'python_bricks', 'duderdaddude'))
        # logger.info(client.run('tp', 'duderdaddude', 'python_bricks'))
        # logger.info(client.run('duderdaddude', 'world', 'postition'))
        logger.info(client.run('summon', 'falling_block', '~ ~1 ~', '{Block:redstone_block,Time:1}'))
        # logger.info(client.run('summon', 'falling_block', commands))
        # logger.info(client.run('fill', '~5 ~-3 ~5 ~15 ~4 ~15 jungle_wood'))
        logger.info(client.run('fill', '305 75 -48 ~15 ~4 ~15 stone replace'))
        # logger.info(client.run('data', 'get', 'block', '3320 90 -48'))
        logger.info(client.run('tp', 'duderdaddude', '200 201 0'))
        # logger.info(client.run('summon', 'falling_block', '200 200 0', '{Block:command_block,Time:1,TileEntityData:{Command:"/fill ~ ~-1 ~-1 ~ ~50 ~-1 redstone_block"},Passengers:[{id:falling_block,Block:redstone_block,Time:1}]}'))
        logger.info(client.run('setblock', '201 200 0 diamond 5 replace'))


@pytest.mark.skip('not now')
def test_summon():
    summon()


