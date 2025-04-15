import tkinter as tk
from tkinter import ttk, messagebox

class ArmyChessTrackerTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("四国军棋记棋器")
        self.geometry("1000x650")
        
        # 初始化棋子数据
        self.players = ["对家", "上家", "下家"]
        self.pieces = {
            "司令": 1,
            "军长": 1,
            "师长": 2,
            "旅长": 2,
            "团长": 2,
            "营长": 2,
            "连长": 3,
            "排长": 3,
            "工兵": 3,
            "地雷": 3,
            "军旗": 1
        }
        
        # 颜色选项
        self.color_options = {
            "橙色": "#FFA500",
            "蓝色": "#1E90FF",
            "紫色": "#9370DB",
            "绿色": "#3CB371"
        }
        
        # 初始化数据存储
        self.player_data = {}
        self.player_colors = {}
        self.used_colors = set()
        
        for player in self.players:
            self.player_data[player] = self.pieces.copy()
            self.player_colors[player] = None
        
        self.init_ui()
    
    def init_ui(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 为每个玩家创建面板
        for i, player in enumerate(self.players):
            player_frame = ttk.LabelFrame(main_frame, text=player)
            player_frame.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)
            
            # 颜色选择部分
            color_frame = ttk.Frame(player_frame)
            color_frame.pack(fill=tk.X, pady=(0, 10))
            
            ttk.Label(color_frame, text="选择颜色:").pack(side=tk.LEFT)
            
            color_var = tk.StringVar()
            color_cb = ttk.Combobox(
                color_frame,
                textvariable=color_var,
                values=list(self.color_options.keys()),
                state="readonly"
            )
            color_cb.pack(side=tk.LEFT, padx=5)
            color_cb.bind("<<ComboboxSelected>>", 
                         lambda e, p=player: self.change_color(p))
            setattr(self, f"{player}_color_cb", color_cb)
            
            # 棋子部分
            for piece, initial_count in self.pieces.items():  # 修复这里
                piece_frame = ttk.Frame(player_frame)
                piece_frame.pack(fill=tk.X, padx=5, pady=2)
                
                label = ttk.Label(piece_frame, text=f"{piece}: {self.player_data[player][piece]}")
                label.pack(side=tk.LEFT, padx=(0, 10))
                setattr(self, f"{player}_{piece}_label", label)
                
                btn = ttk.Button(piece_frame, text="-", width=3,
                                command=lambda p=player, pc=piece: self.decrease_piece(p, pc))
                btn.pack(side=tk.RIGHT)
            
            main_frame.columnconfigure(i, weight=1)
    
    def change_color(self, player):
        color_cb = getattr(self, f"{player}_color_cb")
        selected_color_name = color_cb.get()
        
        if not selected_color_name:
            return
            
        selected_color = self.color_options[selected_color_name]
        
        # 检查颜色是否已被使用
        if selected_color in self.used_colors:
            current_user = [p for p, c in self.player_colors.items() if c == selected_color][0]
            messagebox.showwarning("颜色冲突", 
                                 f"该颜色已被{current_user}使用，请选择其他颜色！")
            color_cb.set("")
            return
            
        # 更新颜色
        if self.player_colors[player]:
            self.used_colors.remove(self.player_colors[player])
            
        self.player_colors[player] = selected_color
        self.used_colors.add(selected_color)
        
        # 应用颜色样式
        style = ttk.Style()
        style.configure(f"{player}.TLabelframe", 
                      background=selected_color,
                      bordercolor="black",
                      lightcolor=selected_color,
                      darkcolor=selected_color)
        
        # 找到对应的LabelFrame并应用样式
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Frame):  # 主框架
                for child in widget.winfo_children():
                    if isinstance(child, ttk.LabelFrame) and child["text"] == player:
                        child.configure(style=f"{player}.TLabelframe")
                        break
    
    def decrease_piece(self, player, piece):
        if self.player_data[player][piece] > 0:
            self.player_data[player][piece] -= 1
            label = getattr(self, f"{player}_{piece}_label")
            label.config(text=f"{piece}: {self.player_data[player][piece]}")
            
            if self.player_data[player][piece] == 0:
                label.config(foreground="red")
            else:
                label.config(foreground="black")

if __name__ == "__main__":
    app = ArmyChessTrackerTk()
    app.mainloop()