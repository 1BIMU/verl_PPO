import pyarrow.parquet as pq

def count_parquet_rows_pyarrow(file_path):
    try:
        table = pq.read_table(file_path)
        print(f"文件 '{file_path}' 的行数: {table.num_rows}")
        print(f"列数: {table.num_columns}")
        return table.num_rows
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None

# 使用示例
count_parquet_rows_pyarrow("/home/wty/verl/data/dapo-math-17k.parquet")