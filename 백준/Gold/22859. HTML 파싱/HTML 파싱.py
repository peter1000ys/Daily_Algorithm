import sys
import re

input = sys.stdin.readline

html_doc = input().rstrip()

# maim 파싱
html_doc = html_doc[len("<main>"):-len("</main>")]

# div 파싱
html_doc = re.sub(r'<div +title="([\w ]*)">',r'title : \1\n', html_doc)
html_doc = re.sub(r'</div>','',html_doc)

# p 파싱
html_doc = re.sub(r'<p>(.*?)</p>',r'\1\n', html_doc)
# p 내부 다른 태그 파싱
html_doc = re.sub(r'</?[\w ]*>','',html_doc)

# p 내부 앞 뒤 공백 제거
html_doc = re.sub(r' ?\n ?','\n',html_doc)
# 2번 이상 공백 제거
html_doc = re.sub(r' {2,}',' ',html_doc)

print(html_doc)