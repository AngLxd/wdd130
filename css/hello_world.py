#print('Hello world')


name= input('What is your favorite color?')
print('Your favorite color is'+ name)

import tkinter as tk
def display_color():
    color=entry.get()
    try:
        label.config(bg=color)
        label.config(text=f'Your favorite color is{color}!')
    except tk.TclError:
        label.config(text='Invalid Color', bg='white')
window= tk.Tk()
window.title('Favorite Color')
window.geometry('300x200')
entry= tk.Entry(window, width=20)
entry.pack(pady=10)
button=tk.Button(window, text='Submit', command=display_color)
button.pack(pady=10)
label=tk.Label(window, text='What is your favorite color?', bg='white', fg='black', font=('Helvetica',16))
label.pack(expand=True, fill='both')
window.mainloop()