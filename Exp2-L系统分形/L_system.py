"""
L-System分形生成与绘图

"""
import matplotlib.pyplot as plt
import math

def generate_lsystem(axiom, productions, generations):
    """
    L系统字符串生成器
    :param axiom: 初始公理字符串
    :param productions: 产生式规则字典
    :param generations: 迭代次数
    :return: 生成后的字符串
    """
    current = axiom
    for _ in range(generations):
        next_gen = []
        for symbol in current:
            next_gen.append(productions.get(symbol, symbol))
        current = ''.join(next_gen)
    return current

def render_lsystem(commands, turn_angle, move_step, 
                  start_point=(0,0), heading=90, 
                  is_tree=False, output_file=None):
    """
    L系统绘图器
    :param commands: 指令字符串
    :param turn_angle: 转向角度（度）
    :param move_step: 移动步长
    :param start_point: 起始坐标
    :param heading: 初始朝向（0向右，90向上）
    :param is_tree: 是否绘制分形树模式
    :param output_file: 输出文件名
    """
    # 设置非交互式后端（解决Spyder显示问题）
    plt.switch_backend('agg')
    
    x, y = start_point
    current_heading = heading
    state_stack = []
    
    # 初始化画布
    fig = plt.figure(figsize=(7, 7) if is_tree else (10, 3))
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 解析指令
    for char in commands:
        if char in {'F', '0', '1'}:
            dx = move_step * math.cos(math.radians(current_heading))
            dy = move_step * math.sin(math.radians(current_heading))
            ax.plot([x, x+dx], [y, y+dy], 
                    color='#2E8B57' if is_tree else '#1E90FF',
                    linewidth=1.5 if is_tree else 1)
            x += dx
            y += dy
        elif char == '+':
            current_heading += turn_angle
        elif char == '-':
            current_heading -= turn_angle
        elif char == '[':
            state_stack.append((x, y, current_heading))
            if is_tree:
                current_heading += turn_angle  # 左转分支
        elif char == ']':
            if state_stack:
                x, y, current_heading = state_stack.pop()
                if is_tree:
                    current_heading -= turn_angle  # 右转返回
    
    # 输出处理
    if output_file:
        plt.savefig(output_file, bbox_inches='tight', dpi=120)
        plt.close(fig)
    else:
        plt.show()

if __name__ == "__main__":
    # 科赫曲线配置
    koch_config = {
        "axiom": "F",
        "rules": {"F": "F+F--F+F"},
        "iterations": 4,
        "angle": 60,
        "step": 5,
        "start_angle": 0
    }
    
    # 分形树配置
    tree_config = {
        "axiom": "0",
        "rules": {"1": "11", "0": "1[0]0"},
        "iterations": 7,
        "angle": 45,
        "step": 7,
        "start_angle": 90
    }
    
    # 生成科赫曲线
    koch_commands = generate_lsystem(koch_config["axiom"], 
                                    koch_config["rules"], 
                                    koch_config["iterations"])
    render_lsystem(koch_commands, 
                  koch_config["angle"], 
                  koch_config["step"],
                  start_point=(0, 0),
                  heading=koch_config["start_angle"],
                  output_file="koch_curve.png")
    
    # 生成分形树
    tree_commands = generate_lsystem(tree_config["axiom"], 
                                    tree_config["rules"], 
                                    tree_config["iterations"])
    render_lsystem(tree_commands, 
                  tree_config["angle"], 
                  tree_config["step"],
                  start_point=(0, 0),
                  heading=tree_config["start_angle"],
                  is_tree=True,
                  output_file="fractal_tree.png")
