package view;

import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import view.panels.ItemListPane;
import view.panels.NewItemPane;

public class MainView {

    private Stage stage = new Stage();

    public MainView(){
        stage.setTitle("MAIN VIEW");
        stage.initStyle(StageStyle.UTILITY);
        stage.setX(660);
        stage.setY(5);
        Group root = new Group();
        Scene scene = new Scene(root, 540, 960);

        // TABPANE
        BorderPane tabView = new BorderPane();
        tabView.prefHeightProperty().bind(scene.heightProperty());
        tabView.prefWidthProperty().bind(scene.widthProperty());
        root.getChildren().add(tabView);

        TabPane tabPane = new TabPane();
        tabView.setCenter(tabPane);

        // ITEMPANES
        tabPane.getTabs().add(new Tab("Item List", new ItemListPane()));
        tabPane.getTabs().add(new Tab("New Item", new NewItemPane()));

        stage.setScene(scene);
        stage.sizeToScene();
        stage.show();
    }
}
