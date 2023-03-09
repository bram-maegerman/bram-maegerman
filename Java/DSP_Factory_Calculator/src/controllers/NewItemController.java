package controllers;

import model.ItemEventEnum;
import model.Observer;
import view.panels.NewItemPane;

public class NewItemController extends Controller implements Observer {
    private NewItemPane newItemPane;

    public void setView(NewItemPane newItemPane) {
        this.newItemPane = newItemPane;
    }

    @Override
    public void update(ItemEventEnum event) {

    }
}
