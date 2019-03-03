#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/9.
from testdemo.logutils import *

def test_dict():
    """
        元素字典
    """
    params_from = {'keys':'ad_drawer_small_card_pos|ad_search_main_page_pos|ad_boost_result_pos|ad_left_screen_pos_one|ad_left_screen_pos_two',
                   'country':'US','model':'6045K','pkg':'com.tct.launcher','sign':'605390a6339d26fa5a17fc5cbb94b8cd'}
    print('keys:' + params_from['keys'])

    log = Logger(level='debug')
    log.logger.info('test test log')



if __name__ == '__main__':
    test_dict()