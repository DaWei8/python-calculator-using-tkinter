import tkinter as tk

message_received = ""
message_sent = ""

root = tk.Tk()
root.geometry("300x400")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 14))
text_result.grid(row=2, column=1, columnspan=4)

btn_send = tk.Button(root, text=">",height=2, width=16)
btn_send.grid(row=2, column=2)

root.mainloop()
