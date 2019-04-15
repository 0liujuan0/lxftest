#!/usr/bin/env python
#_*_coding:utf-8_*_

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from login_test import login_test

def main():
    driver = login_test()
    driver.close()

if __name__ == "__main__":
    main()
