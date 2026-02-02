#!/usr/bin/env python3
"""
シンプルなサンプル画像データ作成スクリプト
標準ライブラリのみを使用して基本的な画像を作成
"""

import os
import sys
from pathlib import Path

# ディレクトリ作成
data_dir = Path(__file__).parent
(images_dir := data_dir / "images").mkdir(exist_ok=True)
(synthetic_dir := data_dir / "synthetic").mkdir(exist_ok=True)

def create_text_image():
    """テキストベースの簡単な画像ファイルを作成"""
    # PPM形式（プレーンフォーマット）で画像を作成
    def create_ppm(filename, width, height, color):
        with open(filename, 'w') as f:
            f.write(f"P3\n{width} {height}\n255\n")
            for y in range(height):
                for x in range(width):
                    f.write(f"{color[0]} {color[1]} {color[2]} ")
                f.write("\n")

    # 基本的な画像を作成
    create_ppm(synthetic_dir / "red_rect.ppm", 300, 200, (255, 0, 0))
    create_ppm(synthetic_dir / "green_circle.ppm", 200, 200, (0, 255, 0))
    create_ppm(synthetic_dir / "blue_bg.ppm", 400, 300, (0, 0, 255))
    create_ppm(synthetic_dir / "gradient.ppm", 300, 100,
              [(i, i, i) for i in range(100) for _ in range(3)])

    print("基本画像ファイルを作成")

def create_test_patterns():
    """テストパターンを作成"""
    patterns = {
        "checkerboard.ppm": "Checkerboard pattern",
        "horizontal_stripes.ppm": "Horizontal stripes",
        "vertical_lines.ppm": "Vertical lines",
        "diagonal.ppm": "Diagonal pattern"
    }

    for filename, desc in patterns.items():
        with open(synthetic_dir / filename, 'w') as f:
            f.write(f"P3\n200 200\n255\n")
            if "Checkerboard" in desc:
                for y in range(200):
                    for x in range(200):
                        if (x // 20 + y // 20) % 2 == 0:
                            f.write("255 255 255 ")
                        else:
                            f.write("0 0 0 ")
                    f.write("\n")
            elif "Horizontal" in desc:
                for y in range(200):
                    color = 255 if y < 100 else 0
                    for x in range(200):
                        f.write(f"{color} {color} {color} ")
                    f.write("\n")
            elif "Vertical" in desc:
                for y in range(200):
                    for x in range(200):
                        color = 255 if x < 100 else 0
                        f.write(f"{color} {color} {color} ")
                    f.write("\n")

    print("テストパターンを作成")

def save_image_list():
    """画像リストを保存"""
    images = list(synthetic_dir.glob("*.ppm"))
    with open(data_dir / "image_list.txt", "w") as f:
        f.write("サンプル画像リスト（PPM形式）:\n")
        f.write("-" * 30 + "\n")
        for img in sorted(images):
            f.write(f"{img.name}\n")
    print(f"画像リストを保存: {len(images)}個の画像")

if __name__ == "__main__":
    print("シンプルなサンプル画像データ作成を開始...")
    create_text_image()
    create_test_patterns()
    save_image_list()
    print("\nサンプル画像データ作成完了！")