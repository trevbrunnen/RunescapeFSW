After my last post about Fresh Start Worlds, I got curious about how successful FSW was. My initial assumption was that most players would be like me--a long-time player who made an alt account to take advantage of boosted experience rates to earn cosmetic rewards, but then abandon the account at the end of the game mode. Because this assumption takes that the player base would be vastly different than the player base Jagex had said they were targeting, I would count FSW as a success if more than 5% of players that made an account continued playing after the conclusion of FSW.

## Summary

There were 58,089 players on the FSW hiscores. Of these players 8,529 had gained more than 1,000,000 experience since the conclusion of FSW and the top 5% (2,901) players had gained more than 28,000,000 experience. If you look at the ratio of experience players gained after FSW to the experience they gained during FSW, 7.7% (4,467) had gained 25% more exp since the end of FSW, 5% (2,878) had gained more than 58% more exp, and 2.3% (1,357) had doubled their FSW experience. From both of these metrics, more than 5% of FSW players continued playing after the end of FSW. 

This means that, by the threshold I set for success, Fresh Start Worlds was successful. 

(Note: I have no idea what Jagex’s internal metric for success was or if my metric is a reasonable one. I wanted to have some metric to test against and set 5% as the threshold before doing any analysis. I think that you could easily argue a different metric or a different threshold.)

## Analysis

I scraped the FSW Overall Hiscores to get a list of who played FSW and their total experience at the end of FSW. I then scraped the main game hiscores to get the current experience of players a couple of months after the conclusion of FSW. For the FSW Hiscores, I only collected username, overall rank, total level, and total experience. For the main game hiscores I collected the level and experience of all skills and the total. Most of the data was collected during the last week of March, with the 150 lowest ranks being collected on April 13th. 

Of the 58,089 players on the FSW hiscores, 21,048 were still on the hiscores in March/April. There are 3 reasons that I can think of that players wouldn’t appear on the hiscores:
They have changed their display name.
They have been banned.
I was rate limited in scraping, so they got misclassified as not on the hiscores but are actually.
From spot checking people who appeared as “Not on hiscores”, I don’t think 3) is an issue. I only spot checked ~10 players, so this assumption could be wrong. Since it takes so long to scrape the hiscores, I won’t be digging into this possible error. Players that have changed their name or have been banned have very different interpretations for the number of players that kept playing. If they changed their display name, they are probably still playing. If they have been banned they very clearly are not still playing on that account. Overall, this means that the number of players with a given experience gain is a lower bound. I unfortunately don’t have a good way to investigate the ~64% of players that are not on the main hiscores. 

![download](https://user-images.githubusercontent.com/47310990/232633264-b735a1fe-28f2-42a3-aac2-735b243e4daa.png)

This figure shows the number of players that gained a given experience since the end of FSW. There are around 4,000 players that are still listed on the hiscores that didn’t gain any experience. That bar has been cut off so that we can see the rest of the data better. Of players that gained any experience, most of them gained more than 1,000 exp. The highest density of players has gained slightly under 1,000,000 exp. My assumption for those players is that they finished up using keys and paper from the Christmas event, but aren’t still actively playing. (This is influenced greatly by my playstyle.)

![image](https://user-images.githubusercontent.com/47310990/232633510-cf649b34-463a-428d-b4e6-fd6ae83a179b.png)

This table shows the number and proportion of players that gained more than a given amount of experience.

![download](https://user-images.githubusercontent.com/47310990/232633302-9164ef3f-ced2-47ad-8fe1-f070a334daa8.png)

This figure shows the experience players gained divided by the experience they had at the end of FSW. This accounts for playstyle in that a player who played a lot during FSW and gained a lot of exp is likely to continue gaining a lot of exp if they continue playing. This plot is cut off at a ratio of 5. There are ~850 players who gained more than 5 times more experience after the end of FSW. The player with the most exp gain was ‘Caraxses’, who had 4,067 experience on the final FSW hiscores and now has 2,214,882,500 exp, for a gained ratio of 544,598. I expect that this is either a player who accidentally made a FSW account and then transferred to the main game almost immediately, or someone who swapped the name off their FSW account to a different account.

![image](https://user-images.githubusercontent.com/47310990/232633400-fff6bca0-7fbd-408e-ba45-cdc20b03600d.png)

This table shows the number and proportion of players that gained more than a given ratio of experience.

## Hiscore Clustering

One final thing I wanted to do with the FSW hiscores data was to see if there are any clusters of players' experience. I ran a k-means clustering algorithm on all of the players that were still on the highscores and it was moderately conclusive at best. I ended up fitting the dataset with 10 clusters, and have plotted the experience breakdowns for the 5 most populous ones. Which one are you in? 

![download](https://user-images.githubusercontent.com/47310990/232633328-025c1ac6-9d12-4aac-8f11-fb31eaa4cc66.png)

The dataset, jupyter notebook used for analysis, and a full list of players and which group they are in can be found on my github. 
