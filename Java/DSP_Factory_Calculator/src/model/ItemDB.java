package model;

import model.loadSave.ItemsLoadSave;

import java.util.ArrayList;

public class ItemDB {
    private static ItemDB itemDB;
    private ArrayList<Item> items = new ArrayList<>();
    private ItemsLoadSave itemsLoadSave= new ItemsLoadSave();

    public static ItemDB getInstance(){
        if(itemDB == null){
            itemDB = new ItemDB();
        }
        return itemDB;
    }

    public ItemDB(){
        this.items = itemsLoadSave.load();
        System.out.println(items.get(0).getName());
    }

    public ArrayList<Item> getItems(){
        return this.items;
    }
}
