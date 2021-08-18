# -*- coding: utf-8 -*-
import json
import sys
import os
import time
import datetime
from tkinter import ttk
from tkinter import *

class locky:
    def __init__(self, window):
        self.dblocky=json.loads(open('databases/db.json').read())
        self.wind=window
        self.wind.title('Locky')
        #self.wind.geometry('640x480')
        frame=LabelFrame(self.wind, text="New")
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        # imput title
        Label(frame, text='Title').grid(row=1, column=0)
        self.title=Entry(frame)
        self.title.grid(row=1, column=1)
        # imput url
        Label(frame, text='URL').grid(row=2, column=0)
        self.url=Entry(frame)
        self.url.grid(row=2, column=1)
        # imput comment
        Label(frame, text='Comment').grid(row=3, column=0)
        self.comment=Entry(frame)
        self.comment.grid(row=3, column=1)
        # imput user
        Label(frame, text='User').grid(row=4, column=0)
        self.user=Entry(frame)
        self.user.grid(row=4, column=1)
        # imput pass
        Label(frame, text='Password').grid(row=5, column=0)
        self.password=Entry(frame)
        self.password.grid(row=5, column=1)
        # Button
        ttk.Button(frame, text = 'Save', command=self.saveNew).grid(row = 6, columnspan = 2, sticky = W + E)
        # Output Messages
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 6, column = 0, columnspan = 2, sticky = W + E)
        # Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 7, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Title', anchor = CENTER)
        self.tree.heading('#1', text = 'URL', anchor = CENTER)

        # Buttons
        ttk.Button(text = 'OPEN', command=self.openItem).grid(row = 8, column = 0, sticky = W + E)
        ttk.Button(text = 'EDIT', command=self.editItem).grid(row = 8, column = 1, sticky = W + E)
        ttk.Button(text = 'UPDATE LIST', command=self.getItems).grid(row = 9, columnspan = 2, sticky = W + E)
        ttk.Button(text = 'DELETE', command=self.delItem).grid(row = 10, columnspan = 2, sticky = W + E)

        self.getItems()

    def velidator(self):
        return len(self.title.get()) !=0 and len(self.url.get())

    def saveNew(self):
        self.message['text']=''
        dblocky=json.loads(open('databases/db.json').read())
        for item in dblocky:
            if self.title.get() == item:
                self.message['text']="Please ingress another tittle"
                return
        op={
        "url": self.url.get(),
        "comment": self.comment.get(),
        "access":{
        "user": self.user.get(),
        "pass": self.password.get()
        }
        }
        print(op)
        dblocky[self.title.get()]=op
        print(dblocky)
        lockyDump = open('databases/db.json', 'w')
        lockyDump.write(json.dumps(dblocky, indent=4))
        lockyDump.close()
        self.title.delete(0, END)
        self.url.delete(0, END)
        self.comment.delete(0, END)
        self.user.delete(0, END)
        self.password.delete(0, END)
        self.getItems()

    def getItems(self):
        dblocky=json.loads(open('databases/db.json').read())
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        for item in dblocky:
            print(dblocky[item]['url'])
            print(item)
            self.tree.insert('', 0, text = item, values = dblocky[item]['url'])

    def openItem(self):
        dblocky=json.loads(open('databases/db.json').read())
        try:
            titleOpen=self.tree.item(self.tree.selection())['values'][0]
        except:
            self.message['text'] = "Select an item of the list"
            return
        titleOpen=self.tree.item(self.tree.selection())['text']
        self.open_wind = Toplevel()
        self.open_wind.title = 'Description'
        frame=LabelFrame(self.open_wind, text=titleOpen)
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        Label(frame, text = "URL: ").grid(row = 0, column = 1)
        Entry(frame, textvariable = StringVar(frame, value = dblocky[titleOpen]['url'])).grid(row = 0, column = 2)
        Label(frame, text = "User: ").grid(row = 1, column = 1)
        Entry(frame, textvariable = StringVar(frame, value = dblocky[titleOpen]['access']['user'])).grid(row = 1, column = 2)
        Label(frame, text = "Pass: ").grid(row = 2, column = 1)
        Entry(frame, textvariable = StringVar(frame, value = dblocky[titleOpen]['access']['pass'])).grid(row = 2, column = 2)

    def editItem(self):
        dblocky=json.loads(open('databases/db.json').read())
        titleOpen=self.tree.item(self.tree.selection())['text']
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit'
        frameEdit=LabelFrame(self.edit_wind, text=titleOpen)
        frameEdit.grid(row=0, column=0, columnspan=3, pady=20)
        url="URL: "+dblocky[titleOpen]['url']
        Label(frameEdit, text = url).grid(row = 0, column = 1)
        self.editURL=Entry(frameEdit)
        self.editURL.grid(row=1, column=1)
        comment="Comment: "+dblocky[titleOpen]['comment']
        Label(frameEdit, text = comment).grid(row = 2, column = 1)
        self.editComment=Entry(frameEdit)
        self.editComment.grid(row=3, column=1)
        user="User: "+dblocky[titleOpen]['access']['user']
        Label(frameEdit, text = user).grid(row = 4, column = 1)
        self.editUser=Entry(frameEdit)
        self.editUser.grid(row=5, column=1)
        password="Pass: "+dblocky[titleOpen]['access']['pass']
        Label(frameEdit, text = password).grid(row = 6, column = 1)
        self.editPassword=Entry(frameEdit)
        self.editPassword.grid(row=7, column=1)
        ttk.Button(frameEdit, text = 'Save', command=lambda: self.recordItem(titleOpen, self.editURL.get(), self.editComment.get(), self.editUser.get(), self.editPassword.get())).grid(row = 8, columnspan = 2, sticky = W + E)
        # Output Messages
        self.messageEdit = Label(frameEdit, text = '', fg = 'red')
        self.messageEdit.grid(row = 9, column = 0, columnspan = 2, sticky = W + E)
        print(titleOpen)
        self.edit_wind.mainloop()

    def recordItem(self, tittle, url, comment, user, password):
        # check items
        if len(url)==0 or len(comment)==0 or len(user)==0 or len(password)==0:
            self.messageEdit['text']="Please complete all items"
            return
        # backup db
        backup_db='db_.json.bk'
        lockyBackup = open(backup_db, 'w')
        lockyBackup.write(json.dumps(json.loads(open('databases/db.json').read()), indent=4))
        lockyBackup.close()
        print(tittle)
        tittleRecord={"url": url,
                    "comment": comment,
                    "access":{
                            "user": user,
                            "pass": password
                    }}
        print(tittle)
        dblocky=json.loads(open('databases/db.json').read())
        dblocky[tittle]=tittleRecord
        print(dblocky)
        lockyDump = open('databases/db.json', 'w')
        lockyDump.write(json.dumps(dblocky, indent=4))
        lockyDump.close()
        self.getItems()

    def delItem(self):
        updateDB = {}
        try:
            titleOpen=self.tree.item(self.tree.selection())['values'][0]
        except:
            self.message['text'] = "Select an item of the list"
            return
        # backup db
        backup_db='db_.json.bk'
        lockyBackup = open(backup_db, 'w')
        lockyBackup.write(json.dumps(self.dblocky, indent=4))
        lockyBackup.close()
        delTittle=self.tree.item(self.tree.selection())['text']
        for item in json.loads(open('databases/db.json').read()):
            if item!=delTittle:
                updateDB[item]=json.loads(open('databases/db.json').read())[item]
        print(updateDB)
        lockyDump = open('databases/db.json', 'w')
        lockyDump.write(json.dumps(updateDB, indent=4))
        lockyDump.close()
        self.getItems()

if __name__ == '__main__':
    window=Tk()
    application=locky(window)
    window.mainloop()
