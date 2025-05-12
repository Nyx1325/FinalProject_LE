# PROJECT TITLE
**Rev Up!**
## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <https://github.com/Nyx1325/FinalProject_LE.git>

## Description
**Rev Up!** is a game inspired by the iconic Tron arcade game *Lightcycle*. Set in a modern parking lot, the player and CPU are red and green motorcycles respectively. During the game, players will have to move around randomly generated cars along with trying to avoid or trap the CPU within their smoke trail while the CPU will be doing the same. 

Besides having my source code, I have images that I created of the elements of the game. I have 3 PNGs of cars, an orange, a blue, and a purple. I also have PNGs of motorcycles where the red motorcycle is the player’s motorcycle, and the green motorcycle is the CPU or opponent. Along with those I also have a JPEG of the background or in this case the parking lot. In my requirements.txt, the game needs pygame and random to help with the overall development of the game and to help randomize the opponent's movement and car spawning. 

Overall, I wanted to have the graphics in a 320 x 240 resolution similar to the old arcade games. While coding, I noticed that the window itself was a bit too small, so I decided to make sure to scale everything by 2 but keeping the same pixel look so that it still gives that retro aesthetic but is more visible on computers or modern displays. In making the PNGs and JPEG, I drew them out with that resolution from inspiration of other top view angled images of cars, motorcycles, and parking lots. I also tried to make the particle trail for the motorcycles to be smoke-like by having the particles circular and contain different opacities along with respective colors to differentiate between the player and CPU’s smoke trails. For the reset button, I chose to have it more rounded to separate it from the end game titles rather than having just “Restart” below to make it more visible for players.

In terms of the design elements, the one thing about the background is that it is basic. To improve it, I would like to have more elements to make it seem realistic in terms of just the design of the parking lot. For example, adding trash or things like greenery just to have it be as realistic as a pixel art can be. 
For the mechanics itself, I had various challenges but there was only one that I could not seem to figure out. I would love to find a way and have the collision aspect more centered around car images so that the motorcycles wouldn't get stuck so easily or hit and bounce off walls that aren't there.
The start of the game is to my liking, where the CPU immediately starts going for the player despite the player may have not started moving. I kept this so that it would be more thrilling as it gives no time and relies on the player's quick reaction. However, I understand that for other people it would probably be better to have a title card or something to indicate that this game is about to start to allow the player to be ready. For that I think I would add a button or a title card and make sure that once the player starts movement that is when the CPU starts trying to get the player.
