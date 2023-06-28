# This is the GlidedRose Refactoring test task

## Problem: 

Gilded Rose Refactoring Kata

Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that we can begin selling a new category of items. First an introduction to our system:

All items have a SellIn value which denotes the number of days we have to sell the item
All items have a Quality value which denotes how valuable the item is
At the end of each day our system lowers both values for every item
Pretty simple, right? Well this is where it gets interesting:

Once the sell by date has passed, Quality degrades twice as fast
The Quality of an item is never negative
"Aged Brie" actually increases in Quality the older it gets
The Quality of an item is never more than 50
"Sulfuras", being a legendary item, never has to be sold or decreases in Quality
"Backstage passes", like aged brie, increases in Quality as it's SellIn value approaches; Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
We have recently signed a supplier of conjured items. This requires an update to our system:

"Conjured" items degrade in Quality twice as fast as normal items

Feel free to make any changes to the UpdateQuality method and add any new code as long as everything still works correctly. However, do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover for you).

Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.

## How to approach it?

The challenge was tackled by employing principles of Object-Oriented Programming(OOP). I identified unique behaviors in different types of items and encapsulated these within separate classes, by follow these breakdown:

1. Identify Unique Item Behavior: I first identified types of items sold by Gilded Rose have unique behaviors regarding how their quality changes over time. For instance, while most items degrade in quality with age, 'Aged Brie' increases in quality, 'sulfuras' never alters, 'Backstage passes' gain value before a concert but drop to zero value afterwards, and 'Conjured' items degrade twice as fast as normal items.
2. Specific Item Classes: I created distinct classes for each type of item to encapsulate the unique behavior related to that item's quality update. This approach simplifies the code, making it more understandable and maintainable. The classes are : 'StandardItem', 'AgedBrieItem', 'BackstagePassesItem', 'SufurasItem', and 'ConjuredItem'.
3. Test-Driven Development: I wrote tests for each class to verify the correctness of our implementation, which is a crucial practice in professional software development. The tests ensure that our code works as expected, enabling safer future modifications.
4. Edge Case Management: I handled edge cases to ensure that an item's quality never goes below 0 or above 50 (except for 'Sulfuras', which has a constant quality of 80). These cases are addressed in each item's 'update_quality' method.

Overall, the approach enhances the code's readability, maintainability, and testability by incorporating principles of object-oriented design and test-driven development. While this may seem complex for a simple system, it proves beneficial as the system grows in complexity. 
