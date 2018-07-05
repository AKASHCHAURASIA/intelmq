# -*- coding: utf-8 -*-

from intelmq.lib import utils
from intelmq.lib.bot import Bot


class ManituParserBot(Bot):

    def process(self):
        report = self.receive_message()
        raw_report = utils.base64_decode(report["raw"])

        feed_list = raw_report.split('\n')
        for feed in feed_list[:-1]:
            data = feed.split(' ')
            if data[1].startswith('...'):
                continue

            event = self.new_event(report)

            event.add('source.ip', data[1])
            event.add('time.source', data[0] + 'UTC')
            event.add('classification.type', 'spam')
            event.add('raw', feed)
            self.send_message(event)

        self.acknowledge_message()


BOT = ManituParserBot
