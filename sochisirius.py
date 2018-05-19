import networkx as nx #подключаем библиотеку, работующую с графами
import matplotlib.pyplot as plt #подключаем библиотеку, отрисовывающую графы из networkx
import tkinter as tk #подключаем библиотеку для графического интерфейса
from PIL import Image, ImageTk #подключаем библиотеку для взаимодействия м/у графическим интерфейсом и графами


G=nx.Graph()#наш граф, с которым мы будем работать
image=Image.open('graph.png')

master=tk.Tk()#основное окно для самой плоскости, графа, кнопок
master.title('Graph Visualiser v 0.1')#заголовок для окна master

def img_to_master():#функция для вставки картинки в окно master
    global image
    image = Image.open('graph.png')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(image=photo)
    label.image = photo
    label.place(x=0, y=75)

def draw_graph():#функция для отрисовки графа
    global G
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.gcf().set_size_inches(20, 9.4)
    plt.savefig('graph.png')
    plt.close()
    img_to_master()

def make_full_graph(amount_of_vertex):#функция для кнопки "Полный граф"
    global G
    G = nx.Graph()
    list_of_nodes=[i for i in range(1, amount_of_vertex+1)]
    G.add_nodes_from(list_of_nodes)
    lis_of_edges=[]
    for i in range(1, amount_of_vertex+1):
        for j in range(1, amount_of_vertex+1):
            if i==j:
                continue
            else:
                buffer=(i,j)
                if buffer not in lis_of_edges:
                    G.add_edge(*buffer)
                    lis_of_edges.append(buffer)
                else:
                    continue
    draw_graph()

def add_vertex():#функция для кнопки "Добавить одну вершину"
    global G
    G.add_node(len(list(G.nodes))+1)
    draw_graph()

def add_vertexes(num):#Функция дня кнопки "Добавить несколько вершин"
    global G
    start=len(list(G.nodes))+1
    end=start+num
    for i in range(start, end):
        G.add_node(i)
    draw_graph()

def is_hamiltonian():#функция определяющая Гамильтонов ли граф
    global G
    if nx.is_connected(G):
        if len(list(G.nodes))<=3:
            return True
        if len(list(G.nodes))/2>=len(list(G.nodes))//2:
            half=len(list(G.nodes))//2+1
        else:
            half=len(list(G.nodes))//2
        if min(list(G.degree))>half:
            return True
        return False
    return False

def rebuild():#функция кнопки "обновления" внешнего вида графа
    draw_graph()

def full_graph_button():#функция для кнопки для построения полного графа
    window=tk.Tk()
    window.title('Настройки для полного графа')
    window.geometry("133x120")

    labelfull = tk.Label(window, text="Введите кол-во вершин \n полного графа:", fg="#eee", bg="#333")
    labelfull.pack()

    msg=tk.StringVar()
    entry=tk.Entry(window, textvariable=msg)
    entry.place(relx=.5, rely=.7, anchor="c")

    button_send_data_to_full=tk.Button(window, text='Построить граф', command=lambda : make_full_graph(int(str(entry.get()))))
    button_send_data_to_full.pack()

    window.mainloop()

img_to_master()

img_full_graph=ImageTk.PhotoImage(file="1img.png")#кнопка для построения полного графа
button_full_graph=tk.Button(master, image=img_full_graph, command=lambda : full_graph_button())
button_full_graph.pack()

img_n_vertex_add=ImageTk.PhotoImage(file="2img.png")#кнопка для добавления n вершин
button_n_vertex=tk.Button(master, image=img_n_vertex_add, command=lambda : add_vertexes(5))
button_n_vertex.pack()

master.mainloop()#после закрытия окна ничего не происходит