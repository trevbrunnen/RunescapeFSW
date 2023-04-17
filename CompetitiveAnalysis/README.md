# RunescapeFSW
Analysis of the Runescape 3 Fresh Start Worlds hiscores at the end of the competitive period.

When Jagex announced Fresh Start Worlds last summer, I was very excited since it seemed like RS3 was getting something like Old School’s leagues. It turned out that it wasn’t quite as close to leagues as I had hoped, but I played consistently during the competitive period and had a lot of fun. After FSW closed, I went back to playing my ironman and I thought my time thinking about FSW was over. However, in late January Mod Allstar uploaded a snapshot of the competitive hiscores. I took this as an opportunity to dig though some data and see if there were any interesting insights in the hiscores.
Unfortunately, the Runescape hiscores don’t have any way to query large numbers of players or ranks simultaneously, so I had to scrape the hiscores to get the full data set. Because of rate limits, this took about 4 hours of scraping and some extra time getting everything ready for analysis. I’ve included my code along with the full FSW hiscores dataset in a github repo linked at the bottom of the post. It would be nice for Jagex to improve the hiscores API so it is easier to do large scale analysis of hiscore data.


On to some analysis! The hiscore snapshot contains the top 2,475 players in each skill plus the 2,475 players with the highest total level. There are 16,442 players that were in this snapshot of the hiscores. I had expected that most players that were ranked highly would have multiple skills ranked. I was wrong with this expectation and more than half of players that were ranked only had 1 or 2 ranked skills. On the other side of the distribution, there were only 9 players that were ranked in the top 2,475 for all skills. 
![download](https://user-images.githubusercontent.com/47310990/227351250-5461429d-5f24-46dc-ae44-7283c84a87fc.png)

The most common ranked skill for players that only had 1 skill ranked was Thieving, with 979 players. The next highest was Runecrafting with 796 players. Only 12 people had Invention as their only top 2,475 ranked skill and 25 had Herblore. I’m not surprised by the position of Thieving, Invention, and Herblore since Thieving was easy to train on its own with safes and Invention and Herblore would be more commonly trained by players who had other high scores. I was surprise that Runecrafting was second. My assumption is that Runecrafting was mainly trained by people who were building their account overall and weren’t specifically training Runecrafting. Runecrafting also had the lowest exp need to be in the top 2,475 at 582,151, almost half of the second lowest Archaeology which required 899,447. 

![download](https://user-images.githubusercontent.com/47310990/227351736-39119772-794d-43aa-bc9b-8a72de5ec92c.png)
![download](https://user-images.githubusercontent.com/47310990/227351772-88006a19-af41-40af-92b5-e03fcd3e0b84.png)

Looking at players with exactly 2 skills that were ranked there are some not terribly surprising correlations. The top combination was Mining and Smithing, with 256 players. The other large combinations were Attack/Strength with 132, Fishing/Cooking with 120, and Hunter/Fishing with 102. 
![download](https://user-images.githubusercontent.com/47310990/227351871-2e387b5d-5b6c-46b8-934e-baa8352c049e.png)

I looked briefly for correlations between different skills, and nothing jumped out at a glance. Here is a plot for just the support skills and here is one for all skills. The all skills plot is probably too large to be useful, but I found it at least a little interesting to look through. 
![download](https://user-images.githubusercontent.com/47310990/227351956-5eed65ed-e81b-4dfa-9f02-b7ee5096fd3e.png)


Finally I wanted to look at distributions of who earned halos for placing in the top 100. I haven’t included any of the first to 99, 120, or 200m. There were 2,220 unique players who earned challenger halos. Of those, 1,828 players only earned 1 halo. (This is where I fell in the competition.) There were 7 players that earned 6 halos and 6 players that earned 7 halos. There was 1 player who earned 9 halos. To get those 9 halos, they got 200m experience in Constitution, Attack, Defence, Strength, Ranged, Magic, Thieving, and Hunter and got 102m Firemaking exp. Their only other ranked skill was Fishing. 

![download](https://user-images.githubusercontent.com/47310990/227352346-6f25a9cf-0e7d-4e6b-89bc-0b6191f64e04.png)
