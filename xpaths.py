#!/usr/bin/env python
#_*_coding:utf-8_*_

# login xpaths
login_username = '//*[@id="username"]'
login_password = '//*[@id="pwd"]'
login_btn = '//*[@id="loginform"]/button'

# datacenter, index after login
datacenter_catalog = '/html/body/div[1]/div/div[1]/div[3]/ul/li[1]/a'
datacenter_etl = '/html/body/div[1]/div/div[1]/div[3]/ul/li[2]/a'
datacenter_dataprocess = '/html/body/div[1]/div/div[1]/div[3]/ul/li[3]/a'
datacenter_share = '/html/body/div[1]/div/div[1]/div[3]/ul/li[4]/a/div[2]'
datacenter_share_mainurl = '/html/body/div[1]/div/div[1]/div[3]/ul/li[4]/div/div/a[2]'
datacenter_share_apimanage = '/html/body/div[1]/div/div[1]/div[3]/ul/li[4]/div/div/a[3]'
datacenter_system = '/html/body/div[1]/div/div[1]/div[3]/ul/li[5]/a'

# datacenter_share_mainurl siderbar
datacenter_share_share_apply = '/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a'
datacenter_share_share_audit = '//*[@id="audit"]'
datacenter_share_share_data = '/html/body/div[1]/aside/section/ul/li[2]/ul/li[3]/a'
datacenter_share_share_log = '/html/body/div[1]/aside/section/ul/li[2]/ul/li[4]/a'
datacenter_share_share_statistic = '/html/body/div[1]/aside/section/ul/li[2]/ul/li[5]/a'
datacenter_share_interfaces = '/html/body/div[1]/aside/section/ul/li[3]/ul/li/a'
datacenter_share_urp_usergroup = '/html/body/div[1]/aside/section/ul/li[4]/ul/li[1]/a'
datacenter_share_urp_organization = '/html/body/div[1]/aside/section/ul/li[4]/ul/li[2]/a'
datacenter_share_urp_user = '/html/body/div[1]/aside/section/ul/li[4]/ul/li[3]/a'
datacenter_share_urp_role = '/html/body/div[1]/aside/section/ul/li[4]/ul/li[4]/a'
datacenter_share_urp_resource = '/html/body/div[1]/aside/section/ul/li[4]/ul/li[5]/a'
datacenter_share_urp_sysmanage = '/html/body/div[1]/aside/section/ul/li[4]/ul/li[6]/a'

#datacenter_share_mainurl main content
datacenter_share_page_tab = '//*[@id="page-tab"]'
datacenter_share_ul = '//*[@id="menu-list"]'
