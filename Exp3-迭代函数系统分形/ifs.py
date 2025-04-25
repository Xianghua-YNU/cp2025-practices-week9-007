import numpy as np
import matplotlib.pyplot as plt

def get_fern_params():
    """返回巴恩斯利蕨的IFS参数"""
    # 每个变换包含6个参数(a,b,c,d,e,f)和概率p
    return [
        [0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.01],   # 茎干
        [0.85, 0.04, -0.04, 0.85, 0.00, 1.60, 0.85],   # 小叶片
        [0.20, -0.26, 0.23, 0.22, 0.00, 1.60, 0.07],   # 左侧大叶片
        [-0.15, 0.28, 0.26, 0.24, 0.00, 0.44, 0.07]    # 右侧大叶片
    ]

def get_tree_params():
    """返回概率树的IFS参数""" 
    return [
        [0.00, 0.00, 0.00, 0.50, 0.00, 0.00, 0.10],    # 树干
        [0.42, -0.42, 0.42, 0.42, 0.00, 0.20, 0.45],   # 左分支
        [0.42, 0.42, -0.42, 0.42, 0.00, 0.20, 0.45]    # 右分支
    ]

def apply_transform(point, params):
    """应用单个变换到点"""
    x, y = point
    a, b, c, d, e, f, _ = params
    return a*x + b*y + e, c*x + d*y + f

def run_ifs(ifs_params, num_points=100000, num_skip=100):
    """
    运行IFS迭代生成点集
    :param ifs_params: IFS参数列表
    :param num_points: 总点数
    :param num_skip: 跳过前n个点(避免初始不稳定)
    :return: 生成的点坐标数组
    """
    # 提取概率用于随机选择
    probs = [p[-1] for p in ifs_params]
    indices = np.arange(len(ifs_params))
    
    # 初始化
    point = (0.5, 0)  # 初始点
    points = np.zeros((num_points, 2))
    
    # 迭代生成点
    for i in range(num_points + num_skip):
        # 随机选择变换
        idx = np.random.choice(indices, p=probs)
        point = apply_transform(point, ifs_params[idx])
        
        # 跳过初始不稳定点
        if i >= num_skip:
            points[i - num_skip] = point
            
    return points

def plot_ifs(points, title="IFS Fractal", save_path=None):
    """绘制IFS分形并保存为PNG"""
    plt.figure(figsize=(8, 8))
    plt.scatter(points[:,0], points[:,1], s=1, c='green', alpha=0.75)
    plt.title(title)
    plt.axis('equal')
    plt.axis('off')
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()

if __name__ == "__main__":
    # 生成并绘制巴恩斯利蕨
    fern_params = get_fern_params()
    fern_points = run_ifs(fern_params)
    plot_ifs(fern_points, "Barnsley Fern", "barnsley_fern.png")
    
    # 生成并绘制概率树
    tree_params = get_tree_params()
    tree_points = run_ifs(tree_params)
    plot_ifs(tree_points, "Probability Tree", "probability_tree.png")
