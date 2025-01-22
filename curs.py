import os
import subprocess
import curses
import signal
import platform

def list_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.py')]

def run_file(file_path):
    return subprocess.Popen(["python3", file_path])

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    directory_path = 'demos/'  
    current_row = 0
    process = None
    files = list_files(directory_path)

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Используйте стрелки для навигации, Enter для выбора файла, q для выхода из скрипта\n")

        for idx, file in enumerate(files):
            x = 2
            y = idx + 1
            if idx == current_row:
                stdscr.addstr(y, x, f"-> {file}", curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, f"   {file}")

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(files) - 1:
            current_row += 1
        elif key == 10:  # Enter
            selected_file = files[current_row]
            file_path = os.path.join(directory_path, selected_file)

            if process:
                process.terminate()
                process = None

            current_file = selected_file
            process = run_file(file_path)

        elif key == ord('q'):
            if process and current_file == files[current_row]: 
                process.terminate()
                process = None
                current_file = None
            break

if __name__ == "__main__":
    curses.wrapper(main)
