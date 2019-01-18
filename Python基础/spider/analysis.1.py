import re
import string
r = ['\n                              Cajin_西法        ', '9.3万', '\n          <i class="video-station-num">182人</i>\n                    ']
st =''.join(r) 
print(st)
res = r'\n([\s\S]*?)\n'
result = re.findall(res,st)
print(result)
# # <div class = "video-info">包含主播姓名和观看人数</div>
#     <span class = "video-nickname">主播姓名</span>
#     <span class = "video-number">观看人数</span>