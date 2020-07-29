In [22]: df = pd.read_csv("a.csv", sep="|", dtype=str)

In [23]: df
Out[23]:
     Name  Acc#       ID Age
0  Suresh  2345     a-b2  24
1  Mahesh   234     a-vf  34
2  Mahesh  4554     a-bg  45
3   Keren   344     s-bg  45
4  yankie   999     z-bg  34
5  yankie  3453  g-bgbbg  45

In [25]: df.groupby('Name',as_index=False).aggregate(lambda tdf: tdf.unique().tolist() if tdf.shape[0] > 1 else tdf)
Out[25]:
     Name         Acc#               ID       Age
0   Keren          344             s-bg        45
1  Mahesh  [234, 4554]     [a-vf, a-bg]  [34, 45]
2  Suresh         2345             a-b2        24
3  yankie  [999, 3453]  [z-bg, g-bgbbg]  [34, 45]
