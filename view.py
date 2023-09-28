import tkinter as tk


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}')


def get_screen_dimensions():
    root = tk.Tk()

    # Lấy kích thước màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Đóng cửa sổ ngay sau khi lấy kích thước
    root.destroy()

    return screen_width, screen_height


# Sử dụng hàm để lấy kích thước màn hình
width, height = get_screen_dimensions()

def onClick():
    # name = txtA.get("1.0", "end")
    # age = txtB.get("1.0", "end")
    pass

def set_text_value_A(str):
    # txtA.delete(1.0, tk.END)  # Xóa nội dung hiện tại trong Text widget
    # # new_text = "Đây là nội dung mới."  # Thay thế bằng nội dung bạn muốn đặt
    # txtA.insert(tk.END, str)
    pass

def set_text_value_B(str):
    # txtB.delete(1.0, tk.END)  # Xóa nội dung hiện tại trong Text widget
    # # new_text = "Đây là nội dung mới."  # Thay thế bằng nội dung bạn muốn đặt
    # txtB.insert(tk.END, str)
    pass

def set_text_label_A(value):
    labelA = 'Temperarture: ' + str(value)

def set_text_label_B(value):
    labelB = 'Moisture: ' + str(value)


window = tk.Tk()
window.title("Python app")
# window.geometry("600x400")
window.attributes('-fullscreen', True)

# Tạo label A
labelA = tk.Label(window, text="Temperarture: 0.0", font=("Helvetica", 16))
labelA.pack(pady=10)

# Tạo label 2
labelB = tk.Label(window, text="Moisture: 0.0", font=("Helvetica", 16))
labelB.pack(pady=10)

center_window(window, width, height)
# labelA = tk.Label(text="Temperarture")
# labelA.place(x=5, y=5, width=80, height=30)

# txtA = tk.Text()
# txtA.place(x=85, y=5, width=100, height=30)

# labelB = tk.Label(text="Moisture")
# labelB.place(x=5, y=35, width=80, height=30)

# txtB = tk.Text()
# txtB.place(x=85, y=35, width=100, height=30)

