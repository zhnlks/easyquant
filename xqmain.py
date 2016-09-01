# -*- coding: utf-8 -*-

# 指定交易商
import easyquotation

import easyquant
from easyquant import PushBaseEngine
from easyquant.log_handler.default_handler import DefaultLogHandler

# broker = 'xq'
# 选择配置文件
need_data = 'xq.json'


# 指定行情引擎
class LFEngine(PushBaseEngine):
    EventType = 'lf'

    def init(self):
        self.source = easyquotation.use('lf')

    def fetch_quotation(self):
        return self.source.stocks(['162411', '000002'])


# 默认推送行情的引擎是levelfun
quotaion_engine = LFEngine
# 行情推送间隔,默认20s
quotaion_engine.PushInterval = 10
# log记录方式
log_type = 'stdout'
log_handler = DefaultLogHandler(name='测试', log_type=log_type, filepath='')

m = easyquant.MainEngine(None, need_data=need_data, quotation_engines=[quotaion_engine], log_handler=log_handler)
m.load_strategy(names=['xqstrategy'])
m.start()
