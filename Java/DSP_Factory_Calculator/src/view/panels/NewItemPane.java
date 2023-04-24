package view.panels;

import controllers.ItemListController;
import controllers.NewItemController;
import javafx.geometry.Insets;
import javafx.scene.layout.GridPane;

public class NewItemPane extends GridPane {

    private NewItemController newItemController;

    public NewItemPane(){
        this.newItemController = new NewItemController();
        this.newItemController.setView(this);

        this.setPadding(new Insets(20));
        this.setVgap(10);
    }
}
