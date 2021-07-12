from Util.path_libs import PATHS
from selenium import webdriver
import pprint, time

path = PATHS['chrome_driver']
breakpoint()
driver = webdriver.Chrome(path)

breakpoint()
driver.get("https://www.URLGOESHERE.com")
time.sleep(3)
scripts = driver.execute_script("""return window.performance.getEntriesByType("resource").filter(e => e.initiatorType === 'script').map(e => e.name.match(/.+\/([^?]+)/)[1]);""")
driver.close()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(scripts)