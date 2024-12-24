# 题目地址:https://kamacoder.com/problempage.php?pid=1070

# 前缀和
import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    n = int(data[index])
    index += 1
    vec = []
    for i in range(n):
        vec.append(int(data[index + i]))
    index += n
    
    p = [0] * n
    presum = 0
    for i in range(n):
        presum += vec[i]
        p[i] = presum
    
    results = []
    while index < len(data):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        
        if a == 0:
            sum_value = p[b]
        else:
            sum_value = p[b] - p[a-1]
        
        results.append(sum_value)
        
    for result in results:
        print(result)
        
if __name__ == "__main__":
    main()
