import os
import pandas as pd

# 定义输入和输出路径
input_folder = r"D:\pipeline\360-json" # 输入文件夹路径
output_folder = r"D:\pipeline\360-excel"  # 输出文件夹路径

# 如果输出文件夹不存在，创建该文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有 JSON 文件
for file_name in os.listdir(input_folder):
    if file_name.endswith(".json"):
        # 构造 JSON 文件的完整路径
        json_file_path = os.path.join(input_folder, file_name)

        # 读取 JSON 文件
        try:
            df = pd.read_json(json_file_path)

            # 构造 Excel 输出文件的路径
            excel_file_name = f"{os.path.splitext(file_name)[0]}.xlsx"
            excel_file_path = os.path.join(output_folder, excel_file_name)

            # 将 DataFrame 保存为 Excel 文件
            df.to_excel(excel_file_path, index=False, engine='openpyxl')
            print(f"{file_name} 已成功转换为 Excel 文件。")
        except Exception as e:
            print(f"无法处理 {file_name}，错误：{e}")

print("所有文件处理完毕。")