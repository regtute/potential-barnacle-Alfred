from datetime import datetime
import pyperclip





clipboard_content = pyperclip.paste()


time_format = "%Y-%m-%d"

# 尝试将剪贴板内容解析为时间
try:
    parsed_time = datetime.strptime(clipboard_content, time_format)
    
    # 将解析后的时间转换为10位数字的时间戳
    timestamp = int(parsed_time.timestamp())
    
    # 将转换后的时间戳复制到剪贴板
    pyperclip.copy(str(timestamp))

except:
    if clipboard_content.isdigit() and len(clipboard_content) == 10:
        timestamp = datetime.fromtimestamp(int(clipboard_content))
        
        # 格式化时间戳为 "%Y-%m-%d %H:%M:%S" 格式
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        
        # 将格式化后的时间戳复制到剪贴板
        pyperclip.copy(formatted_timestamp)

    else:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        pyperclip.copy(formatted_time)


# 1624733200
# 2022-3-4
# 1646323200