package model.loadSave;

import model.Item;

import java.io.*;
import java.nio.Buffer;
import java.util.ArrayList;

public class ItemsLoadSave {
    public ArrayList<Item> load() {
        ArrayList<Item> returnList = new ArrayList<>();

        try(BufferedReader reader = new BufferedReader(new FileReader("src/files/items.txt"))){
            String line = reader.readLine();
            while(line != null && !line.trim().equals("")){
                String[] tokens = line.split(";");
                Item item = new Item(tokens[0], Integer.parseInt(tokens[1]));
                for(int i = 2; i < tokens.length; i++){
                    String[] recipeItem = tokens[i].split("/");
                    item.addRecipeItem(recipeItem[0], Integer.parseInt(recipeItem[1]));
                }
                returnList.add(item);
                line = reader.readLine();
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }

        return returnList;
    }

    public void save(ArrayList<Item> saveList) {
        try(BufferedWriter writer = new BufferedWriter(new FileWriter("src/files/items.txt"))) {
            for(Item item: saveList){
                writer.write(item.getName() + ";" + item.getCraftingTime() + item.getRecipeItemsString());
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
