import pandas as pd

template=\
'''## 教室
<iframe src="http://cloud.liveqing.com:10080/LivePlayer.html?videoUrl={}&poster=https%3A%2F%2Fz3.ax1x.com%2F2021%2F03%2F20%2F64mQOS.jpg&autoplay=no" width="640" height="360" allowfullscreen></iframe>

## PPT
<iframe src="http://cloud.liveqing.com:10080/LivePlayer.html?videoUrl={}&poster=https%3A%2F%2Fz3.ax1x.com%2F2021%2F03%2F20%2F64mQOS.jpg&autoplay=no" width="640" height="360" allowfullscreen></iframe>'''

data = pd.read_csv('../sourse_code_modified.csv').values.tolist()
for i in data:
    course_id = i[1]
    ppt_stream = i[-3]
    room_stream = i[-2]
    content = template.format(room_stream, ppt_stream)
    print(i)
    with open(f'{course_id}.md','w',encoding='utf-8-sig') as F:
        F.write(content)
