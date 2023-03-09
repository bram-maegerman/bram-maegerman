package controllers;

import model.ItemEventEnum;
import model.Observer;
import view.panels.ItemListPane;

public class ItemListController extends Controller implements Observer {
    private ItemListPane itemListPane;

    public void setView(ItemListPane itemListPane) {
        this.itemListPane = itemListPane;
        this.itemListPane.updateItemList(getItemFacade().getItems());
    }

    @Override
    public void update(ItemEventEnum event) {
        switch(event){
            case UPDATE_ITEMS:
                itemListPane.updateItemList(getItemFacade().getItems());
        }
    }
}
