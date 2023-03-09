package model;

import java.util.ArrayList;
import java.util.List;

public class Item {
    private String name;
    private double craftingTime;
    private List<String> recipeItems = new ArrayList<>();
    private List<Integer> recipeItemsAmounts = new ArrayList<>();

    public Item(String name, double craftingTime){
        this.name = name;
        this.craftingTime = craftingTime;
    }

    public void addRecipeItem(String name, int amount){
        this.recipeItems.add(name);
        this.recipeItemsAmounts.add(amount);
    }

    public String getName(){
        return this.name;
    }

    public double getCraftingTime() {
        return craftingTime;
    }

    public String getRecipeItemsString() {
        String returnString = "";
        for(int i = 0; i < recipeItems.size(); i++){
            returnString += ";" + recipeItems.get(i) + "/" + recipeItemsAmounts.get(i);
        }
        return returnString;
    }
}
