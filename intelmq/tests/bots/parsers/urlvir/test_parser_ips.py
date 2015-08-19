# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import unittest

import intelmq.lib.test as test
from intelmq.bots.parsers.urlvir.parser_ips import URLVirIPsParserBot


EXAMPLE_REPORT = {"feed.name": "URLVir",
                  "feed.url": "http://www.urlvir.com/export-ip-addresses/",
                  "raw": "IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj"
                         "IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiNVUkxWaXIgQWN0"
                         "aXZlIE1hbGljaW91cyBJUCBBZGRyZXNzZXMgSG9zdGluZyBNYWx3"
                         "YXJlCiNVcGRhdGVkIG9uIEF1Z3VzdCAxNywgMjAxNSwgMTA6MTYg"
                         "YW0KI0ZyZWUgZm9yIG5vbmNvbW1lcmNpYWwgdXNlIG9ubHksIGNv"
                         "bnRhY3QgdXMgZm9yIG1vcmUgaW5mb3JtYXRpb24KIyMjIyMjIyMj"
                         "IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj"
                         "IyMjIyMjIyMjIyMjIyMjIyMjCjE5Mi4wLjIuMQoxOTIuMC4yLjIK"
                         "MTkyLjAuMi4zCjE5Mi4wLjIuNA==",
                  "__type": "Report",
                  }
EXAMPLE_EVENT = {"feed.name": "URLVir",
                 "feed.url": "http://www.urlvir.com/export-ip-addresses/",
                 "source.ip": "192.0.2.1",
                 "classification.type": "malware",
                 "__type": "Event",
                 "raw": "MTkyLjAuMi4x",
                 }


class TestURLVirIPsParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for URLVirIPsParserBot.
    """

    def prepare_bot(self):
        self.bot_id = 'test-bot'
        self.bot_reference = URLVirIPsParserBot
        self.default_input_message = json.dumps(EXAMPLE_REPORT)
        super(TestURLVirIPsParserBot, self).prepare_bot()

    def test_event(self):
        """ Test if correct Event has been produced. """
        self.prepare_bot()
        self.run_bot()
        self.assertEventAlmostEqual(0, EXAMPLE_EVENT)


if __name__ == '__main__':
    unittest.main()
