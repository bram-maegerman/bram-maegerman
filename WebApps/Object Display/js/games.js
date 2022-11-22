const mygames = [
    {name: "Call Of Duty", type: "First Person Shooter", rating: 7.9, favourite: false},
    {name: "GTAV", type: "Open World", rating: 9.1, favourite: true},
    {name: "Super Mario Bros", type: "Platformer", rating: 8.3, favourite: false},
    {name: "Forza Hozizon 5", type: "Racing Simulator", rating: 8.5, favourite: true},
    {name: "Gran Turismo", type: "Racing Simulator", rating: 6.9, favourite: false},
    {name: "Elden Ring", type: "Fantasy", rating: 9.3, favourite: false},
    {name: "God Of War", type: "Singleplayer RPG", rating: 9.5, favourite: false},
    {name: "Assetto Corsa", type: "Racing Simulator", rating: 8.6, favourite: true}
]

const friendGames = [
    {name: "Minecraft", type: "Survival", rating: 10, favourite: true},
    {name: "Fortnite", type: "Battle Royale", rating: 6.8, favourite: true}
]

const games = [...mygames, ...friendGames]



// PRINT
const toString = (game) => {
    return `Name: ${game.name} - Type: ${game.type} - Rating: ${game.rating} - Favourite: ${game.favourite ? 'Yes':'No'}`;
}

function printAllGames(games){
    games.map(toString).forEach(addStatus);
}

const printFirstGames = (amount) => {
    addStatus(`<h3>My First ${amount} Games</h3>`)
    for(let i = 0; i < amount; i++){
        addStatus(games[i].name);
    }
}

const printGamesWithRating = (games, rating) => {
    addStatus(`<h3>Games with rating higher then ${rating}</h3>`);
    printAllGames(games.filter(game => game.rating >= rating));
}

const filterAndPrintGames = (games, filter) => {
    printAllGames(games.filter(filter));
}

const printFavouriteGames = (games) => {
    printAllGames(games.filter(game => game.favourite));
}



// STATS
const getAverageRating = (games) => {
    let totalRating = 0;
    for(const game of games){
        totalRating += game.rating;
    }
    return `Average Rating of all the games: ${(totalRating/games.length).toFixed(2)}`;
}

const getHighestRating = (games) => {
    let highestGame = games[0];
    for(const game of games){
        if(game.rating > highestGame.rating){
            highestGame = game;
        }
    }
    return `Highest rating game is ${highestGame.name} with a rating of ${highestGame.rating}`;
}



// SCREEN
addStatus("<h3>My Own Games</h3>");
printAllGames(mygames);

addStatus("<h3>My Friend's Games</h3>");
printAllGames(friendGames)

addStatus("<h3>These are all the games in this library</h3>");
printAllGames(games)

addStatus("<h3>Some Statistics</h3>")
addStatus(getAverageRating(games))
addStatus(getHighestRating(games))

printFirstGames(2)

addStatus("<h3>Favourite games in this library</h3>");
printFavouriteGames(games);

printGamesWithRating(games, 3);

addStatus("<h3>Games with type \"Open World\"</h3>")
filterAndPrintGames(games, (game) => game.type === "Open World")