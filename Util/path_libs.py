import os

pkg_dir = os.path.dirname(os.path.abspath(__file__))

PATHS = {'pkg_dir': os.path.dirname(os.path.abspath(__file__)),
         'chrome_driver': os.path.join(pkg_dir, 'chromedriver'),
         }