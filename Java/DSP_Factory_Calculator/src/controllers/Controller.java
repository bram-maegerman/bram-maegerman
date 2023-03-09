package controllers;

import model.ItemFacade;

public class Controller {
    private ItemFacade itemFacade;

    public Controller(){
        this.itemFacade = ItemFacade.getInstance();
    }

    public ItemFacade getItemFacade(){
        return this.itemFacade;
    }
}
