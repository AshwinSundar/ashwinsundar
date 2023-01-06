# Engineering Risks

Date: November 2022

I recently saw an interesting, flippant post on Reddit:

**SAVE THIS LOCALLY**
<img src="https://i.redd.it/pk7ja7q739y91.jpg">

Why, indeed? One redditor responded,

"NASA had to pay $14 billion for the oversize luggage fee."

Haha, possibly.

"Some poor baggage handler doesn't have to toss 200 space shuttles onto the plane, but they would have to toss 200 60 pound bags on the plane."

Interesting, that makes sense. I think we're getting closer, but still not sure.

"Because weight management, fuel burn, and the airlines like money. Also, too much weight on an airplane can lead to it underperforming."

Aha, okay! "Airlines like money" is a pretty generic argument but very popular currently. Who can disprove it?

"Space shuttle weight empty: 165,000 pounds

---

Boeing 747 passengers: 416 people x 250lb person estimate = 104,000 pounds

416 passengers' 50lb carryon luggage: 20,800 pounds

Only ONE overweight/oversized/extra checked bag per person: 70lb x 416 people = 29,120 pounds

---

Starting to add up yet?"

Ah you wonderful person! You did the math! I am going to just take it at face value and accept it, because this explanation makes the most sense and is the simplest. But someone has a really good follow-up question!

"Is the average of 250lb correct? I'm using metric and an online search said that the average is only 130lb. I'm not sure if there are two different units called pounds."

As far as I know there is not, at least not in the confusing way that there's seem to be multiple tons (short ton/US ton = 2,000 pounds, long ton/British ton = 2240 pounds, and the metric ton = 1000 kiograms/2204 pounds). But the first point is a really good question! Why are we overestimating SO MUCH for the average weight? Why not just pick the average?

If weight is normally distributed in the population, meaning if you plotted a graph of number of people in the population at every single weight, you would end up with a bell curve:

** link to galton board.mp4 **

The unique feature of a bell curve is that exactly 50% of the area of that curve lies in front of the mean, and 50% of the area of the curve lies behind the mean. In our case, this means that if we set max takeoff weight to:

`NUMBER_OF_PASSENGER * AVG_WEIGHT`

50% of full planes will take off past the designed max takeoff weight.

So instead, the team (composed of engineers and risk experts) get together and find some statistics on the distribution of weight in the population, and design an aircraft that can hold any 400 randomly picked passengers from the population, and ensure the vast, vast majority of flights do NOT take off past that weight. Beyond that, they may also mitigate the risk of that occuring even further down, such as by taking other steps to make sure the max takeoff weight is not exceeded
