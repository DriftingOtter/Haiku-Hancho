import tkinter as tk

def init_window(title="Tkinter Window", x_size=None, y_size=None):
    win = tk.Tk()
    win.wm_title(title)

    # Set window size if specified
    if (x_size is not None) and (y_size is not None):
        win.wm_geometry(f"{x_size}x{y_size}")

    return win

def set_grid(window, cols, rows):
    for row in range(len(rows)):
        window.grid_rowconfigure(row, weight=rows[row])

    for col in range(len(cols)):
        window.grid_columnconfigure(col, weight=cols[col])

def get_haiku_topic():
    return "The spring..."

def main():
    # Initializing Window
    win = init_window("Haiku Hacho")

    # Set window grid
    rows = [1, 1, 2]
    cols = [1, 1, 2]
    set_grid(win, cols, rows)

    # App title
    title = tk.Label(win,
                     text = "Haiku Hancho",
                     font = ("Arial", 30))
    title.grid(row=0, column=0, columnspan=3, sticky="nw", padx=(50,0), pady=(50,0))

    # Get topic for user to write
    haiku_topic = get_haiku_topic()

    # Haiku topic display
    topic = tk.Label(win,
                     text = haiku_topic,
                     font = ("Arial", 30))
    topic.grid(row=1, column=1, columnspan=1, sticky="nw", padx=(50,0), pady=(5,0))

    # Topic re-roll button
    topic_reset = tk.Button(win,
                            text = "\U0001F3B2",
                            font = ("Arial", 20))
    topic_reset.grid(row=1, column=2, columnspan=1, sticky="nw", padx=(5,0), pady=(5,0))

    # Settings button
    settings = tk.Button(win,
                            text = "?",
                            font = ("Arial", 20))
    settings.grid(row=1, column=3, columnspan=1, sticky="ne", padx=(0,50), pady=(5,0))

    # Haiku entry box
    entry_box = tk.Text(win,
                        font   = ("Arial", 50),
                        wrap   = "word",
                        height = 10)
    entry_box.grid(row=2, column=1, columnspan=3, sticky="swe", padx=(50,50), pady=(5,50))

    # Run GUI loop
    win.mainloop()

if __name__ == "__main__":
    main()

