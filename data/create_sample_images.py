#!/usr/bin/env python3
"""
サンプル画像データ作成スクリプト
画像処理教材用の様々な種類のサンプル画像を生成
"""

import numpy as np
from PIL import Image
import os
from pathlib import Path

# ディレクトリ作成
data_dir = Path(__file__).parent
(images_dir := data_dir / "images").mkdir(exist_ok=True)
(synthetic_dir := data_dir / "synthetic").mkdir(exist_ok=True)

def create_basic_shapes():
    """基本形状の画像を作成"""
    # 白背景
    white_bg = np.ones((400, 600, 3), dtype=np.uint8) * 255

    # 円形
    circle = np.zeros((200, 200, 3), dtype=np.uint8)
    center = 100
    y, x = np.ogrid[:200, :200]
    mask = (x - center)**2 + (y - center)**2 <= 90**2
    circle[mask] = [255, 0, 0]  # 赤い円

    # 長方形
    rectangle = np.zeros((150, 250, 3), dtype=np.uint8)
    rectangle[25:125, 175:225] = [0, 255, 0]  # 緑の長方形

    # 三角形
    triangle = np.zeros((200, 200, 3), dtype=np.uint8)
    triangle[100:200, 50:150] = [0, 0, 255]  # 青の三角形

    # 画像を配置
    composite = white_bg.copy()
    composite[50:250, 50:250] = circle
    composite[100:250, 300:550] = rectangle
    composite[200:400, 300:500] = triangle

    # 保存
    Image.fromarray(composite).save(synthetic_dir / "basic_shapes.jpg")
    print("基本形状画像を作成: basic_shapes.jpg")

def create_gradient_images():
    """グラデーション画像を作成"""
    # 水平グラデーション
    gradient_h = np.zeros((300, 600, 3), dtype=np.uint8)
    for i in range(600):
        gradient_h[:, i] = i * 255 // 600
    Image.fromarray(gradient_h).save(synthetic_dir / "horizontal_gradient.jpg")

    # 垂直グラデーション
    gradient_v = np.zeros((300, 600, 3), dtype=np.uint8)
    for i in range(300):
        gradient_v[i, :] = i * 255 // 300
    Image.fromarray(gradient_v).save(synthetic_dir / "vertical_gradient.jpg")

    # カラーグラデーション
    color_grad = np.zeros((300, 600, 3), dtype=np.uint8)
    for i in range(600):
        color_grad[:, i, 0] = i * 255 // 600  # R
        color_grad[:, i, 1] = 255 - i * 255 // 600  # G
        color_grad[:, i, 2] = 128  # B
    Image.fromarray(color_grad).save(synthetic_dir / "color_gradient.jpg")

    print("グラデーション画像を作成")

def create_noise_images():
    """ノイズ画像を作成"""
    # ガウシアンノイズ
    gaussian_noise = np.random.normal(128, 50, (400, 600, 3))
    gaussian_noise = np.clip(gaussian_noise, 0, 255).astype(np.uint8)
    Image.fromarray(gaussian_noise).save(synthetic_dir / "gaussian_noise.jpg")

    # salt and pepperノイズ
    sp_noise = np.random.randint(0, 256, (400, 600, 3), dtype=np.uint8)
    salt_pepper = np.random.random((400, 600, 3))
    sp_noise[salt_pepper < 0.05] = 0
    sp_noise[salt_pepper > 0.95] = 255
    Image.fromarray(sp_noise).save(synthetic_dir / "salt_pepper_noise.jpg")

    print("ノイズ画像を作成")

def create_pattern_images():
    """パターン画像を作成"""
    # チェスボード
    chess = np.zeros((400, 400, 3), dtype=np.uint8)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                chess[i*50:(i+1)*50, j*50:(j+1)*50] = 255
    Image.fromarray(chess).save(synthetic_dir / "chessboard.jpg")

    # 縞模様
    stripes = np.zeros((300, 600, 3), dtype=np.uint8)
    for i in range(0, 600, 30):
        stripes[:, i:i+15] = [128, 128, 128]
    Image.fromarray(stripes).save(synthetic_dir / "stripes.jpg")

    print("パターン画像を作成")

def save_image_list():
    """画像リストを保存"""
    images = list(synthetic_dir.glob("*.jpg"))
    with open(data_dir / "image_list.txt", "w") as f:
        f.write("サンプル画像リスト:\n")
        f.write("-" * 30 + "\n")
        for img in sorted(images):
            f.write(f"{img.name}\n")
    print(f"画像リストを保存: {len(images)}個の画像")

if __name__ == "__main__":
    print("サンプル画像データ作成を開始...")
    create_basic_shapes()
    create_gradient_images()
    create_noise_images()
    create_pattern_images()
    save_image_list()
    print("\nサンプル画像データ作成完了！")