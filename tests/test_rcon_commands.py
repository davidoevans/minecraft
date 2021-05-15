import pytest
# from mcipc.rcon.je import Biome, Client
from rcon import Client


def test_rcon():
    with Client('127.0.0.1', 25575, passwd='minecraft') as client:
        response = client.run('say', 'hello there')
        print(response)


