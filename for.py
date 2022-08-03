from bs4 import BeautifulSoup
import requests
# creating the request
res=requests.get("https://www.flipkart.com/mobiles/~cs-5ikxi0dku2/pr?sid=tyy%2C4io&collection-tab-name=realme+narzo+series&sort=price_desc&param=234&pageUID=1626267808088&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_4_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_YELWEWN3DMAC_wp2&fm=neo%2Fmerchandising&iid=M_af0591bc-ff6c-4a3e-846b-50a9a2486f6b_3.YELWEWN3DMAC&ppt=hp&ppn=homepage&ssid=rle3b62j0g0000001659401733856")
soup=BeautifulSoup(res.content,'html.parser')
content=soup.find_all("div",class_="_1AtVbE col-12-12")
print(content)