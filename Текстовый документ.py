import tkinter as tk
from tkinter import messagebox
from tkinter import *
import turtle
import tkinter.ttk as ttk
from PIL import Image, ImageTk

# Создание основного окна
root = tk.Tk()
root.title("Проект")
root.geometry("1920x1080")

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

# Функция для завершения перемещения и проверки, попал ли блок в зону
def stop_drag(event):
    widget = event.widget
    x = widget.winfo_x()
    y = widget.winfo_y()

    # Проверка, находится ли блок внутри зоны
    if (drop_zone_x <= x <= drop_zone_x + drop_zone_width and
        drop_zone_y <= y <= drop_zone_y + drop_zone_height):
        # Перемещаем блок в центр зоны
        widget.place(x=drop_zone_x + (drop_zone_width - widget.winfo_width()) // 2,
                     y=drop_zone_y + (drop_zone_height - widget.winfo_height()) // 2)
        
        # Создаём новый блок на месте старого
        create_new_block(widget.startX, widget.startY)

# Функция для создания нового блока
def create_new_block(x, y):
    global block_counter
    block_counter += 1
    text = str(block_counter)
    block = tk.Label(root, text=text, bg="Blue", padx=20, pady=10)
    block.place(x=x, y=y)
    block.bind("<Button-1>", start_drag)  # Начало перемещения
    block.bind("<B1-Motion>", drag)       # Перемещение
    block.bind("<ButtonRelease-1>", stop_drag)  # Завершение перемещения


# Создание зоны, куда можно поместить блоки
drop_zone_x, drop_zone_y = 1000, 400
drop_zone_width, drop_zone_height = 200, 100

drop_zone = tk.Canvas(root, width=drop_zone_width, height=drop_zone_height, bg="lightblue")
drop_zone.place(x=drop_zone_x, y=drop_zone_y)

# Создание начальных блоков
block_counter = 3  # Счётчик для создания новых блоков
blocks = ["Вперед", "Назад", "Вправо","Влево"]

for i, text in enumerate(blocks):
    block = tk.Label(root, text=text, bg="Blue", padx=20, pady=10)
    block.place(x=50 + i * 100, y=50)
    block.bind("<Button-1>", start_drag)  # Начало перемещения
    block.bind("<B1-Motion>", drag)       # Перемещение
    block.bind("<ButtonRelease-1>", stop_drag)  # Завершение перемещения


text_tools = Frame(root,padx=10,pady=10)
text_tools = Frame(master=root, relief=SUNKEN, borderwidth=0)
method_lbl = Label(text_tools,text="Инструменты",font=("Arial", 20))
text_tools.pack(side=tk.LEFT, anchor=tk.NE)
method_lbl.grid(row=1, column=1)
text_tools.place(x=95, y=10)


# Поле с инструментами
tool_frame = tk.Frame(root)
tool_frame.pack(side=tk.LEFT, padx=10, pady=10)



# Кнопка для выполнения команд
def next_image():
    global current_image_index, label, green_button, blue_button

    # Увеличиваем индекс текущего изображения
    current_image_index += 1

    # Обновляем изображение на экране
    label.config(image=images[current_image_index])

    # Делаем кнопку "Предыдущее изображение" активной
    blue_button.config(state=tk.NORMAL)

    # Если достигнуто последнее изображение, делаем кнопку "Следующее изображение" неактивной
    if current_image_index == len(images) - 1:
        green_button.config(state=tk.DISABLED)

# Функция для возврата к предыдущему изображению
def previous_image():
    global current_image_index, label, green_button, blue_button

    # Уменьшаем индекс текущего изображения
    current_image_index -= 1

    # Обновляем изображение на экране
    label.config(image=images[current_image_index])

    # Делаем кнопку "Следующее изображение" активной
    green_button.config(state=tk.NORMAL)

    # Если достигнуто первое изображение, делаем кнопку "Предыдущее изображение" неактивной
    if current_image_index == 0:
        blue_button.config(state=tk.DISABLED)


# Загрузка изображений
image_paths = ["C:\\Users\\ИВАН\\Desktop\\menu.png","C:\\Users\\ИВАН\\Desktop\\menu2.png"]  # Укажите пути к вашим изображениям
images = []

for path in image_paths:
    img = Image.open(path)  # Открываем изображение с помощью PIL
    img = img.resize((700,900), Image.ANTIALIAS)  # Масштабируем изображение
    img_tk = ImageTk.PhotoImage(img)  # Конвертируем в формат, поддерживаемый tkinter
    images.append(img_tk)

def move_button1():
    # Новые координаты (x, y)
    new_x = 50
    new_y = 100
    blue_button.place(x=new_x, y=new_y)  # Перемещаем кнопку
    new_x1 = 10
    new_y1 = 250
    green_button.place(x=new_x1,y=new_y1)
# Индекс текущего изображения
current_image_index = 0
second_button = Image.open("C:\\Users\\ИВАН\\Desktop\\greeencircle.png")  # Укажите путь к вашему изображению
greencircle = ImageTk.PhotoImage(second_button)
# Создание метки для отображения изображения
label = tk.Label(root, image=images[current_image_index])
label.pack(pady=10)
label.place(x=10,y=100)
# Создание кнопки для перехода к следующему изображению

def move_button():
    # Новые координаты (x, y)
    new_x = 10
    new_y = 350
    blue_button.place(x=new_x, y=new_y)  # Перемещаем кнопку
    new_x1 = 50
    new_y1 = 100
    green_button.place(x=new_x1,y=new_y1)


green_button = tk.Button(root, image=greencircle, command=lambda:(next_image(), move_button()))
green_button.pack(side=tk.RIGHT, padx=10, pady=10)
green_button.place(x=10, y=250)
green_button["bg"] = root["bg"]
first_button = Image.open("C:\\Users\\ИВАН\Desktop\\bluecircle.png")  # Укажите путь к вашему изображению
bluecircle = ImageTk.PhotoImage(first_button)

# Создание кнопки для возврата к предыдущему изображению
blue_button = tk.Button(root, image=bluecircle, command=lambda:(previous_image(), move_button1()), state=tk.DISABLED)
blue_button.pack(side=tk.LEFT, padx=10, pady=10)
blue_button.place(x=50,y=100)
blue_button["bg"] = root["bg"]

width_length_label = tk.Label(root, text="Ширина и Высота:")
width_length_label.pack(pady=5)
width_length_entry = tk.Entry(root)
width_length_entry.pack(pady=5)
size_label = tk.Label(root, text="Размер клеток:")
size_label.pack(pady=5)
size_entry = tk.Entry(root)
size_entry.pack(pady=5)
# Размеры поля
GRID_SIZE = width_length_entry.get()
CELL_SIZE = size_entry.get()

GRID_SIZE = 5
CELL_SIZE = 5

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
canvas.place(x=1400,y=200)

create_button = tk.Button(root, text="Создать Canvas", command=canvas)
create_button.pack(pady=10)
create_button.place(x=1200,y=200)

# Привязка событий
canvas.bind("<B1-Motion>", drag_wall)
canvas.bind("<Button-2>", place_water)
canvas.bind("<Button-3>", place_bush)
root.bind("<KeyPress>", on_key_press)

# Начальная отрисовка поля
draw_grid(canvas)

root.mainloop()
