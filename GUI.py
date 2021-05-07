import tkinter as tk

from Deletes import delete
from Inserts import insertArt, insertArtist, insertGallery, insertCustomer, insertAuction, insertReciept
from Selects import selecting
from Updates import update


class Table:

    def __init__(self, root, total_rows, total_columns, lst):

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = tk.Entry(root, width=40, fg='blue', font=('Arial', 8, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, lst[i][j])


def insert_art():
    art_form = tk.Toplevel(window)
    art_form.title("INSERTING INTO ART TABLE")
    frm_form = tk.Frame(master=art_form, relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack()

    lbl_name = tk.Label(master=frm_form, text="Name:")
    ent_name = tk.Entry(master=frm_form, width=50)
    lbl_name.grid(row=0, column=0, sticky="e")
    ent_name.grid(row=0, column=1)

    lbl_desc = tk.Label(master=frm_form, text="Description:")
    ent_desc = tk.Entry(master=frm_form, width=50)
    lbl_desc.grid(row=1, column=0, sticky="e")
    ent_desc.grid(row=1, column=1)

    lbl_cat = tk.Label(master=frm_form, text="Category:")
    ent_cat = tk.Entry(master=frm_form, width=50)
    lbl_cat.grid(row=2, column=0, sticky="e")
    ent_cat.grid(row=2, column=1)

    lbl_artist = tk.Label(master=frm_form, text="Artist:")
    ent_artist = tk.Entry(master=frm_form, width=50)
    lbl_artist.grid(row=3, column=0, sticky="e")
    ent_artist.grid(row=3, column=1)

    lbl_gallery = tk.Label(master=frm_form, text="Gallery:")
    ent_gallery = tk.Entry(master=frm_form, width=50)
    lbl_gallery.grid(row=4, column=0, sticky="e")
    ent_gallery.grid(row=4, column=1)

    lbl_price = tk.Label(master=frm_form, text="Price:")
    ent_price = tk.Entry(master=frm_form, width=50)
    lbl_price.grid(row=5, column=0, sticky="e")
    ent_price.grid(row=5, column=1)

    frm_buttons = tk.Frame(master=art_form)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        name = ent_name.get()
        desc = ent_desc.get()
        cat = ent_cat.get()
        artist = ent_artist.get()
        gallery = ent_gallery.get()
        price = ent_price.get()
        insertArt(name, desc, cat, artist, gallery, price)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def insert_artist():
    art_form = tk.Toplevel(window)
    art_form.title("INSERTING INTO ARTIST TABLE")
    frm_form = tk.Frame(master=art_form, relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack()

    lbl_name = tk.Label(master=frm_form, text="Name:")
    ent_name = tk.Entry(master=frm_form, width=50)
    lbl_name.grid(row=0, column=0, sticky="e")
    ent_name.grid(row=0, column=1)

    lbl_lastname = tk.Label(master=frm_form, text="Lastname:")
    ent_lastname = tk.Entry(master=frm_form, width=50)
    lbl_lastname.grid(row=1, column=0, sticky="e")
    ent_lastname.grid(row=1, column=1)

    lbl_id = tk.Label(master=frm_form, text="National_ID:")
    ent_id = tk.Entry(master=frm_form, width=50)
    lbl_id.grid(row=2, column=0, sticky="e")
    ent_id.grid(row=2, column=1)

    lbl_no = tk.Label(master=frm_form, text="Phone_Number:")
    ent_no = tk.Entry(master=frm_form, width=50)
    lbl_no.grid(row=3, column=0, sticky="e")
    ent_no.grid(row=3, column=1)

    lbl_age = tk.Label(master=frm_form, text="Age:")
    ent_age = tk.Entry(master=frm_form, width=50)
    lbl_age.grid(row=4, column=0, sticky="e")
    ent_age.grid(row=4, column=1)

    frm_buttons = tk.Frame(master=art_form)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        name = ent_name.get()
        lastname = ent_lastname.get()
        id = ent_id.get()
        number = ent_no.get()
        age = ent_age.get()
        insertArtist(name, lastname, id, number, age)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def insert_gallery():
    art_form = tk.Toplevel(window)
    art_form.title("INSERTING INTO GALLERY TABLE")
    frm_form = tk.Frame(master=art_form, relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack()

    lbl_name = tk.Label(master=frm_form, text="Name:")
    ent_name = tk.Entry(master=frm_form, width=50)
    lbl_name.grid(row=0, column=0, sticky="e")
    ent_name.grid(row=0, column=1)

    lbl_od = tk.Label(master=frm_form, text="Opening_Date:")
    ent_od = tk.Entry(master=frm_form, width=50)
    lbl_od.grid(row=1, column=0, sticky="e")
    ent_od.grid(row=1, column=1)

    lbl_cd = tk.Label(master=frm_form, text="Closing_Date:")
    ent_cd = tk.Entry(master=frm_form, width=50)
    lbl_cd.grid(row=2, column=0, sticky="e")
    ent_cd.grid(row=2, column=1)

    frm_buttons = tk.Frame(master=art_form)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        name = ent_name.get()
        open = ent_od.get()
        close = ent_cd.get()
        insertGallery(name, open, close)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def insert_customer():
    art_form = tk.Toplevel(window)
    art_form.title("INSERTING INTO CUSTOMER TABLE")
    frm_form = tk.Frame(master=art_form, relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack()

    lbl_name = tk.Label(master=frm_form, text="Name:")
    ent_name = tk.Entry(master=frm_form, width=50)
    lbl_name.grid(row=0, column=0, sticky="e")
    ent_name.grid(row=0, column=1)

    lbl_lastname = tk.Label(master=frm_form, text="Lastname:")
    ent_lastname = tk.Entry(master=frm_form, width=50)
    lbl_lastname.grid(row=1, column=0, sticky="e")
    ent_lastname.grid(row=1, column=1)

    lbl_no = tk.Label(master=frm_form, text="Phone_Number:")
    ent_no = tk.Entry(master=frm_form, width=50)
    lbl_no.grid(row=2, column=0, sticky="e")
    ent_no.grid(row=2, column=1)

    frm_buttons = tk.Frame(master=art_form)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        name = ent_name.get()
        lastname = ent_lastname.get()
        number = ent_no.get()
        insertCustomer(name, lastname, number)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def insert_auction():
    art_form = tk.Toplevel(window)
    art_form.title("INSERTING INTO ART TABLE")
    frm_form = tk.Frame(master=art_form, relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack()

    lbl_date = tk.Label(master=frm_form, text="Date:")
    ent_date = tk.Entry(master=frm_form, width=50)
    lbl_date.grid(row=0, column=0, sticky="e")
    ent_date.grid(row=0, column=1)

    lbl_gal = tk.Label(master=frm_form, text="Gallery:")
    ent_gal = tk.Entry(master=frm_form, width=50)
    lbl_gal.grid(row=1, column=0, sticky="e")
    ent_gal.grid(row=1, column=1)

    frm_buttons = tk.Frame(master=art_form)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        date = ent_date.get()
        gallery = ent_gal.get()
        insertAuction(date, gallery)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def insert_reciept():
    art_form = tk.Toplevel(window)
    art_form.title("INSERTING INTO ART TABLE")
    frm_form = tk.Frame(master=art_form, relief=tk.SUNKEN, borderwidth=3)
    frm_form.pack()

    lbl_customer = tk.Label(master=frm_form, text="Customer(Phone_Number):")
    ent_customer = tk.Entry(master=frm_form, width=50)
    lbl_customer.grid(row=0, column=0, sticky="e")
    ent_customer.grid(row=0, column=1)

    lbl_artist = tk.Label(master=frm_form, text="Artist(National_ID):")
    ent_artist = tk.Entry(master=frm_form, width=50)
    lbl_artist.grid(row=1, column=0, sticky="e")
    ent_artist.grid(row=1, column=1)

    lbl_auction = tk.Label(master=frm_form, text="Auction(ID):")
    ent_auction = tk.Entry(master=frm_form, width=50)
    lbl_auction.grid(row=2, column=0, sticky="e")
    ent_auction.grid(row=2, column=1)

    lbl_sug_p = tk.Label(master=frm_form, text="Suggested Price:")
    ent_sug_p = tk.Entry(master=frm_form, width=50)
    lbl_sug_p.grid(row=3, column=0, sticky="e")
    ent_sug_p.grid(row=3, column=1)

    frm_buttons = tk.Frame(master=art_form)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        customer = ent_customer.get()
        artist = ent_artist.get()
        auction = ent_auction.get()
        suggested_price = ent_sug_p.get()
        insertReciept(customer, artist, auction, suggested_price)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def insert_window():
    new_window = tk.Toplevel(window)
    question = tk.Label(
        master=new_window,
        text="WHICH TABLE DO YOU WISH TO INSERT DATA IN?",
        fg="SpringGreen4",
        width=50,
        height=1
    )
    question.pack()

    table_buttons = tk.Frame(master=new_window)
    table_buttons.pack(fill=tk.BOTH, expand=True)

    art = tk.Button(
        master=table_buttons,
        text="Art",
        fg="gray1",
        bg="DarkOliveGreen1",
        width=10,
        command=insert_art
    )
    art.pack()

    artist = tk.Button(
        master=table_buttons,
        text="Artist",
        fg="gray1",
        bg="DarkOliveGreen1",
        width=10,
        command=insert_artist
    )
    artist.pack()

    gallery = tk.Button(
        master=table_buttons,
        text="Gallery",
        fg="gray1",
        bg="DarkOliveGreen1",
        width=10,
        command=insert_gallery
    )
    gallery.pack()

    customer = tk.Button(
        master=table_buttons,
        text="Customer",
        fg="gray1",
        bg="DarkOliveGreen1",
        width=10,
        command=insert_customer
    )
    customer.pack()

    auction = tk.Button(
        master=table_buttons,
        text="Auction",
        fg="gray1",
        bg="DarkOliveGreen1",
        width=10,
        command=insert_auction
    )
    auction.pack()

    reciept = tk.Button(
        master=table_buttons,
        text="Reciept",
        fg="gray1",
        bg="DarkOliveGreen1",
        width=10,
        command=insert_reciept
    )
    reciept.pack()


def delete_window():
    new_window = tk.Toplevel(window)
    instruction = tk.Label(
        master=new_window,
        text="WRITE YOUR DELETE QUERY!",
        fg="SpringGreen4",
        width=50,
        height=2
    )
    instruction.pack()

    delete_query = tk.Text(master=new_window)
    delete_query.pack()

    frm_buttons = tk.Frame(master=new_window)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        query = delete_query.get(1.0, tk.END)
        delete(query)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def update_window():
    new_window = tk.Toplevel(window)
    instruction = tk.Label(
        master=new_window,
        text="WRITE YOUR UPDATE QUERY!",
        fg="SpringGreen4",
        width=50,
        height=2
    )
    instruction.pack()

    update_query = tk.Text(master=new_window)
    update_query.pack()

    frm_buttons = tk.Frame(master=new_window)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        query = update_query.get(1.0, tk.END)
        update(query)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


def show_window():
    new_window = tk.Toplevel(window)
    instruction = tk.Label(
        master=new_window,
        text="WRITE YOUR SELECT QUERY!",
        fg="SpringGreen4",
        width=50,
        height=2
    )
    instruction.pack()

    show_query = tk.Text(master=new_window)
    show_query.pack()

    frm_buttons = tk.Frame(master=new_window)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    def do_it():
        query = show_query.get(1.0, tk.END)
        items = selecting(query)

        rows = len(items)
        cols = len(items[0])
        second_window = tk.Toplevel(new_window)
        t = Table(second_window, rows, cols, items)

    btn_submit = tk.Button(master=frm_buttons, text="Submit", command=do_it)
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


window = tk.Tk()
window.title("Picto Gallery Datatbase")

greeting_frame = tk.Frame(master=window)
greeting_frame.pack(fill=tk.BOTH, expand=True)
greeting = tk.Label(
    master=greeting_frame,
    text="WELCOME TO PICTO GALLERY DATABASE!",
    fg="maroon",
    width=50,
    height=1,
)
greeting.pack()

select_frame = tk.Frame(master=window)
select_frame.pack(fill=tk.BOTH, expand=True)

select = tk.Label(
    master=select_frame,
    text="Select what you wish to do:"
)
select.pack()

buttons_frame = tk.Frame(master=window)
buttons_frame.pack(fill=tk.BOTH, expand=True)

insert_button = tk.Button(
    master=buttons_frame,
    text="Insert data",
    fg="yellow",
    bg="light slate blue",
    width=10,
    height=2,
    command=insert_window
)
insert_button.pack()

delete_button = tk.Button(
    master=buttons_frame,
    text="Delete data",
    fg="yellow",
    bg="light slate blue",
    width=10,
    height=2,
    command=delete_window
)
delete_button.pack()

update_button = tk.Button(
    master=buttons_frame,
    text="Update data",
    fg="yellow",
    bg="light slate blue",
    width=10,
    height=2,
    command=update_window
)
update_button.pack()

show_button = tk.Button(
    master=buttons_frame,
    text="Show data",
    fg="yellow",
    bg="light slate blue",
    width=10,
    height=2,
    command=show_window
)
show_button.pack()

window.mainloop()
