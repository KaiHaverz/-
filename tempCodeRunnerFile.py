import tkinter as tk
from tkinter import ttk

class ArmyChessTrackerTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("四国军棋记棋器")
        self.geometry("580x500")
        self.configure(bg="#333333")  # 深灰色背景
        
        # 初始化数据
        self.players = ["对家", "上家", "下家"]
        self.pieces = {
            "司令": 1, "军长": 1, "师长": 2, "旅长": 2,
            "团长": 2, "营长": 2, "连长": 3, "排长": 3,
            "工兵": 3, "地雷": 3, "军旗": 1
        }
        
        # 存储棋子数据
        self.player_data = {p: self.pieces.copy() for p in self.players}
        
        self.init_styles()
        self.init_ui()
    
    def init_styles(self):
        """初始化样式"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 基础样式
        style.configure('TFrame', background='#333333')
        style.configure('TLabel', background='#333333', foreground='white')
        style.configure('TButton', background='#555555', foreground='white')
        
        # 标题样式（14号加粗字体）
        style.configure('Title.TLabel', 
                      font=('Microsoft YaHei', 14, 'bold'),
                      foreground='white',
                      background='#333333',
                      anchor='center')
    
    def init_ui(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        for i, player in enumerate(self.players):
            # 创建玩家面板框架
            player_frame = ttk.Frame(main_frame)
            player_frame.grid(row=0, column=i, sticky="nsew", padx=5, pady=5)
            
            # 添加标题标签（居中显示）
            title = ttk.Label(
                player_frame,
                text=player,
                style='Title.TLabel'
            )
            title.pack(fill=tk.X, pady=(0, 10))
            
            # 棋子记录部分
            for piece in self.pieces:
                self.create_piece_ui(player_frame, player, piece)
            
            main_frame.columnconfigure(i, weight=1)
    
    def create_piece_ui(self, parent, player, piece):
        """创建棋子UI组件"""
        piece_frame = ttk.Frame(parent)
        piece_frame.pack(fill=tk.X, padx=5, pady=2)
        
        # 棋子标签（白色文字）
        label = ttk.Label(
            piece_frame, 
            text=f"{piece}: {self.player_data[player][piece]}",
            foreground='white'
        )
        label.pack(side=tk.LEFT, padx=(0, 10))
        setattr(self, f"{player}_{piece}_label", label)
        
        # 按钮区域
        btn_frame = ttk.Frame(piece_frame)
        btn_frame.pack(side=tk.RIGHT)
        
        # +1按钮
        ttk.Button(
            btn_frame, 
            text="+1", 
            width=3,
            command=lambda p=player, pc=piece: self.increase_piece(p, pc)
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        # -1按钮
        ttk.Button(
            btn_frame, 
            text="-1", 
            width=3,
            command=lambda p=player, pc=piece: self.decrease_piece(p, pc)
        ).pack(side=tk.LEFT)
    
    def decrease_piece(self, player, piece):
        """减少棋子数量"""
        if self.player_data[player][piece] > 0:
            self.player_data[player][piece] -= 1
            self.update_piece_display(player, piece)
    
    def increase_piece(self, player, piece):
        """增加棋子数量"""
        self.player_data[player][piece] += 1
        self.update_piece_display(player, piece)
    
    def update_piece_display(self, player, piece):
        """更新棋子显示"""
        label = getattr(self, f"{player}_{piece}_label")
        label.config(text=f"{piece}: {self.player_data[player][piece]}")
        
        # 数量为0时变红
        if self.player_data[player][piece] == 0:
            label.config(foreground="red")
        else:
            label.config(foreground="white")

if __name__ == "__main__":
    app = ArmyChessTrackerTk()
    app.mainloop()