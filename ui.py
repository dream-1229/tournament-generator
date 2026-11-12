import tkinter as tk
import platform     #OS判別

from control    import translate_list
from main       import main_function

is_mac = platform.system() == "Darwin"      #OS判別

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Main Page", font=("Helvetica", 35))
        label.pack(expand=True)

        button = tk.Button(self, text="作成開始",command=lambda: controller.show_frame("SportListPage"))
        button.pack()



class Input_SportNamePage(tk.Frame):
    def __init__(self, parent, controller):
            super().__init__(parent)

            label   = tk.Label(self, text="種目名入力", font=("Helvetica", 35))
            label.pack(pady=30)

            entry = tk.Entry(self, font=("Helvetica", 20))
            entry.pack(pady=10)

            def save_sport_name():
                sport_name = entry.get().strip()
                if not sport_name:
                    return
                controller.sport_name   = sport_name
                controller.show_frame("class_main")

            button  = tk.Button(self, text="決定", command=save_sport_name)
            button.pack()
            

class Input_class_listPage(tk.Frame):
    def __init__(self, parent, controller, title, name, target_list, max_select, bg, next_page, first_state):
        super().__init__(parent)
        self.controller     = controller
        self.target_list    = target_list
        self.max_select     = max_select
        self.bg             = bg
        self.next_page      = next_page
        self.first_state    = first_state
        default_bg          = self.cget("bg")


        def toggle_class(r, c, b):
            nonlocal all_selected

            address = (r+1)*10 + (c+1)

            if address in self.target_list:
                self.target_list.remove(address)
                if is_mac:
                    b.config(highlightbackground=default_bg)     #MacOS
                else:
                    b.config(bg=default_bg)                      #WindowsOS
            else:
                if len(self.target_list) < self.max_select:
                    self.target_list.append(address)
                    if is_mac:
                        b.config(highlightbackground=self.bg)
                    else:
                        b.config(bg=self.bg)
            print(name, self.target_list)

            if self.max_select != 3:
                all_selected = len(self.target_list) == 25
                if all_selected:
                    toggle_button.config(text="全解除")
                else:
                    toggle_button.config(text="全選択")

                if len(self.target_list) >= 8:     #8クラス未満
                    next_button.config(state="normal")   
                else:
                    next_button.config(state="disabled") 

        def toggle_all():
            nonlocal all_selected

            if not all_selected:
                self.target_list.clear()

                for row in range(5):
                    for column in range(5):
                        address = (row+1)*10 + (column+1)
                        self .target_list.append(address)
                        button = class_buttons[(row, column)]
                        if is_mac:
                            button.config(highlightbackground=self.bg)
                        else:
                            button.config(bg=self.bg)

                toggle_button.config(text="全解除")
                next_button.config(state ="normal")
                all_selected = True

            else:
                self.target_list.clear()

                for button in class_buttons.values():
                    if is_mac:
                        button.config(highlightbackground=default_bg)
                    else:
                        button.config(bg=default_bg)

                toggle_button.config(text="全選択")
                if self.max_select != 3:
                    next_button.config(state="disabled")

                all_selected = False
                
            print(name, self.target_list)

        #__________
        top_area    = tk.Frame(self)
        top_area.pack(fill="x")

        label       = tk.Label(self, text=title, font=("Helvetica", 35))
        label.pack(pady=20)
        #__________
        grid_area   =tk.Frame(self)
        grid_area.pack(expand=True)

        class_buttons = {}
        all_selected = False
        class_type  = ["A", "E", "S", "C", "M"]

        for row in range(5):
            for column, letter in enumerate(class_type):        #enumerate:https://note.nkmk.me/python-enumerate-start/
                text    = f"{row+1}{letter}"
    
                class_button  = tk.Button(grid_area, text=text)
                class_buttons[(row, column)] = class_button
                class_button.config(command= lambda r=row, c=column, b=class_button:toggle_class(r, c, b))
                class_button.grid(row=row, column=column)
        #__________
        bottom_area =tk.Frame(self)
        bottom_area.pack()

        if self.max_select != 3:
            all_selected = False
            toggle_button = tk.Button(bottom_area, text="全選択", command=toggle_all)
            toggle_button.pack(side="left", padx=5)

        next_button = tk.Button(bottom_area, text="完了", command=lambda: controller.show_frame(self.next_page), state=first_state)
        next_button.pack(side="left", padx=5)
        #__________


class SportListPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller =controller

        #__________    
        show_list_area  =tk.Frame(self)
        show_list_area.pack()

        self.sport_label = tk.Label(self, text="登録されている種目はありません", font=("Helvetica", 20))
        self.sport_label.pack(pady=30)

        self.add_button  = tk.Button(self, text="種目を追加", command=lambda: controller.show_frame("Input_SportNamePage"))
        self.add_button.pack(pady=10)

        self.create_button = tk.Button(self, text="作成開始", state="disabled", command=self.make_tornament)
        self.create_button.pack(pady=10)
        #__________
        
    def on_show(self):
        if self.controller.class_list:
            self.controller.sport_registered = True

            self.sport_label.config(text=self.controller.sport_name)
            self.add_button.config(state="disabled")
            self.create_button.config(state="normal")
        else:
            self.sport_label.config(text="登録されている種目はありません")
            self.add_button.config(state="normal")
            self.create_button.config(state="disabled")
    
    def make_tornament(self):
        main_function(
            self.controller.sport_name,
            self.controller.class_list,
            self.controller.class_ex_list
        )
        self.controller.show_frame("FinalPage")

class FinalPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="完成", font=("Helvetica", 35))
        label.pack(expand=True)



class class_main(Input_class_listPage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller,
                        title       = "出場クラス",
                        name        = "first_list       :",
                        target_list = controller.class_list,
                        max_select  = 25,
                        bg          = "#E00000",
                        next_page   = "ex_class",
                        first_state = "disabled"
                        )

class ex_class(Input_class_listPage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller,
                        title       = "優秀戦績クラス",
                        name        = "first_ex_list    :",
                        target_list = controller.class_ex_list,
                        max_select  = 3,
                        bg          = "#005EE0",
                        next_page   = "SportListPage",
                        first_state = "normal"
                        )


class App(tk.Tk):
    def __init__(self):

        super().__init__()
        self.title("Tkinter change page")
        self.geometry("800x600")

        self.sport_name         = ""
        self.class_list         = []
        self.class_ex_list      = []
        self.sport_registered   = False

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (
                MainPage, 
                SportListPage,
                Input_SportNamePage,
                class_main, ex_class, 
                FinalPage
                ):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if hasattr(frame, "on_show"):
            frame.on_show()
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()