
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import turtle
import tkinter.ttk as ttk

# Функция для выполнения команд
def execute_commands():
    try:
        # Очистка экрана черепахи
        turtle.clear()

        # Получение команд из текстового поля
        commands = command_block.get("1.0", tk.END).strip().split("\n")

        # Выполнение команд
        for command in commands:
            if command.startswith("вперёд"):
                distance = int(command.split()[1])
                turtle.forward(distance)
            elif command.startswith("назад"):
                distance = int(command.split()[1])
                turtle.backward(distance)
            elif command.startswith("вправо"):
                angle = int(command.split()[1])
                turtle.right(angle)
            elif command.startswith("влево"):
                angle = int(command.split()[1])
                turtle.left(angle)
            else:
                messagebox.showerror("Ошибка", f"Неизвестная команда: {command}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка выполнения команды: {e}")

# Функция для добавления команды в блок
def add_command(command):
    command_block.insert(tk.END, command + "\n")

# Создание основного окна
root = tk.Tk()
root.title("Проект")
root.geometry("1920x1080")

frame = Frame(
   root,
   padx=10,
   pady=10,
   width=100,
   height=100
)
frame = Frame(master=root,width=50,height=60,bg="gray", relief=SUNKEN, borderwidth=5)
method_lbl = Label(
   frame,
   text="Инструменты"
)
frame.pack(side=tk.LEFT, anchor=tk.NE)
method_lbl.grid(row=1, column=1)

frame.place(x=95, y=10)


# Поле с инструментами
tool_frame = tk.Frame(root)
tool_frame.pack(side=tk.LEFT, padx=10, pady=10)


# Кнопки для инструментов
tk.Button(tool_frame, text="Вперёд", command=lambda: add_command("вперёд")).pack(pady=5)
tk.Button(tool_frame, text="Назад ", command=lambda: add_command("назад ")).pack(pady=5)
tk.Button(tool_frame, text="Вправо", command=lambda: add_command("вправо")).pack(pady=5)
tk.Button(tool_frame, text="Влево ", command=lambda: add_command("влево ")).pack(pady=5)

# Поле с блоками команд
command_block = tk.Text(root, height=50, width=50)
command_block.pack(side=tk.LEFT, padx=10, pady=10)


field = tk.Text(root, height=50, width=50)
field.pack(side=tk.LEFT, padx=10, pady=10)
# Кнопка для выполнения команд
execute_button = tk.Button(root, text="Выполнить", command=execute_commands)
execute_button.pack(side=tk.LEFT, padx=10, pady=10)
execute_button.place(x=1000, y=10)



# Размеры поля
GRID_SIZE = 10
CELL_SIZE = 50

# Цвета
WATER_COLOR = "blue"
BUSH_COLOR = "green"
WALL_COLOR = "gray"
TURTLE_COLOR = "yellow"
EXIT_COLOR = "red"
EMPTY_COLOR = "white"

# Начальные координаты черепахи и выхода
turtle_pos = (0, 0)
exit_pos = (GRID_SIZE - 1, GRID_SIZE - 1)

# Инициализация поля
grid = [[EMPTY_COLOR for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
grid[turtle_pos[0]][turtle_pos[1]] = TURTLE_COLOR
grid[exit_pos[0]][exit_pos[1]] = EXIT_COLOR

# Функция для отрисовки поля
def draw_grid(canvas):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x0, y0 = j * CELL_SIZE, i * CELL_SIZE
            x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
            canvas.create_rectangle(x0, y0, x1, y1, fill=grid[i][j], outline="black")

# Функция для перетаскивания стенок
def drag_wall(event):
    x, y = event.x // CELL_SIZE, event.y // CELL_SIZE
    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        if grid[y][x] == EMPTY_COLOR:
            grid[y][x] = WALL_COLOR
            draw_grid(canvas)

# Функция для размещения воды
def place_water(event):
    x, y = event.x // CELL_SIZE, event.y // CELL_SIZE
    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        if grid[y][x] == EMPTY_COLOR:
            grid[y][x] = WATER_COLOR
            draw_grid(canvas)

# Функция для размещения кустов
def place_bush(event):
    x, y = event.x // CELL_SIZE, event.y // CELL_SIZE
    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        if grid[y][x] == EMPTY_COLOR:
            grid[y][x] = BUSH_COLOR
            draw_grid(canvas)

# Функция для перемещения черепахи
def move_turtle(dx, dy):
    global turtle_pos
    x, y = turtle_pos[1] + dx, turtle_pos[0] + dy
    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        if grid[y][x] == EMPTY_COLOR or grid[y][x] == EXIT_COLOR:
            grid[turtle_pos[0]][turtle_pos[1]] = EMPTY_COLOR
            turtle_pos = (y, x)
            grid[y][x] = TURTLE_COLOR
            draw_grid(canvas)
            if turtle_pos == exit_pos:
                messagebox.showinfo("Победа!", "Черепаха нашла выход!")

# Обработка нажатий клавиш
def on_key_press(event):
    if event.keysym == 'Up':
        move_turtle(0, -1)
    elif event.keysym == 'Down':
        move_turtle(0, 1)
    elif event.keysym == 'Left':
        move_turtle(-1, 0)
    elif event.keysym == 'Right':
        move_turtle(1, 0)


# Создание холста
canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
canvas.pack()

# Привязка событий
canvas.bind("<B1-Motion>", drag_wall)
canvas.bind("<Button-2>", place_water)
canvas.bind("<Button-3>", place_bush)
root.bind("<KeyPress>", on_key_press)

# Начальная отрисовка поля
draw_grid(canvas)

# Функция для начала перемещения блока
def start_drag(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

# Функция для перемещения блока
def drag(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

# Функция для завершения перемещения и проверки, попал ли блок в область
def stop_drag(event):
    widget = event.widget
    x = widget.winfo_x()
    y = widget.winfo_y()

    # Проверка, находится ли блок внутри области
    if (drop_zone_x <= x <= drop_zone_x + drop_zone_width and
        drop_zone_y <= y <= drop_zone_y + drop_zone_height):
        print("Блок помещён в область!")
    else:
        print("Блок вне области.")



# Создание области, куда можно поместить блок
drop_zone_x, drop_zone_y = 1400, 600
drop_zone_width, drop_zone_height = 60, 60

drop_zone = tk.Canvas(root, width=drop_zone_width, height=drop_zone_height, bg="lightblue")
drop_zone.place(x=drop_zone_x, y=drop_zone_y)

# Создание перетаскиваемого блока
block = tk.Canvas(root, width=50, height=50, bg="red")
block.place(x=1400, y=600)

# Привязка событий мыши к блоку
block.bind("<Button-1>", start_drag)  # Начало перемещения
block.bind("<B1-Motion>", drag)       # Перемещение
block.bind("<ButtonRelease-1>", stop_drag)  # Завершение перемещения
# Запуск основного цикла
root.mainloop()