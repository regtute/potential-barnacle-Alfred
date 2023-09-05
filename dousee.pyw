
import pyperclip


def extract_text(text):
    # 查找第一个出现的"https://"的位置
    start_index = text.find("https://")
    
    if start_index != -1:
        # 查找最后一个"/"的位置
        end_index = text.rfind("/")
        
        if end_index != -1:
            # 提取从"https://"到最后一个"/"之间的文本
            return text[start_index:end_index+1]
    
    # 如果没有找到指定的文本，则返回空字符串
    return ""

# 示例文本
text = pyperclip.paste()


# 提取指定文本
extracted_text = extract_text(text)

# 输出提取的文本
pyperclip.copy(extracted_text)
