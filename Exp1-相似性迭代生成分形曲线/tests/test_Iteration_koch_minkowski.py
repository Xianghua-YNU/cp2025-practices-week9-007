import numpy as np
import matplotlib.pyplot as plt

def koch_generator(u, level):
    u = np.array([0, 1j]) # 初始竖直线段
    
    if level <= 0:
        return u
        
    theta = np.pi/3 # 旋转角度
    for _ in range(level):
        new_u = []
        for i in range(len(u)-1):
            start = u[i]
            end = u[i+1]
            
            # 生成科赫曲线的四个新线段
            p1 = start
            p2 = start + (end - start)/3
            p3 = p2 + (end - start)/3 * np.exp(1j*theta)
            p4 = start + 2*(end - start)/3
            p5 = end
            
            new_u.extend([p1, p2, p3, p4, p5])
        
        u = np.array(new_u)
    
    return u

def minkowski_generator(u, level):
    u = np.array([0, 1]) # 初始水平线段
    
    theta = np.pi/2 # 旋转角度
    for _ in range(level):
        new_u = []
        for i in range(len(u)-1):
            start = u[i]
            end = u[i+1]
            
            # 生成Minkowski曲线的八个新线段
            p1 = start
            p2 = start + (end - start)/4
            p3 = p2 + (end - start)/4 * np.exp(1j*theta)
            p4 = p2 + (end - start)/4 * (1 + 1j)
            p5 = start + (end - start)/2 + (end - start)/4 * 1j
            p6 = start + (end - start)/2
            p7 = start + (end - start)/2 - (end - start)/4 * 1j
            p8 = start + 3*(end - start)/4 - (end - start)/4 * 1j
            p9 = start + 3*(end - start)/4
            p10 = end
            
            new_u.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        
        u = np.array(new_u)
    
    return u


if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])
    
    # 创建2x2子图布局
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    
    # 生成不同层级的科赫曲线
    for i in range(4):
        koch_points = koch_generator(init_u, i+1)
        axs[i//2, i%2].plot(koch_points.real, koch_points.imag, 'k-', lw=1)
        axs[i//2, i%2].set_title(f"Koch Curve Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    
    plt.tight_layout()
    plt.show()

    # 生成不同层级的Minkowski香肠
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        minkowski_points = minkowski_generator(init_u, i+1)
        axs[i//2, i%2].plot(minkowski_points.real, minkowski_points.imag, 'k-', lw=1)
        axs[i//2, i%2].set_title(f"Minkowski Sausage Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    
    plt.tight_layout()
    plt.show()
