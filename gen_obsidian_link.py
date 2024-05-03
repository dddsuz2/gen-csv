import os
import re

# ユーザーからの入力でフォルダパスを受け取る
input_folder_path = input("フォルダパスを入力してください: ")
folder_path = input_folder_path.replace("\\", "/").replace("C:", "/mnt/c")

def extract_numbers(file_name):
    # ファイル名から数字を抽出する
    matches = re.findall(r'(\d+(?:\.\d+)?)', file_name)
    return [float(match) for match in matches]

def generate_obsidian_links(folder_path):
    file_links = []
    files = os.listdir(folder_path)

    # ファイル名から数字を抽出し、複数の数字を持つ場合も考慮してソートする
    sorted_files = sorted(files, key=extract_numbers)

    for file_name in sorted_files:
        # 拡張子を取り除いたファイル名を生成
        file_name_without_extension = os.path.splitext(file_name)[0]
        
        # ファイル名からObsidianのリンク形式を生成
        obsidian_link = f"[[{file_name_without_extension}]]"
        file_links.append(obsidian_link)
    
    return file_links

# 指定されたフォルダ内のファイルからObsidianのリンクを生成
try:
    generated_links = generate_obsidian_links(folder_path)
    # 生成されたリンクを表示
    for link in generated_links:
        print(link)
except FileNotFoundError:
    print("指定されたフォルダが見つかりません。正しいパスを入力してください。")