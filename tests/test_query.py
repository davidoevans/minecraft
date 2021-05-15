import pytest
from mcipc.query import Client
import socket
import logging

logger = logging.getLogger('test_mcipi')


def test_query():
    try:
        with Client('127.0.0.1', 25575) as client:
            basic_stats = client.stats()

            logger.info(basic_stats)

    except socket.timeout as timeout:
        logger.info(timeout)

