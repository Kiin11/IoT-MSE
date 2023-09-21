import tkinter as tk


def onClick():
    name = txtA.get("1.0", "end")
    age = txtB.get("1.0", "end")

def set_text_value_A(str):
    txtA.delete(1.0, tk.END)  # Xóa nội dung hiện tại trong Text widget
    # new_text = "Đây là nội dung mới."  # Thay thế bằng nội dung bạn muốn đặt
    txtA.insert(tk.END, str)
def set_text_value_B(str):
    txtB.delete(1.0, tk.END)  # Xóa nội dung hiện tại trong Text widget
    # new_text = "Đây là nội dung mới."  # Thay thế bằng nội dung bạn muốn đặt
    txtB.insert(tk.END, str)


window = tk.Tk()
window.title("Python app")
# window.geometry("600x400")
window.attributes('-fullscreen', True)

labelA = tk.Label(text="Nhiet do")
labelA.place(x=5, y=5, width=80, height=30)

txtA = tk.Text()
txtA.place(x=85, y=5, width=100, height=30)

labelB = tk.Label(text="Do Am")
labelB.place(x=5, y=35, width=80, height=30)

txtB = tk.Text()
txtB.place(x=85, y=35, width=100, height=30)

button = tk.Button(text="save", command=onClick)
button.place(x=5, y=125, width=100, height=50)
