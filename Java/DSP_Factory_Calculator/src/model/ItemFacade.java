package model;

import java.util.ArrayList;
import java.util.List;

public class ItemFacade {

    private static ItemFacade itemFacade;
    private ItemDB itemDB;
    private List<Observer> observers = new ArrayList<>();

    public static ItemFacade getInstance(){
        if(itemFacade == null){
            itemFacade = new ItemFacade();
        }
        return itemFacade;
    }

    public ItemFacade(){
        this.itemDB = ItemDB.getInstance();
    }

    public ArrayList<Item> getItems(){
        return itemDB.getItems();
    }

    public void updateItemList(){
        notifyObservers(ItemEventEnum.UPDATE_ITEMS);
    }


    // OBSERVERS
    public void addObserver(Observer o){
        this.observers.add(o);
    }

    public void notifyObservers(ItemEventEnum event){
        observers.forEach(o -> o.update(event));
    }
}
