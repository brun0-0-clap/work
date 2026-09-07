# ex03 研究 deactivate shell函数

1. `which deactivate` 的输出结果：（粘贴输出）
> deactivate 不是磁盘上的可执行程序，是bash内存中的shell函数。

2. deactivate函数主要完成的工作：
- 恢复激活虚拟环境之前备份的PATH环境变量
- 取消VIRTUAL_ENV环境变量
- 把shell提示符恢复到激活前的样式
- 执行unset，删除deactivate自身这个函数，退出环境后无法再次调用

3. 理解：
虚拟环境激活是修改当前shell进程的环境变量；deactivate负责撤销全部修改，恢复shell原始状态。它只对当前终端会话生效，不会修改系统全局配置。
