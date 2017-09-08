# coding:utf8

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
r = requests.get(url)
print('Status code:',r.status_code)


#将API响应存储在一个变量中
response_dict = r.json()
print('Total repositories:',response_dict['total_count'])
#搜索有关仓库的信息
repo_dicts = response_dict['items']
print('Respositories returned;',len(repo_dicts))
#研究第一个仓库
#repo_dict = repo_dicts[0]
#names,stars,owners = [],[],[]
names,plot_dicts = [],[]
#stars = []
for repo_dict in repo_dicts:
       name = repo_dict['name']
       names.append(name)
#       star = repo_dict['stargazers_count']
#       stars.append(star)
#       owners.append(repo_dict['owner']['login'])
       plot_dict = {
           'Value': repo_dict['stargazers_count'],
           'label': repo_dict['owner']['login'],
           'xlink': repo_dict['html_url']
            }
       plot_dicts.append(plot_dict)
print(plot_dicts)
my_style = LS('#333366',base_style=LCS)
## 定制图表的外观
my_config = pygal.Config()
my_config.x_labels_rotation =45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size =14
my_config.major_lable_font_size = 18
# 将较长的项目名缩短为15个字符
my_config.truncate_label = 15
# 将图表中的水平线隐藏
my_config.show_y_guides = False
# 设置自定义宽度，让图表更充分地利用浏览器中的可用空间
my_config.width = 1000

pr = pygal.Bar(my_config,style=my_style)
pr.title = 'Most-Starred Python Project On Github'
pr.x_labels = names
pr.y_title = 'Star Number'
pr.add('',plot_dicts)
pr.render_to_file('python_repos.svg')
#    print('\nName',repo_dict['name'])
#    print('Owner',repo_dict['owner']['login'])
#    print('Star',repo_dict['stargazers_count'])
#    print('Repository:',repo_dict['html_url'])
#    print('Created:',repo_dict['created_at'])
#    print('Update:',repo_dict['updated_at'])
#    print('Description:',repo_dict['description'])
#print('\nkeys:',len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)
#处理结果
#print(response_dict.keys())