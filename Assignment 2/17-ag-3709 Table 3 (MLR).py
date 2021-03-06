# This data helps to calculate the quality of a software in terms of its execution time and reliability score. Here, 
# X1 = Execution Time (in seconds)
# X2 = Reliability Points (out of 10)
# Y = Quality Score of Software (out of 10)

X1 = [3,5,7,9,10,11]
X2 = [9,8,8,7,5,4]
Y = [8,7,6,6,5,4]
n = 6

x1_bar = sum(X1)/len(X1)
x2_bar = sum(X2)/len(X2)
y_bar = sum(Y)/len(Y)

#-------------------- x1_sq ------------------------
x1_sq = []
for i in range(0,6):
        x1_sq.append(X1[i] ** 2)
        sum_x1_sq = sum(x1_sq)

#------------------- x2_sq -------------------------
x2_sq = []
for i in range(0,6):
        x2_sq.append(X2[i] ** 2)
        sum_x2_sq = sum(x2_sq)

#------------------- x1x2 -------------------------
x1x2 = []
for i in range(0,6):
        x1x2.append(X1[i] * X2[i])
        sum_x1x2 = sum(x1x2)

#------------------ x1y ---------------------------
x1y = []
for i in range(0,6):
        x1y.append(X1[i] * Y[i])
        sum_x1y = sum(x1y)

#------------------ x2y ---------------------------
x2y = []
for i in range(0,6):
        x2y.append(X2[i] * Y[i])
        sum_x2y = sum(x2y)

#------------------ sx2_sq -------------------------
sx2_sq = sum_x2_sq - (n * x2_bar * x2_bar)


#------------------ sx1_sq -------------------------
sx1_sq = sum_x1_sq - (n * x1_bar * x1_bar)


#------------------ sx1x2 ---------------------------
sx1x2 = sum_x1x2 - (n * x1_bar * x2_bar)


#------------------ sx1y ----------------------------
sx1y = sum_x1y - (n * x1_bar * y_bar)


#------------------ sx2y ---------------------------
sx2y = sum_x2y - (n * x2_bar * y_bar)


D = (sx1_sq * sx2_sq) - (sx1x2 ** 2)
#------------------ b1 -----------------------------
b1 = ((sx2_sq * sx1y) - (sx1x2 * sx2y)) / D


#------------------ b2 -----------------------------
b2 = ((sx1_sq * sx2y) - (sx1x2 * sx1y)) / D


#------------------ b0 -----------------------------
b0 = y_bar - (b1 * x1_bar) - (b2 * x2_bar)


#------------------ y_hat --------------------------
y_hat = []
for i in range(0,6):
        y_hat.append(b0 + (b1 * X1[i]) + (b2 * X2[i]))

#------------------ TSS ----------------------------
T = []
for i in range(0,6):
        T.append((Y[i]-y_bar) ** 2)
        TSS = sum(T)

#------------------ MSS ----------------------------
M = []
for i in range(0,6):
        M.append((y_hat[i]-y_bar) ** 2)
        MSS = sum(M)

#------------------ RSS ----------------------------
R = []
for i in range(0,6):
        R.append((Y[i]-y_hat[i]) ** 2)
        RSS = sum(R)

#------------------ MSE ----------------------------
k = 3
MSE = RSS / (n-k)

#------------------ vb1 ----------------------------
vb1 = MSE * (sx2_sq / D)


#------------------ vb2 ----------------------------
vb2 = MSE * (sx1_sq / D)


#------------------ vb0 ----------------------------
vb0 = MSE * ((1/n) + (((x1_bar * x1_bar * sx2_sq) + (x2_bar * x2_bar * sx1_sq) - (2 * x1_bar * x2_bar * sx1x2)) / D))


        



