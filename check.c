def check(a):
    


if (N <= 0) {
    return true;
}
for (int i = 0; i + 1 < N; ++i) {
    if (a[i] > a[i + 1]) { // i是一个不合法的位置 我们找到后面最小的位置
        j = i + 1;
        for (int k = j; k < N; ++k) {
            if (a[k] < a[j]) {
                j = k;
            }
        }
        // j是i后面最小值的位置
        swap(a[i], a[j]);
        for (int k = i; k + 1 < N; ++k) {  //看一下交换后面是不是有序的
            if (a[k] > a[k + 1]) {
                return false;
            }
        }
        return true;
    }
}
return true;