package model;

import java.util.ArrayList;
import java.util.List;

public class Item {
    private String name;
    private List<String> recipeItems = new ArrayList<>();
    private List<Integer> recipeItemsAmounts = new ArrayList<>();
    private double craftingTime;

    public Item(String name, double craftingTime){
        this.name = name;
        this.craftingTime = craftingTime;
    }

    public void addRecipeItem(String item){
        this.recipeItems.add(item);
    }
}
