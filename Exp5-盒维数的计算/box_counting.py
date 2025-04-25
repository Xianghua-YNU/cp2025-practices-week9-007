import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_and_binarize_image(image_path, threshold=128):
    """
    加载图像并转换为二值数组
    :param image_path: 图像文件路径
    :param threshold: 二值化阈值 (0-255)
    :return: 二值化的NumPy数组 (0和1)
    """
    img = Image.open(image_path).convert('L')  # 转换为灰度
    img_array = np.array(img)
    binary_image = (img_array > threshold).astype(int)
    return binary_image

def box_count(binary_image, box_sizes):
    """
    盒计数算法实现
    :param binary_image: 二值图像数组
    :param box_sizes: 盒子尺寸列表
    :return: 字典 {box_size: count}
    """
    height, width = binary_image.shape
    counts = {}
    
    for box_size in box_sizes:
        # 计算网格行列数
        rows = height // box_size
        cols = width // box_size
        
        count = 0
        
        # 遍历所有盒子
        for i in range(rows):
            for j in range(cols):
                # 获取当前盒子区域
                box = binary_image[i*box_size:(i+1)*box_size, 
                                  j*box_size:(j+1)*box_size]
                
                # 检查盒子是否包含前景像素
                if np.any(box == 1):
                    count += 1
        
        counts[box_size] = count
    
    return counts

def calculate_fractal_dimension(binary_image, min_box_size=1, max_box_size=None, num_sizes=10):
    """
    计算分形维数
    :param binary_image: 二值图像数组
    :param min_box_size: 最小盒子尺寸
    :param max_box_size: 最大盒子尺寸
    :param num_sizes: 盒子尺寸数量
    :return: 盒维数, 拟合结果
    """
    if max_box_size is None:
        max_box_size = min(binary_image.shape) // 2
    
    # 生成等比数列的盒子尺寸
    box_sizes = np.logspace(np.log2(min_box_size), np.log2(max_box_size), 
                           num=num_sizes, base=2).astype(int)
    box_sizes = np.unique(box_sizes)  # 去除重复值
    
    # 执行盒计数
    counts = box_count(binary_image, box_sizes)
    
    # 准备回归数据
    epsilons = np.array(list(counts.keys()))
    N_epsilons = np.array(list(counts.values()))
    
    # 对数变换
    log_eps = np.log(epsilons)
    log_N = np.log(N_epsilons)
    
    # 线性回归
    slope, intercept = np.polyfit(log_eps, log_N, 1)
    D = -slope
    
    return D, (epsilons, N_epsilons, slope, intercept)

def plot_log_log(epsilons, N_epsilons, slope, intercept, save_path=None):
    """
    绘制log-log图
    """
    log_eps = np.log(epsilons)
    log_N = np.log(N_epsilons)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(log_eps, log_N, label='Data points')
    
    # 绘制拟合直线
    fit_line = slope * log_eps + intercept
    plt.plot(log_eps, fit_line, 'r-', 
             label=f'Fit line (slope={-slope:.3f})')
    
    plt.xlabel('log(ε)')
    plt.ylabel('log(N(ε))')
    plt.title('Box Counting Method - log-log plot')
    plt.legend()
    plt.grid(True)
    
    if save_path:
        plt.savefig(save_path)
    plt.show()

if __name__ == "__main__":
    # 示例用法
    IMAGE_PATH = "barnsley.png"  # 修改为指向images目录的相对路径
    
    # 1. 加载并二值化图像
    binary_img = load_and_binarize_image(IMAGE_PATH)
    
    # 2. 计算分形维数
    D, (epsilons, N_epsilons, slope, intercept) = calculate_fractal_dimension(binary_img)
    
    # 3. 输出结果
    print("盒计数结果:")
    for eps, N in zip(epsilons, N_epsilons):
        print(f"ε = {eps:4d}, N(ε) = {N:6d}, log(ε) = {np.log(eps):.3f}, log(N) = {np.log(N):.3f}")
    
    print(f"\n拟合斜率: {slope:.5f}")
    print(f"估算的盒维数 D = {D:.5f}")
    
    # 4. 绘制log-log图
    plot_log_log(epsilons, N_epsilons, slope, intercept, "log_log_plot.png")
