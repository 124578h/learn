import streamlit as st

# 显示文本
st.write("## 早上好！")

# 显示 Markdown 格式的文本
st.markdown(
"""
### 早上好！
# 1. 数据类型确定

确定要收集的关键数据类型，确保数据的全面性和多样性。这些数据类型应涵盖以下几类：

- **患者基础健康信息**
	- **年龄**
	- **性别**
	- **身高**
	- **体重**
	- **BMI（体重指数）**

- **代谢数据**
	- **糖代谢情况**
		- 血糖水平（空腹血糖、餐后血糖）
		- 胰岛素抵抗指数
		- 糖化血红蛋白（HbA1c）
	- **脂肪代谢情况**
		- 血脂水平（总胆固醇、LDL、HDL、甘油三酯）
		- 游离脂肪酸
	- **蛋白质代谢情况**
		- 血清蛋白（白蛋白、球蛋白）
		- 尿素氮（BUN）
		- 肌酐

- **身体成分分析**
	- **体脂率**
	- **瘦体质量（肌肉质量）**
	- **水分含量**
	- **矿物质含量**

- **运动能耗评估**
	- **基础代谢率（BMR）**
	- **每日总能量消耗（TDEE）**
	- **活动水平（轻度、中度、高强度）**

- **TNM分期**
	- **原发肿瘤大小（T）**
	- **淋巴结受累情况（N）**
	- **远处转移情况（M）**
	- **总体临床分期**

### 2. 数据收集与预处理

收集上述数据类型的原始数据，并进行以下预处理步骤：

- **数据清洗**：处理缺失值、异常值、重复数据等问题。
- **数据标准化**：根据各变量的不同单位和量纲，进行标准化处理，确保数据的一致性。
- **数据整合**：将来自不同来源的数据整合到统一的数据库中，确保数据的连贯性和完整性。

### 3. 数据标注

- 对数据进行标注，特别是对于TNM分期、代谢数据中的异常情况等，以便模型能够更好地理解和分类。

### 4. 数据集划分

- **训练集**：用于模型的训练，占数据集的70-80%。
- **验证集**：用于调参和模型验证，占数据集的10-15%。
- **测试集**：用于最终模型的测试，占数据集的10-15%。

### 5. 数据质量评估

- **数据完整性检查**：确保每个数据样本包含所有必要的信息。
- **数据一致性检查**：确保数据的一致性，例如身高和体重的关系，BMI计算的合理性等。
- **相关性分析**：对各变量间进行相关性分析，确保模型能有效利用这些数据。

### 6. 数据安全和隐私保护

- 确保数据的匿名化处理，保护患者隐私。
- 根据相关法律法规，确保数据使用合规。

### 7. 数据增强（可选）

- 使用数据增强技术，生成额外的虚拟样本，增加数据的多样性和丰富度，特别是在数据不平衡的情况下。

通过以上步骤，能够构建一个高质量的癌症患者营养数据集，支持后续的模型训练和优化过程。""")

# 显示数字变量
a = 329 * 3
st.write(a)

# 显示列表和字典
st.write([1122, 331, 987])
st.write({"a": 1, "b": 2, "c": 3})

# 设置网页标题
st.title("我的个人网站 ")

# 显示图片
st.image("pythonProject/good.png", width=200)

# 创建并显示 DataFrame
import pandas as pd
df = pd.DataFrame({
    "学号": ["01", "02", "03", "04"],
    "班级": ["二班", "一班", "二班", "三班"],
    "成绩": [92, 67, 70, 88]
})
st.dataframe(df)

# 显示非交互式的表格
st.table(df)

# 添加分隔线
st.divider()

# 运行 Streamlit 应用
# 在终端中输入：streamlit run streamlit-demo.py



import streamlit as st

# 文本输入框
name = st.text_input("请输入你的名字：")
if name:
    st.write(f"你好，{name}")

# 密码输入框
password = st.text_input("请输入你的密码：", type="password")
if password:
    st.write("密码已输入，但为了安全，不会显示。")
import streamlit as st

# 创建一个密码输入框，设置初始值、占位符和最大字符数
password = st.text_input(
    "请输入你的密码：",
    type="password",
    value="",
    placeholder="至少6位字符",
    max_chars=20,
    key="password_input",
    label="密码",
    label_visibility=st.LabelVisibility.DEFAULT,
    help="请输入您的账户密码"
)  # 在这个示例中，我们创建了一个密码输入框，并设置了初始值为空字符串、占位符为“至少6位字符”、最大字符数为20。同时，我们还设置了 key、label 和 help 参数来提供额外的信息和自定义标签文本。label_visibility 参数设置为 st.LabelVisibility.DEFAULT，这意味着标签将正常显示。如果需要隐藏标签，可以将其设置为 st.LabelVisibility.HIDDEN

# 检查密码是否被输入
if password:
    st.write("密码已输入。")

# 多行文本输入区
paragraph = st.text_area("请输入一段自我介绍：")
if paragraph:
    st.write(f"自我介绍：{paragraph}")

# 数字输入框
age = st.number_input("请输入你的年龄：", value=20, min_value=0, max_value=150, step=1)
if age:
    st.write(f"输入的年龄是：{age}")

# 勾选框
checked = st.checkbox("我同意以上条款")
if checked:
    st.write("您已同意条款!")

# 按钮
if st.button("提交"):
    st.write("提交成功！")



import streamlit as st

# 单选按钮
gender = st.radio("你的性别是什么？", ["男性", "女性", "跨性别"], index=None)
if gender:
    st.write(f"你选择的性别是 {gender}")

# 单选下拉框
contact = st.selectbox("你希望通过什么方式联系？", ["电话", "邮件", "微信", "QQ", "其它"])
st.write(f"好的，我们会通过 {contact} 联系你")

# 多选下拉框
fruits = st.multiselect("你喜欢的水果是什么？", ["苹果", "香蕉", "橙子", "梨", "西瓜", "葡萄"])
for fruit in fruits:
    st.write(f"你选择的水果是 {fruit}")

# 滑块
height = st.slider("你的身高是多少厘米？", min_value=100, max_value=230, value=170, step=1)
st.write(f"你的身高是 {height} 厘米")

# 文件上传器
uploaded_file = st.file_uploader("上传文件", type=["py"])
if uploaded_file:
    st.write(f"你上传的文件是 {uploaded_file.name}")
    # 如果是文本文件，可以读取内容
    if uploaded_file.name.endswith(".txt") or uploaded_file.name.endswith(".py"):
        contents = uploaded_file.read()
        st.write(contents)




import streamlit as st

# 创建侧边栏
with st.sidebar:
    name = st.text_input("请输入你的名字：")
    if name:
        st.write(f"你好，{name}")

# 创建分列
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.text_input("请输入你的密码：", type="password")
with col2:
    st.text_area("请输入一段自我介绍：")
with col3:
    age = st.number_input("请输入你的年龄：")
    st.write(f"你的年龄是：{age}岁")
    st.checkbox("我同意以上条款")

# 创建选项卡
tab1, tab2, tab3 = st.tabs(["性别", "联系方式", "喜好水果"])
with tab1:
    gender = st.radio("你的性别是什么？", ["男性", "女性", "跨性别"])
    if gender:
        st.write(f"你选择的性别是 {gender}")
with tab2:
    contact = st.selectbox("你希望通过什么方式联系？", ["电话", "邮件", "微信", "QQ"])
    st.write(f"好的，我们会通过 {contact} 联系你")
with tab3:
    fruits = st.multiselect("你喜欢的水果是什么？", ["苹果", "香蕉", "橙子", "梨"])
    for fruit in fruits:
        st.write(f"你选择的水果是 {fruit}")

# 创建折叠展开组件
with st.expander("身高信息"):
    height = st.slider("你的身高是多少厘米？", min_value=100, max_value=230, value=170, step=1)
    st.write(f"你的身高是 {height} 厘米")


















