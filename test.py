

import tkinter as tk
string = 'sabujowma;jvlnk sopdinkfiog spifnkf;asjdfdposj;' \
         'flmdfoasljnfklddubsfdnkl;fsdfssa dkbjnlkmdmsfff' \
         'fffffffffffffffffffffffffffffffffffffffffikmiokd' \
         'msdnkf moisjbfens asce asia dface feetle de ce nu vi' \
         'ne la petrecere ce furmoasa este madalia doame,me ce' \
         ' ,a bucur ca a pputut sa o sarut pe obraz , macar atata' \
         ' in 4 ani de zile'

root = tk.Tk()
string = tk.StringVar()
root.geometry('300x300')
label = tk.Label(root, textvariable=string.get()).pack()
string.set(string)
root.mainloop()
