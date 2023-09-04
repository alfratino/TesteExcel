import pandas as pd

ensinc = pd.read_excel("MatEnsinc.xlsx")
control = pd.read_excel("Pedicontrol.xlsx")
uni = pd.merge(control, ensinc, left_on="mat_icontrol", right_on="mat_ensinc", how="left")

uni.to_excel("uniao.xlsx")
print(uni)