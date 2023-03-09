package view.panels;

import controllers.ItemListController;
import javafx.collections.FXCollections;
import javafx.geometry.Insets;
import javafx.scene.control.ListView;
import javafx.scene.layout.GridPane;
import model.Item;

import java.util.ArrayList;
import java.util.List;


public class ItemListPane extends GridPane{

    private ItemListController itemListController;
    private ListView<String> itemListView = new ListView<>();

    public ItemListPane(){
        this.itemListController = new ItemListController();
        this.itemListController.setView(this);

        this.setPadding(new Insets(20));
        this.setVgap(10);

        itemListView.setPrefSize(520, 900);
        this.add(itemListView, 0, 0);
    }

    public void updateItemList(ArrayList<Item> items){
        this.itemListView.getItems().clear();
        for(Item item: FXCollections.observableArrayList(items)){
            this.itemListView.getItems().add(item.getName() + " - " + item.getCraftingTime() + "s");
        }
    }
}
