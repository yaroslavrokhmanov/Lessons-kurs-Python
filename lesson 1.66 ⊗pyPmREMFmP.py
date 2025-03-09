import re  

# 1. Дана строка:

txt = '2025-12-31'
# Разбейте ее на три кармана.

res = re.fullmatch('(\d{4})-(\d{2})-(\d{2})', txt)
print(res[1]) # 2025 
print(res[2]) # 12
print(res[3]) # 31
