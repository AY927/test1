from sympy import python
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit超入門')

st.write('プレグレスバーの表示')

latest_iteration =st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration:{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!'

left_colum,right_colum=st.columns(2)
button = left_colum.button('右カラムに文字を表示')
if button:
    right_colum.write('ここは右カラム')


ex1 = st.expander('問い合わせ')
ex1.write('問い合わせの回答')
ex2 = st.expander('問い合わせ')
ex2.write('問い合わせの回答')
ex3 = st.expander('問い合わせ')
ex3.write('問い合わせの回答')

st.write('Display Image')

if st.checkbox('Show image'):
    img = Image.open('sleeping.jpg')
    st.image(img, caption='sleeping_cat', use_column_width=True)

option=st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です。'

hobby =st.text_input('あなたの趣味を教えてください。')
condition= st.slider('あなたの今の調子は？',0,100,50)

'あなたの趣味：',hobby,'です。'
'今の調子：',condition

st.write('DataFrame')
df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.write(df)
st.dataframe(df,width=100,height=100)
st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ###  項
# repr('import streamlit as st \n import numpy as np\n import pandas as pd')
# """
# bf2=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(bf2)