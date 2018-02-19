
EXCHANGE = (
    ('HOSE', 'HOSE'),
    ('HNX', 'HNX'),
    ('UPCOM', 'UPCOM')
)

# CRAWLING_SOURCE = 'http://cophieu68.vn/snapshot.php?id={symbol}'
#
# CLOSE_XPATH = "//strong[@id='stockname_close']/text()"
# REF_XPATH = "//div[@id='snapshot_trading']/div[1]/table/tr[1]/td[2]/strong/text()"
# OPEN_XPATH = "//div[@id='snapshot_trading']/div[1]/table/tr[2]/td[2]/strong/text()"
# HIGH_XPATH = "//strong[@id='stockname_price_highest']/span/text()"
# LOW_XPATH = "//strong[@id='stockname_price_lowest']/span/text()"
# VOL_XPATH = "//strong[@id='stockname_volume']/span/text()"
# FOREIGN_BOUGHT_XPATH = ""
# FOREIGN_SOLD_XPATH = ""

CRAWL_SOURCE = 'http://www.cophieu68.vn/historyprice.php?id={symbol}'

DATE_XPATH = "//div[@id='content']//table[1]/tr[2]/td[2]/text()"
REF_XPATH = "//div[@id='content']//table[1]/tr[2]/td[3]/text()"
OPEN_XPATH = "//div[@id='content']//table[1]/tr[2]/td[8]/span/text()"
CLOSE_XPATH = "//div[@id='content']//table[1]/tr[2]/td[6]//strong/text()"
HIGH_XPATH = "//div[@id='content']//table[1]/tr[2]/td[9]/span/text()"
LOW_XPATH = "//div[@id='content']//table[1]/tr[2]/td[10]/span/text()"
VOL_XPATH = "//div[@id='content']//table[1]/tr[2]/td[7]/text()"
AGREEMENT_XPATH = "//div[@id='content']//table[1]/tr[2]/td[11]/text()"
FOREIGN_BUY_XPATH = "//div[@id='content']//table[1]/tr[2]/td[12]/text()"
FOREIGN_SELL_XPATH = "//div[@id='content']//table[1]/tr[2]/td[13]/text()"

# Article status
PAGE_STATUS = (
    (1, 'DRAFT'),
    (2, 'PUBLISHED'),
)
POSTS_PER_PAGE = 6