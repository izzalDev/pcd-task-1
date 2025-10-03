# import customtkinter as ctk
#
# # Inisialisasi tema dan ukuran jendela
# ctk.set_appearance_mode("System")  # Bisa: "Light", "Dark", "System"
# ctk.set_default_color_theme("blue")  # Warna tema: blue, dark-blue, green
#
# # Membuat class untuk aplikasi
# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("PCD Task 1")
#         self.geometry("600x400")  # Perbesar ukuran untuk ruang sidebar
#
#         # ========= Layout Frame =========
#         # Sidebar (kiri)
#         self.sidebar = ctk.CTkFrame(self, width=150, corner_radius=0)
#         self.sidebar.pack(side="left", fill="y")
#
#         # Konten utama (kanan)
#         self.main_content = ctk.CTkFrame(self)
#         self.main_content.pack(side="left", fill="both", expand=True)
#
#         # ========= Sidebar Widgets =========
#         self.sidebar_label = ctk.CTkLabel(self.sidebar, text="MENU", font=ctk.CTkFont(size=16, weight="bold"))
#         self.sidebar_label.pack(pady=(20, 10))
#
#         self.home_button = ctk.CTkButton(self.sidebar, text="Home", command=self.show_home)
#         self.home_button.pack(pady=5, fill="x", padx=10)
#
#         self.about_button = ctk.CTkButton(self.sidebar, text="Tentang", command=self.show_about)
#         self.about_button.pack(pady=5, fill="x", padx=10)
#
#         # ========= Main Content Widgets =========
#         self.label = ctk.CTkLabel(self.main_content, text="Masukkan Nama Anda:")
#         self.label.pack(pady=10)
#
#         self.entry = ctk.CTkEntry(self.main_content, placeholder_text="Nama")
#         self.entry.pack(pady=10)
#
#         self.button = ctk.CTkButton(self.main_content, text="Sapa Saya", command=self.say_hello)
#         self.button.pack(pady=10)
#
#         self.output_label = ctk.CTkLabel(self.main_content, text="")
#         self.output_label.pack(pady=10)
#
#     def say_hello(self):
#         name = self.entry.get()
#         if name:
#             self.output_label.configure(text=f"Halo, {name}!")
#         else:
#             self.output_label.configure(text="Silakan masukkan nama terlebih dahulu.")
#
#     def show_home(self):
#         self.output_label.configure(text="")  # Kosongkan output
#         self.label.configure(text="Masukkan Nama Anda:")
#
#     def show_about(self):
#         self.label.configure(text="Aplikasi ini dibuat untuk tugas PCD.")
#         self.output_label.configure(text="Silakan kembali ke Home untuk memasukkan nama.")
#
# # Menjalankan aplikasi
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
import customtkinter as ctk
import tkinter as tk
from typing import List

frame: tk.Frame = tk.Frame()
frame.pack_configure

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__() # type: ignore

        self.title("Input Matriks 3x3")
        self.geometry("500x400")

        # ======== Area Input Matriks ========
        self.matrix_frame: ctk.CTkFrame = ctk.CTkFrame(self, width=400)
        self.matrix_frame.pack(pady=20)

        # List untuk menyimpan 3x3 CTkEntry
        self.entries: List[List[ctk.CTkEntry]] = []

        for _ in range(3):  # Baris
            row_frame: ctk.CTkFrame = ctk.CTkFrame(self.matrix_frame, fg_color="transparent")
            row_frame.pack(pady=5)

            row_entries: List[ctk.CTkEntry] = []
            for _ in range(3):  # Kolom
                entry: ctk.CTkEntry = ctk.CTkEntry(row_frame, width=60, justify="center")
                entry.pack(side="left", padx=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Tombol untuk menampilkan nilai matriks
        self.submit_button: ctk.CTkButton = ctk.CTkButton(
            self.matrix_frame,
            text="Tampilkan Matriks",
            command=self.show_matrix
        )
        self.submit_button.pack(pady=10)

        self.result_label: ctk.CTkLabel = ctk.CTkLabel(self.matrix_frame, text="", justify="left")
        self.result_label.pack(pady=10)

    def show_matrix(self) -> None:
        matrix: List[List[float]] = []

        for row in self.entries:
            current_row: List[float] = []
            for entry in row:
                val: str = entry.get()
                try:
                    num: float = float(val)
                    current_row.append(num)
                except ValueError:
                    current_row.append(0.0)  # Default ke 0 jika kosong / salah input
            matrix.append(current_row)

        # Tampilkan hasil
        output: str = "\n".join([str(row) for row in matrix])
        self.result_label.configure(text=output)


if __name__ == "__main__":
    app: App = App()
    app.mainloop()
