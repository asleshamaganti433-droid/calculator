import tkinter as tk
from tkinter import messagebox

# List to store contacts
contacts = []

# Function to update contact list display
def refresh_listbox():
    listbox_contacts.delete(0, tk.END)
    for index, contact in enumerate(contacts):
        listbox_contacts.insert(tk.END, f"{index+1}. {contact['name']} - {contact['phone']}")

# Add new contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    
    if not name or not phone:
        messagebox.showwarning("Error", "Name and phone are required.")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    refresh_listbox()
    clear_inputs()

# Search contact
def search_contact():
    search_term = entry_search.get().strip().lower()
    results = []
    for contact in contacts:
        if search_term in contact["name"].lower() or search_term in contact["phone"]:
            results.append(contact)
    
    if results:
        result_text = "\n".join([f"{c['name']} - {c['phone']}" for c in results])
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No matching contacts found.")

# Delete a selected contact
def delete_contact():
    selected_index = listbox_contacts.curselection()
    if selected_index:
        index = selected_index[0]
        contacts.pop(index)
        refresh_listbox()
    else:
        messagebox.showwarning("Error", "Select a contact to delete.")

# Populate selected contact into input fields for updating
def load_contact_for_update():
    selected_index = listbox_contacts.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact["name"])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact["phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact["email"])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, contact["address"])
    else:
        messagebox.showwarning("Error", "Select a contact to update.")

# Update selected contact
def update_contact():
    selected_index = listbox_contacts.curselection()
    if selected_index:
        index = selected_index[0]
        contacts[index] = {
            "name": entry_name.get().strip(),
            "phone": entry_phone.get().strip(),
            "email": entry_email.get().strip(),
            "address": entry_address.get().strip()
        }
        refresh_listbox()
        clear_inputs()
    else:
        messagebox.showwarning("Error", "Select a contact to update.")

# Clear input fields
def clear_inputs():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_search.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Contact input section
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root, width=50)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root, width=50)
entry_address.pack()

# Buttons for actions
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
tk.Button(root, text="Load Selected for Update", command=load_contact_for_update).pack(pady=5)

# Search section
tk.Label(root, text="Search by Name or Phone").pack()
entry_search = tk.Entry(root, width=50)
entry_search.pack()
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)

# Contact list display
listbox_contacts = tk.Listbox(root, width=70, height=10)
listbox_contacts.pack(pady=10)

root.mainloop()
