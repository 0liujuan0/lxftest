#!/usr/bin/env python
#_*_coding:utf-8_*_

import unittest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import conf
import xpaths

class TestDCShareMain(unittest.TestCase):
    """Test Login"""
    def setUp(self):
        self.driver = conf.get_driver(proxy=True, login=True)
    def tearDown(self):
        self.driver.close()

    def test_side_bar(self):
        menu = self.driver.find_element_by_xpath(xpaths.datacenter_share)
        share_mainurl = self.driver.find_element_by_xpath(xpaths.datacenter_share_mainurl)
        ActionChains(self.driver).move_to_element(menu).click(share_mainurl).perform()
        self.assertEqual(len(self.driver.window_handles), 2, msg=u'does not open new window when click catacenter_share')
        self.driver.switch_to.window(self.driver.window_handles[1])

        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_xpath(xpaths.datacenter_share_page_tab)

        self.driver.find_element_by_xpath(xpaths.datacenter_share_share_apply).click()
        self.assertIsNotNone(self.driver.find_element_by_xpath(xpaths.datacenter_share_page_tab), msg=u'page tab is none after click share apply')
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'资源申请', ul.text, msg=u'does not open tab when click share apply')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_share_audit).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'申请审核', ul.text, msg=u'does not open tab when click share audit')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_share_data).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'共享数据', ul.text, msg=u'does not open tab when click share data')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_share_log).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'共享日志', ul.text, msg=u'does not open tab when click share log')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_share_statistic).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'共享统计', ul.text, msg=u'does not open tab when click share statistic')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_interfaces).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'公共接口配置', ul.text, msg=u'does not open tab when click share interfaces')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_urp_usergroup).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'用户组管理', ul.text, msg=u'does not open tab when click share usergroup')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_urp_organization).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'组织架构', ul.text, msg=u'does not open tab when click share organization')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_urp_user).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'用户管理', ul.text, msg=u'does not open tab when click share user')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_urp_role).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'角色管理', ul.text, msg=u'does not open tab when click share role')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_urp_resource).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'资源管理', ul.text, msg=u'does not open tab when click share resource')

        self.driver.find_element_by_xpath(xpaths.datacenter_share_urp_sysmanage).click()
        ul = self.driver.find_element_by_xpath(xpaths.datacenter_share_ul)
        self.assertIn(u'系统设置', ul.text, msg=u'does not open tab when click share manage')
