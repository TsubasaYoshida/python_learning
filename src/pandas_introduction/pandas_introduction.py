import pandas as pd
import numpy as np

s1 = pd.Series([1,2,3,5])
print(s1)

df = pd.DataFrame({
    '名前' :['田中', '山田', '高橋'],
    '役割' : ['営業部長', '広報部', '技術責任者'],
    '身長' : [178, 173, 169]
    })
print(df)
print(df.dtypes)
print(df.columns)

data = {
    '名前' :['田中', '山田', '高橋'],
    '役割' : ['営業部長', '広報部', '技術責任者'],
    '身長' : [178, 173, 169]
    }
df = pd.DataFrame(data, columns=["名前", "身長", "役割"])
print(df)
df.columns = ["Name", "height", "Position"]
print(df)

df = pd.DataFrame(np.random.randn(20,2))
print(df)
print(df.head())
print(df.tail())
print(df.head().append(df.tail()))
print(df.head(3).append(df.tail(3)))

print('-------------------------')

df = pd.DataFrame([[10, 20], [25, 50]], index=["1行", "2行"], columns=["1列", "2列"])
print(df)
print('-----')
print(df.loc["1行", :])
print('-----')
print(df.loc[: , ["1列", "2列"]])
print('-----')
print(df.iloc[1:2])
print('-----')
print(df.iloc[:, -1])

print('-------------------------')

df = pd.DataFrame([[10, 20,30, 30], [25, 50,65, 80]], index=["1行", "2行"], columns=["A", "B", "C", "D"])
print(df)
print('-----')
print(df.query('A >= 5 and C <= 50'))

print('-------------------------')

# ダウンロード？してそうなのでコメントアウトしておく（本ファイルを何度も実行するため）
# data = pd.read_csv("https://aiacademy.jp/dataset/sample_data.csv",
#                    encoding="cp932",
#                    skiprows=1, # 1行読み飛ばす
#                    )

# print(data)
# print(type(data))
# print(data.dtypes)

print('-------------------------')

df = pd.DataFrame(np.random.randn(20,2))
print(df.sort_index(ascending=False))
# print(df.sort_values(by=1))
# print(df.sort_values(by=1, ascending=False))