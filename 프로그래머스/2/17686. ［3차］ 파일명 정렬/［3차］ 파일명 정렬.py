def solution(files):
    return sorted(files, key=lambda x: split_file_name(x))

def split_file_name(file_name):
    file_name = file_name.lower()
    
    # 1. split TAIL
    if '.' in file_name:
        file_name = file_name[:file_name.index('.')]
    
    # 2. split HEAD and NUMBER
    start_idx = False
    for idx in range(len(file_name)):
        if not start_idx and file_name[idx].isdigit():
            start_idx = idx
            continue
        if start_idx != False and not file_name[idx].isdigit():
            return [file_name[:start_idx], int(file_name[start_idx:idx])]
    return [file_name[:start_idx], int(file_name[start_idx:])]