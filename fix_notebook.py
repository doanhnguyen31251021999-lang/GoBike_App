import nbformat


file_path = 'Ai_Go_Bike.ipynb'

with open(file_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Xóa metadata widgets bị lỗi cấu trúc
if 'widgets' in nb.metadata:
    del nb.metadata['widgets']
    print("Đã xóa metadata lỗi thành công!")

with open(file_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
