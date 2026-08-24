#!/bin/bash
CSV="$1"

# 文件不存在，错误输出到stderr，退出码非0
if [ ! -f "$CSV" ]; then
    echo "error: file $CSV does not exist" >&2
    exit 1
fi

# 统计5xx状态最多的前2个path，次数降序，次数相同按path字典序
tail -n +2 "$CSV" | awk -F',' '$4 ~ /^5/ {print $3}' \
| sort | uniq -c \
| sort -k1,1nr -k2,2 \
| head -n 2

# 计算平均latency_ms，保留两位小数，跳过表头
tail -n +2 "$CSV" | awk -F',' '{sum+=$5; cnt++} END {printf "avg latency: %.2f\n", sum/cnt}'
