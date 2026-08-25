#!/bin/bash

echo "=====1.创建test.sh脚本===="
rm -f test.sh
touch test.sh
echo 'echo hello' > test.sh

echo "=====2.查看原始权限（无x执行位）===="
ls -l test.sh

echo "=====3.直接./执行，会权限拒绝 ===="
./test.sh

echo "=====4.bash解释器方式运行，不需要x权限 ===="
bash test.sh

echo "=====5.添加可执行权限chmod +x ===="
chmod +x test.sh

echo "=====6.再次查看权限，出现x标记 ===="
ls -l test.sh

echo "=====7.添加权限后 ./直接运行 ===="
./test.sh

rm -f test.sh
