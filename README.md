# Django-First-Project

Django first attempt

## Useage

> [全國商工行政服務入口網](https://gcis.nat.gov.tw/mainNew/index.jsp) \
> [政府資料開放平臺 | 政府資料開放平臺](https://data.gov.tw)

take out list of [全國營業(稅籍)登記資料集 | 政府資料開放平臺](https://data.gov.tw/dataset/9400)

- 營業地址
- 統一編號
- 總機構統一編號
- 營業人名稱
- 資本額
- 設立日期
- 組織別名稱
- 使用統一發票
- 行業代號
- 名稱

and show on google map with api

## Url Directory

BASE_DIR \
| - admin/ \
| - home/ \
|&nbsp;&nbsp;| - './'&nbsp;: homepage-list \
| - company/ \
|&nbsp;&nbsp;| - './'&nbsp;: company-search-list \
|&nbsp;&nbsp;| - 'map/'&nbsp;: company-search-map \
|&nbsp;&nbsp;| - 'uploadpath/'&nbsp;: company-upload \
| - firesafety/ \
&nbsp;&nbsp;&nbsp;| - './'&nbsp;: firesafety-search-list \
&nbsp;&nbsp;&nbsp;| - '<<int:id>>/'&nbsp;: firesafety-detail
      
> any other url redirect to '/home/'
