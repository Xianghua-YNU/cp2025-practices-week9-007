"""
项目4: Mandelbrot与Julia集分形生成模板
请补全下方函数，实现Mandelbrot与Julia集的生成与可视化。
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot(width=800, height=800, max_iter=100):
    """
    生成Mandelbrot集数据
    :param width: 图像宽度(像素)
    :param height: 图像高度(像素) 
    :param max_iter: 最大迭代次数
    :return: 2D numpy数组，包含每个点的逃逸时间
    
    实现步骤:
    1. 创建x(-2.0到1.0)和y(-1.5到1.5)的线性空间
    2. 生成复数网格C
    3. 初始化Z和B数组
    4. 迭代计算逃逸时间
    """
    # TODO: 创建x和y的线性空间
    # TODO: 使用np.meshgrid生成网格
    # TODO: 构建复数矩阵C = x + iy
    x = np.linspace(-2,1,width)
    y = np.linspace(-1.5,1.5,height)
    Re,Im = np.meshgrid(x,y)
    C = Re + 1j*Im   
    # TODO: 初始化记录数组
    # B = np.zeros(...)  # 记录迭代次数
    # Z = np.zeros(...)  # 初始值设为0
    Z = np.zeros(C.shape,dtype=np.complex128)      #Z的初始值为零
    B = np.zeros(C.shape)               #记录迭代次数 
    # TODO: 迭代计算
    for j in range(max_iter):
        mask = np.abs(Z) <= 2
        B += mask
        Z[mask] = Z[mask]**2 + C[mask]
    # TODO: 返回转置后的结果
    return B.T

def generate_julia(c, width=800, height=800, max_iter=100):
    """
    生成Julia集数据
    :param c: Julia集参数(复数)
    :param width: 图像宽度(像素)
    :param height: 图像高度(像素)
    :param max_iter: 最大迭代次数
    :return: 2D numpy数组，包含每个点的逃逸时间
    
    实现步骤:
    1. 创建x和y的线性空间(-2.0到2.0)
    2. 生成复数网格Z0
    3. 初始化记录数组
    4. 迭代计算逃逸时间
    """
    # TODO: 创建x和y的线性空间
    # TODO: 使用np.meshgrid生成网格
    # TODO: 构建复数矩阵Z0 = x + iy
    x = np.linspace(-2,2,width)
    y = np.linspace(-2,2,height)
    Re,Im = np.meshgrid(x,y)
    Z0 = Re + 1j*Im
    # TODO: 初始化记录数组
    # B = np.zeros(...)  # 记录迭代次数
    # Z = Z0.copy()  # 初始值为网格点
    Z = Z0.copy()
    B = np.zeros(Z0.shape)         
    # TODO: 迭代计算
    for j in range(max_iter):
        mask = np.abs(Z) <= 2
        B += mask
        Z[mask] = Z[mask]**2 + c
    
    # TODO: 返回转置后的结果
    return B.T

def plot_fractal(data, title, filename=None, cmap='magma'):
    """
    绘制分形图像
    :param data: 分形数据(2D数组)
    :param title: 图像标题
    :param filename: 保存文件名(可选)
    :param cmap: 颜色映射
    """
    plt.figure(figsize=(10, 10))
    plt.imshow(data.T, cmap=cmap, origin='lower')
    plt.title(title)
    plt.axis('off')
    
    if filename:
        plt.savefig(filename, bbox_inches='tight', dpi=150)
    plt.show()

if __name__ == "__main__":
    # 示例参数
    width, height = 800, 800
    max_iter = 100
    
    # 生成并绘制Mandelbrot集
    mandelbrot = generate_mandelbrot(width, height, max_iter)
    plot_fractal(mandelbrot, "Mandelbrot Set", "mandelbrot.png")
    
    # 生成并绘制Julia集(多个c值)
    julia_c_values = [
        -0.8 + 0.156j,  # 经典Julia集
        -0.4 + 0.6j,    # 树枝状Julia集 
        0.285 + 0.01j   # 复杂结构Julia集
    ]
    
    for i, c in enumerate(julia_c_values):
        julia = generate_julia(c, width, height, max_iter)
        plot_fractal(julia, f"Julia Set (c = {c:.3f})", f"julia_{i+1}.png")
