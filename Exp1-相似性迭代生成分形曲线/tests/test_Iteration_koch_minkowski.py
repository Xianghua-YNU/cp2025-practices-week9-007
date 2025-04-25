import os
import sys
import json
import subprocess
import pytest
from pathlib import Path


def load_config():
    """
    从 config.json 文件加载测试配置。
    若文件不存在或解析出错，程序将退出并给出相应提示。
    """
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config.get('tests', [])
    except FileNotFoundError:
        print("未找到配置文件 config.json")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"解析配置文件时出错: {e}")
        sys.exit(1)


TESTS = load_config()


def run_test(test_file):
    """
    运行单个测试文件并返回测试结果。
    若测试文件不存在或运行时出现意外错误，会打印错误信息并返回 False。
    """
    try:
        result = pytest.main(["-v", test_file])
        return result == 0
    except FileNotFoundError:
        print(f"测试文件 {test_file} 不存在！")
        return False
    except Exception as e:
        print(f"运行测试 {test_file} 时发生意外错误: {e}")
        return False


def calculate_score():
    """
    计算总分并生成测试结果列表。
    遍历所有测试，运行每个测试并根据结果计算得分，最后返回总分、满分和结果列表。
    """
    total_points = 0
    max_points = 0
    results = []

    for test in TESTS:
        max_points += test["points"]
        test_file = test["file"]
        test_name = test["name"]
        points = test["points"]

        print(f"运行测试: {test_name}")
        passed = run_test(test_file)

        if passed:
            total_points += points
            status = "通过"
        else:
            status = "失败"

        results.append({
            "name": test_name,
            "status": status,
            "points": points if passed else 0,
            "max_points": points
        })

        print(f"  状态: {status}")
        print(f"  得分: {points if passed else 0}/{points}")
        print()

    print(f"总分: {total_points}/{max_points}")
    return total_points, max_points, results


def generate_markdown_report(results, total_points, max_points):
    """
    生成 Markdown 格式的测试报告。
    若生成过程中出现错误，会打印错误信息。
    """
    try:
        with open(os.environ.get('GITHUB_STEP_SUMMARY', 'score_summary.md'), 'w') as f:
            f.write("# 自动评分结果\n\n")
            f.write("| 测试 | 状态 | 得分 |\n")
            f.write("|------|------|------|\n")

            for result in results:
                f.write(f"| {result['name']} | {result['status']} | {result['points']}/{result['max_points']} |\n")

            f.write(f"\n## 总分: {total_points}/{max_points}\n")
    except Exception as e:
        print(f"生成 Markdown 报告时出错: {e}")


def generate_json_report(results, total_points, max_points):
    """
    生成 JSON 格式的测试报告。
    若生成过程中出现错误，会打印错误信息。
    """
    try:
        score_data = {
            "score": total_points,
            "max_score": max_points,
            "tests": results
        }

        with open('score.json', 'w') as f:
            json.dump(score_data, f, indent=2)
    except Exception as e:
        print(f"生成 JSON 报告时出错: {e}")


if __name__ == "__main__":
    try:
        project_root = Path(__file__).parent.parent.parent
        os.chdir(project_root)
    except Exception as e:
        print(f"切换工作目录时出错: {e}")
        sys.exit(1)

    try:
        print("安装依赖...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError:
        print("安装依赖失败，请检查 requirements.txt 文件及网络连接等情况。")
        sys.exit(1)
    except FileNotFoundError:
        print("未找到 requirements.txt 文件。")
        sys.exit(1)

    print("\n开始评分...\n")
    total, maximum, results = calculate_score()

    generate_markdown_report(results, total, maximum)
    generate_json_report(results, total, maximum)

    if 'GITHUB_OUTPUT' in os.environ:
        try:
            with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
                f.write(f"points={total}\n")
        except Exception as e:
            print(f"设置 GitHub Actions 输出变量时出错: {e}")

    sys.exit(0 if total == maximum else 1)
