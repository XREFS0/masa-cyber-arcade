"""
MASA Arcade Hub: Rock-Paper-Scissors & Cyber Tic-Tac-Toe
Developer: MASA
"""

import random
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MasaArcadeHub(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MASA Cyber Arcade Hub")
        self.geometry("540x680")
        self.resizable(False, False)
        self.configure(fg_color="#0A0E17")

        self._build_shell()
        self._show_rps_view()

    def _build_shell(self):
        top_bar = ctk.CTkFrame(self, fg_color="#121826", corner_radius=14)
        top_bar.pack(fill="x", padx=20, pady=(15, 10))

        title = ctk.CTkLabel(
            top_bar,
            text="MASA ARCADE HUB",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#F59E0B",
        )
        title.pack(pady=(10, 4))

        self.tab_selector = ctk.CTkSegmentedButton(
            top_bar,
            values=["Rock-Paper-Scissors", "Tic-Tac-Toe"],
            command=self._on_tab_change,
            selected_color="#D97706",
            selected_hover_color="#B45309",
        )
        self.tab_selector.set("Rock-Paper-Scissors")
        self.tab_selector.pack(pady=(0, 10))

        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=20, pady=(0, 15))

    def _on_tab_change(self, choice):
        for w in self.main_container.winfo_children():
            w.destroy()
        if choice == "Rock-Paper-Scissors":
            self._show_rps_view()
        else:
            self._show_ttt_view()

    # --- RPS GAME ---
    def _show_rps_view(self):
        self.rps_user_score = 0
        self.rps_cpu_score = 0

        card = ctk.CTkFrame(self.main_container, fg_color="#121826", corner_radius=16)
        card.pack(fill="both", expand=True)

        score_frame = ctk.CTkFrame(card, fg_color="#0A0E17", corner_radius=12)
        score_frame.pack(fill="x", padx=20, pady=15)
        score_frame.grid_columnconfigure(0, weight=1)
        score_frame.grid_columnconfigure(1, weight=1)

        self.lbl_rps_p1 = ctk.CTkLabel(
            score_frame,
            text="YOU\n0",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#38BDF8",
        )
        self.lbl_rps_p1.grid(row=0, column=0, pady=10)

        self.lbl_rps_cpu = ctk.CTkLabel(
            score_frame,
            text="CPU\n0",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#F43F5E",
        )
        self.lbl_rps_cpu.grid(row=0, column=1, pady=10)

        self.lbl_rps_status = ctk.CTkLabel(
            card,
            text="Select your weapon to begin",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#E2E8F0",
        )
        self.lbl_rps_status.pack(pady=10)

        self.lbl_rps_detail = ctk.CTkLabel(
            card,
            text="First to reach 5 points claims victory",
            font=ctk.CTkFont(size=12),
            text_color="#94A3B8",
        )
        self.lbl_rps_detail.pack(pady=(0, 20))

        btn_row = ctk.CTkFrame(card, fg_color="transparent")
        btn_row.pack(fill="x", padx=20, pady=10)
        btn_row.grid_columnconfigure((0, 1, 2), weight=1, uniform="rps")

        weapons = [("🪨 Rock", "Rock", 0), ("📄 Paper", "Paper", 1), ("✂️ Scissors", "Scissors", 2)]
        for label, val, col in weapons:
            b = ctk.CTkButton(
                btn_row,
                text=label,
                font=ctk.CTkFont(size=14, weight="bold"),
                fg_color="#1E293B",
                hover_color="#334155",
                height=48,
                corner_radius=10,
                command=lambda v=val: self._play_rps(v),
            )
            b.grid(row=0, column=col, padx=5, sticky="ew")

        ctk.CTkButton(
            card,
            text="Reset Scores",
            font=ctk.CTkFont(size=12),
            fg_color="#374151",
            hover_color="#4B5563",
            corner_radius=8,
            command=self._reset_rps,
        ).pack(side="bottom", pady=15)

    def _play_rps(self, user_choice):
        if self.rps_user_score >= 5 or self.rps_cpu_score >= 5:
            return

        cpu_choice = random.choice(["Rock", "Paper", "Scissors"])
        if user_choice == cpu_choice:
            outcome = "Draw! Both chose " + user_choice
            color = "#FBBF24"
        elif (user_choice == "Rock" and cpu_choice == "Scissors") or \
             (user_choice == "Paper" and cpu_choice == "Rock") or \
             (user_choice == "Scissors" and cpu_choice == "Paper"):
            self.rps_user_score += 1
            outcome = f"You Won! {user_choice} beats {cpu_choice}"
            color = "#34D399"
        else:
            self.rps_cpu_score += 1
            outcome = f"CPU Scored! {cpu_choice} beats {user_choice}"
            color = "#F87171"

        self.lbl_rps_p1.configure(text=f"YOU\n{self.rps_user_score}")
        self.lbl_rps_cpu.configure(text=f"CPU\n{self.rps_cpu_score}")
        self.lbl_rps_status.configure(text=outcome, text_color=color)

        if self.rps_user_score >= 5:
            self.lbl_rps_detail.configure(text="MATCH CHAMPION! Congratulations MASA Player!", text_color="#34D399")
        elif self.rps_cpu_score >= 5:
            self.lbl_rps_detail.configure(text="DEFEAT! CPU took the series.", text_color="#F87171")

    def _reset_rps(self):
        self.rps_user_score = 0
        self.rps_cpu_score = 0
        self.lbl_rps_p1.configure(text="YOU\n0")
        self.lbl_rps_cpu.configure(text="CPU\n0")
        self.lbl_rps_status.configure(text="Select your weapon to begin", text_color="#E2E8F0")
        self.lbl_rps_detail.configure(text="First to reach 5 points claims victory", text_color="#94A3B8")

    # --- TIC TAC TOE GAME ---
    def _show_ttt_view(self):
        self.ttt_board = [""] * 9
        self.ttt_turn = "X"
        self.ttt_active = True

        card = ctk.CTkFrame(self.main_container, fg_color="#121826", corner_radius=16)
        card.pack(fill="both", expand=True)

        self.ttt_status = ctk.CTkLabel(
            card,
            text="Player X's Turn",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#38BDF8",
        )
        self.ttt_status.pack(pady=(15, 10))

        grid_frame = ctk.CTkFrame(card, fg_color="#0A0E17", corner_radius=12)
        grid_frame.pack(padx=20, pady=10)
        grid_frame.grid_columnconfigure((0, 1, 2), weight=1, uniform="ttt")
        grid_frame.grid_rowconfigure((0, 1, 2), weight=1, uniform="ttt")

        self.ttt_buttons = []
        for i in range(9):
            btn = ctk.CTkButton(
                grid_frame,
                text="",
                font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold"),
                fg_color="#1E293B",
                hover_color="#334155",
                width=85,
                height=85,
                corner_radius=10,
                command=lambda idx=i: self._ttt_click(idx),
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.ttt_buttons.append(btn)

        ctk.CTkButton(
            card,
            text="New Game",
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#D97706",
            hover_color="#B45309",
            corner_radius=8,
            height=38,
            command=self._reset_ttt,
        ).pack(side="bottom", pady=15)

    def _ttt_click(self, idx):
        if not self.ttt_active or self.ttt_board[idx] != "":
            return

        self.ttt_board[idx] = self.ttt_turn
        color = "#38BDF8" if self.ttt_turn == "X" else "#F43F5E"
        self.ttt_buttons[idx].configure(text=self.ttt_turn, text_color=color)

        if self._check_ttt_winner(self.ttt_turn):
            self.ttt_status.configure(text=f"Player {self.ttt_turn} Wins the Grid!", text_color="#34D399")
            self.ttt_active = False
            return

        if "" not in self.ttt_board:
            self.ttt_status.configure(text="Stalemate! Game Tied.", text_color="#FBBF24")
            self.ttt_active = False
            return

        self.ttt_turn = "O" if self.ttt_turn == "X" else "X"
        turn_color = "#38BDF8" if self.ttt_turn == "X" else "#F43F5E"
        self.ttt_status.configure(text=f"Player {self.ttt_turn}'s Turn", text_color=turn_color)

    def _check_ttt_winner(self, p):
        b = self.ttt_board
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(b[x] == b[y] == b[z] == p for x, y, z in wins)

    def _reset_ttt(self):
        self.ttt_board = [""] * 9
        self.ttt_turn = "X"
        self.ttt_active = True
        self.ttt_status.configure(text="Player X's Turn", text_color="#38BDF8")
        for b in self.ttt_buttons:
            b.configure(text="", fg_color="#1E293B")


if __name__ == "__main__":
    app = MasaArcadeHub()
    app.mainloop()
