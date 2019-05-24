# -*- coding:utf-8 -*-

import tkinter

class Scribble:
    # 繝懊ち繝ｳ縺梧款縺輔ｌ縺�
    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y,
                                outline = self.color.get(),
                                width = self.width.get())

    # 繝峨Λ繝�げ
    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y,
                                fill = self.color.get(),
                                width = self.width.get())
        self.sx = event.x
        self.sy = event.y

    # 繧ｦ繧｣繝ｳ繝峨え繧剃ｽ懊ｋ
    def create_window(self):
        window = tkinter.Tk()
        self.canvas = tkinter.Canvas(window, bg = "white", 
                                     width = 300, height = 300)
        self.canvas.pack()
        quit_button = tkinter.Button(window, text = "邨ゆｺ�",
                                     command = window.quit)
        quit_button.pack(side = tkinter.RIGHT)

        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)

        # 濶ｲ繧帝∈縺ｶ
        COLORS = ["red", "green", "blue", "#FF00FF", "black"]
        self.color = tkinter.StringVar()                    
        self.color.set(COLORS[1])                             
        b = tkinter.OptionMenu(window, self.color, *COLORS) 
        b.pack(side = tkinter.LEFT)

        # 邱壹�螟ｪ縺輔ｒ驕ｸ縺ｶ
        self.width = tkinter.Scale(window, from_ = 1, to = 15,
                                   orient = tkinter.HORIZONTAL) 
        self.width.set(5)                                       
        self.width.pack(side = tkinter.LEFT)
        
        return window;
    
    def __init__(self):
        self.window = self.create_window();  # 蜻ｼ縺ｳ蜃ｺ縺吶→縺阪�self. + 繝｡繧ｽ繝�ラ蜷�
            
    def run(self):
        self.window.mainloop()

# 髢句ｧ�   
Scribble().run()
