import matplotlib.pyplot as plt
import math

def apply_rules(axiom, rules, iterations):
    """
    L-System string generator
    :param axiom: Initial string
    :param rules: Dictionary, symbol rewriting rules
    :param iterations: Number of iterations
    :return: Generated string after iterations
    """
    current = axiom
    for _ in range(iterations):
        next_seq = []
        for c in current:
            next_seq.append(rules.get(c, c))
        current = ''.join(next_seq)
    return current

def draw_l_system(commands, angle_deg, step, initial_pos=(0, 0), initial_angle=90, tree_mode=False, savefile=None):
    """
    L-System plotter
    :param commands: Command string
    :param angle_deg: Angle to turn each time
    :param step: Step length
    :param initial_pos: Initial position
    :param initial_angle: Initial direction (degrees)
    :param tree_mode: Whether to use fractal tree mode (affects behavior of [ and ])
    :param savefile: If specified, save the plot to this file
    """
    x, y = initial_pos
    current_angle = initial_angle
    stack = []
    fig, ax = plt.subplots()
    for cmd in commands:
        if cmd in ('F', '0', '1'):
            nx = x + step * math.cos(math.radians(current_angle))
            ny = y + step * math.sin(math.radians(current_angle))
            ax.plot([x, nx], [y, ny], color='green' if tree_mode else 'blue', linewidth=1.2 if tree_mode else 1)
            x, y = nx, ny
        elif cmd == 'f':
            x += step * math.cos(math.radians(current_angle))
            y += step * math.sin(math.radians(current_angle))
        elif cmd == '+':
            current_angle += angle_deg
        elif cmd == '-':
            current_angle -= angle_deg
        elif cmd == '[':
            stack.append((x, y, current_angle))
            if tree_mode:
                current_angle += angle_deg
        elif cmd == ']':
            x, y, current_angle = stack.pop()
            if tree_mode:
                current_angle -= angle_deg
    ax.set_aspect('equal')
    ax.axis('off')
    if savefile:
        plt.savefig(savefile, bbox_inches='tight', pad_inches=0.1, dpi=150)
        plt.close()
    else:
        plt.show()

if __name__ == "__main__":
    # Koch curve parameters
    koch_axiom = "F"
    koch_rules = {'F': 'F+F--F+F'}
    koch_angle = 60
    koch_iter = 4
    koch_step = 5
    koch_cmds = apply_rules(koch_axiom, koch_rules, koch_iter)
    plt.figure(figsize=(10, 3))
    draw_l_system(koch_cmds, koch_angle, koch_step, initial_pos=(0, 0), initial_angle=0)
    plt.title("L-System Koch Curve")
    plt.axis('equal')
    plt.axis('off')
    plt.show()

    # Fractal tree parameters
    tree_axiom = "0"
    tree_rules = {'1': '11', '0': '1[0]0'}
    tree_angle = 45
    tree_iter = 7
    tree_step = 7
    tree_cmds = apply_rules(tree_axiom, tree_rules, tree_iter)
    plt.figure(figsize=(7, 7))
    draw_l_system(tree_cmds, tree_angle, tree_step, initial_pos=(0, 0), initial_angle=90, tree_mode=True)
    plt.title("L-System Fractal Tree")
    plt.axis('equal')
    plt.axis('off')
    plt.show()
