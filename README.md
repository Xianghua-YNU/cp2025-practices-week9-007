[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KNfdPqNp)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19286374)
# 计算物理实验第九周：分形探索

欢迎来到分形的世界！本系列作业包含五个编程项目，旨在引导你探索和实践生成各种迷人分形图案的不同方法。你将使用 Python 编程语言，结合几何迭代、L-系统、迭代函数系统 (IFS) 和复数动力学等技术，亲手创造出这些复杂的结构。

## 学习目标

完成本系列作业后，你将能够：

*   理解并区分几种主要的分形生成范式：确定性几何迭代、L-系统、概率性迭代函数系统 (IFS) 和复数动力学。
*   使用 Python 编程语言实现这些分形生成算法。
*   利用 `matplotlib` 库将生成的分形进行可视化。
*   体会简单规则如何通过迭代产生复杂的、具有自相似性的结构。
*   初步理解分形维数的概念，并能动手实现盒计数法来估算分形维数。
*   欣赏数学和计算在模拟自然形态和探索复杂系统中的力量。

## 作业概览

本次大作业包含以下五个独立的编程项目：

1.  **项目 1: 确定性迭代 I - 相似性变换生成曲线分形**
2.  **项目 2: 确定性迭代 II - L-System 生成分形 (曲线与树)**
3.  **项目 3: 随机迭代 - 概率性迭代函数系统 (IFS)**
4.  **项目 4: 复数动力学 - Mandelbrot 与 Julia 集**
5.  **项目 5: 分形分析 - 盒计数法估算分形维数**

请按顺序完成这些项目，后面的项目可能会用到前面项目建立的概念或技能。

## 通用指南

*   **编程语言:** 所有项目请使用 Python 3.x 完成。
*   **库:**
    *   项目 1 & 2: 推荐使用 `matplotlib.pyplot` 进行绘图，例如使用 `plot` 函数绘制线段。
    *   项目 3 & 4: 推荐使用 `matplotlib.pyplot` 进行点集的绘制 (`scatter`) 和图像显示 (`imshow`)。可能需要 `random` 库 (项目 3) 和 `cmath` 或 `numpy` (项目 4)。
    *   项目 5: 需要 `matplotlib` (用于绘图和可能的图像处理)，以及 `numpy` (用于数组操作和线性回归)。
    *   请确保安装了必要的库 (`pip install matplotlib numpy`)。
*   **代码风格:** 请编写清晰、结构良好、有适当注释的代码。使用有意义的变量名。
*   **提交:**
    *   通过 GitHub Classroom 接受作业邀请，这会为你创建一个私有仓库。
    *   将你的代码 (`.py` 文件) 和生成的图像 (`.png` 或 `.jpg` 文件) 添加到你的仓库中。
    *   对于每个项目，确保提交了所有要求的代码和结果文件。
    *   通过 `git commit` 和 `git push` 将你的工作提交到 GitHub 仓库。请确保在截止日期前完成最终提交。

---

## 项目目录结构
```
p2025-practice-week9/
├── Exp1-相似性迭代生成分形曲线/        # 项目1：通过几何相似变换生成分形曲线
│   ├── Iteration_koch_minkowski.py     # 主程序文件，实现科赫曲线和闵可夫斯基香肠曲线的生成
│   ├── solution/                       # 参考答案目录
│   │   ├── Iteration_koch_minkowski_solution.py  # 项目1的参考解决方案
│   ├── tests/                          # 测试目录
│   │   └── test_Iteration_koch_minkowski.py  # 项目1的测试用例
│   ├── 实验报告.md                     # 项目1的实验报告模板
│   └── 项目说明.md                     # 项目1的详细说明文档
├── Exp2-L系统分形/                     # 项目2：L系统生成分形
│   ├── L_system.py                     # 主程序文件，实现L系统分形生成算法
│   ├── solution/                       # 参考答案目录
│   │   ├── L_system_solution.py        # 项目2的参考解决方案
│   ├── tests/                          # 测试目录
│   │   └── test_L_system.py            # 项目2的测试用例
│   ├── 实验报告.md                     # 项目2的实验报告模板
│   └── 项目说明.md                     # 项目2的详细说明文档
├── Exp3-迭代函数系统分形/              # 项目3：迭代函数系统(IFS)生成分形
│   ├── ifs.py                          # 主程序文件，实现IFS分形生成算法
│   ├── solution/                       # 参考答案目录
│   │   ├── ifs_solution.py             # 项目3的参考解决方案
│   ├── tests/                          # 测试目录
│   │   └── test_ifs.py                 # 项目3的测试用例
│   ├── 实验报告.md                     # 项目3的实验报告模板
│   └── 项目说明.md                     # 项目3的详细说明文档
├── Exp4-曼德勃罗特集和朱利亚集分形/    # 项目4：复数动力学分形
│   ├── mandelbrot_julia.py             # 主程序文件，实现Mandelbrot和Julia集的计算
│   ├── solution/                       # 参考答案目录
│   │   ├── mandelbrot_julia_solution.py # 项目4的参考解决方案
│   ├── tests/                          # 测试目录
│   │   └── test_mandelbrot_julia.py    # 项目4的测试用例
│   ├── 实验报告.md                     # 项目4的实验报告模板
│   └── 项目说明.md                     # 项目4的详细说明文档
├── Exp5-盒维数的计算/                  # 项目5：分形维数计算
│   ├── box_counting.py                 # 主程序文件，实现盒计数法计算分形维数
│   ├── solution/                       # 参考答案目录
│   │   ├── box_counting_solution.py    # 项目5的参考解决方案
│   ├── tests/                          # 测试目录
│   │   └── test_box_counting.py        # 项目5的测试用例
│   ├── 实验报告.md                     # 项目5的实验报告模板
│   └── 项目说明.md                     # 项目5的详细说明文档
├── images/                             # 图像资源目录
│   └── barnsley_fern.png               # 示例分形图像(巴恩斯利蕨)
├── README.md                           # 项目总说明文档(当前文件)
└── requirements.txt                    # Python依赖库列表 
```

## 评估

你的作业将基于以下方面进行评估：

*   **功能正确性:** 代码是否能成功生成所要求的分形图案？维数计算是否合理？
*   **算法实现:** 是否正确理解并实现了相应的分形生成算c法或分析方法？
*   **代码质量:** 代码是否清晰、结构良好、有注释、易于理解？
*   **结果呈现:** 生成的图像是否清晰、符合预期？分析结果是否明确报告？
*   **完成度:** 是否完成了所有要求的任务和提交了所有必需的文件？

## 资源

*   维基百科等在线资源关于各种分形（Koch Curve, Mandelbrot Set, IFS 等）的介绍。

## 获取帮助

如果在完成作业过程中遇到困难，请利用课程提供的答疑渠道（助教）。

祝你探索分形之旅愉快！
