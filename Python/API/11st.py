from Python.config import APIKEY
import requests
import json
import xmltodict

# 키워드에 해당하는 상품 검색 API

APIKEY = APIKEY['11st']

keyword = "rtx3080"
sort_type = "CP"

test_url = \
  f"""http://openapi.11st.co.kr/openapi/OpenApiService.tmall?key={APIKEY}&apiCode=ProductSearch&keyword={keyword}&sortCd={sort_type}"""
response = requests.request("GET", test_url)
jsonString = json.dumps(xmltodict.parse(response.text), indent=4)
dict_data = json.loads(jsonString)

breakpoint()