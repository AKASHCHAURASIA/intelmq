# -*- coding: utf-8 -*-

import os
import unittest

import intelmq.lib.test as test
from intelmq.bots.parsers.manitu.parser import ManituParserBot
from intelmq.lib import utils


with open(os.path.join(os.path.dirname(__file__), 'test_manitu.data'), 'rb') as handle:
    REPORT_DATA = handle.read()

EXAMPLE_REPORT = {"feed.name": "Manitu Feed",
                  "feed.provider": "manitu.net",
                  "__type": "Report",
                  "raw": utils.base64_encode(REPORT_DATA),
                  "time.observation": "2018-07-03T12:19:24+00:00"
                  }

EXAMPLE_EVENT = [{"__type": "Event",
                  "feed.name": "Manitu Feed",
                  "feed.provider": "manitu.net",
                  "time.observation": "2018-07-05T07:38:47+00:00",
                  "source.ip": "187.141.75.161",
                  "time.source": "2018-07-03T10:15:00+00:00",
                  "classification.type": "spam",
                  "raw": "MjAxOC0wNy0wM1QxMjoxNSswMjAwIDE4Ny4xNDEuNzUuMTYxICAgIA=="
                  },
                 {"__type": "Event",
                  "feed.name": "Manitu Feed",
                  "feed.provider": "manitu.net",
                  "time.observation": "2018-07-05T07:38:47+00:00",
                  "source.ip": "138.36.122.252",
                  "time.source": "2018-07-03T10:15:00+00:00",
                  "classification.type": "spam",
                  "raw": "MjAxOC0wNy0wM1QxMjoxNSswMjAwIDEzOC4zNi4xMjIuMjUyICAgIA=="
                  }]


class TestManituParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for ManituParserBot.
    """

    @classmethod
    def set_bot(self):
        self.bot_reference = ManituParserBot
        self.default_input_message = EXAMPLE_REPORT

    def test_event(self):
        """ Test if correct Event has been produced. """
        self.run_bot()
        self.assertMessageEqual(0, EXAMPLE_EVENT[0])
        self.assertMessageEqual(1, EXAMPLE_EVENT[1])


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
