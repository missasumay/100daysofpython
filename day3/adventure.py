# for proper exiting - sys.exit(1) = closes the program
import sys

# set password
password = "TALES WHISPERED IN SHADOWS"

print("Welcome to the thrilling world of our Choose Your Own Adventure game! Prepare to embark on a journey filled with excitement, danger, and endless possibilities. To navigate through this immersive experience, remember to input your commands in UPPERCASE. Your decisions will shape the outcome of your adventure, so choose wisely. Are you ready to begin? Then let's go!")

# part one
lake = input("\nIn the heart of the forest, nestled between towering trees and lush greenery, lies a tranquil lake. Its surface shimmers like a sheet of glass in the gentle breeze, reflecting the colors of the surrounding landscape. Ducks glide peacefully across its mirrored expanse, while fish dart beneath the surface, creating ripples that dance in the sunlight. The air is filled with the soothing symphony of chirping birds and rustling leaves, adding to the serene ambiance of this hidden gem. Here, amidst the serenity of nature, one can't help but feel a sense of calm and wonder, as if time itself slows down in reverence to the beauty of the lake. On the other side you see a forest, that calls to you. You have three options how to procceed: do you GO AROUND the lake, SWIM across it or use a BOAT to reach to the forest? ").upper()

if lake == "GO AROUND":
    print("\nAs you embark on your journey around the lake, the path twists and turns, revealing new vistas at every bend. The air is filled with the earthy scent of damp soil and the sweet fragrance of wildflowers that line the trail. Sunlight filters through the canopy above, casting dappled shadows on the forest floor. Along the shoreline, the water laps gently against rocks, creating a soothing melody that accompanies your steps. Birds flit among the branches, their songs echoing through the trees. With each passing moment, the beauty of your surroundings fills you with a sense of awe and gratitude as you immerse yourself in the timeless rhythm of nature. On your way you notice a sign with a word TALES.\n")
elif lake == "SWIM":
    print("\nAs you glide through the cool waters of the lake, the ripples you create spread out in gentle waves behind you. The sun's rays dance on the surface, casting shimmering reflections that mesmerize as you swim onward. Around you, the tranquility of the water envelopes you, offering a sense of peace and serenity. As you reach the edge of the lake, the forest looms ahead, its towering trees beckoning you closer. With each stroke, you draw nearer to the lush greenery that awaits. The sounds of nature grow louder—the rustling of leaves, the chirping of birds—calling you deeper into the heart of the woods. Finally, you emerge from the water, stepping onto the soft earth of the forest floor. The cool breeze carries the scent of pine and damp earth, invigorating your senses. With each step beneath the canopy of trees, you feel a sense of adventure stirring within you, eager to explore this enchanting realm that lies ahead.\n")
elif lake == "BOAT":
    print("\nAs you set sail across the tranquil lake, the gentle sway of the boat beneath you lulls you into a state of peaceful anticipation. The water stretches out before you, reflecting the azure sky above like a flawless mirror. With each stroke of the oar, the boat glides effortlessly through the calm waters, leaving a trail of ripples in its wake. As you draw closer to the opposite shore, the outline of the forest comes into view, its lush green canopy beckoning you with promises of adventure. The air is alive with the symphony of nature—the chirping of birds, the rustling of leaves—a melody that fills you with excitement for the journey ahead. As the boat reaches the shore, you step onto solid ground, greeted by the soft earth beneath your feet. The scent of pine and damp moss fills the air, heightening your senses and fueling your desire to explore the mysteries that lie within the depths of the forest. With each step you take into the unknown, you feel a sense of wonder and exhilaration coursing through your veins, eager to uncover the secrets that await amidst the towering trees. On your way you notice a sign with a word TALES.\n")
else:
    print("\nOops! It seems you've entered an unexpected command. Game will be terminated.")
    sys.exit(1)

# part two
forest = input("\n Standing in front of the forest, you inhale the crisp air, scented with pine and earth. The world holds its breath in anticipation, trees standing silent in the stillness. You need to make a decision: will you GO THROUGH the forest or you decide to use nearby path to GO AROUND it? ").upper()

if forest == "GO THROUGH":
    print("\nAs you journey through the forest, towering trees envelop you in their leafy embrace. Sunlight filters through the canopy above, casting dappled shadows on the forest floor. Each step crunches softly on the bed of fallen leaves, while the air is alive with the symphony of nature—birdsong, rustling leaves, and the occasional scurry of small creatures. With each twist and turn of the path, you feel a sense of wonder and adventure, as if each moment holds the promise of discovery amidst the ancient secrets of the woods. On one of the trees you see a word carved out: WHISPERED.\n")
elif forest == "GO AROUND":
    print("\nAs you navigate the perimeter of the forest, the trail winds beneath the towering trees, offering glimpses into the heart of the woodland realm. Sunlight filters through the dense foliage, casting shifting patterns of light and shadow upon the forest floor. Each step brings you closer to the mysteries hidden within the depths of the woods. The air is filled with the earthy scent of moss and fallen leaves, mingled with the sweet fragrance of wildflowers that dot the forest's edge. Birds flit among the branches, their songs echoing through the trees, while small creatures scurry and rustle in the underbrush. With every turn of the path, you find yourself drawn deeper into the enchanting beauty of the forest, each moment filled with the promise of new adventures and discoveries waiting to be made amidst the whispering trees.\n")
else:
    print("\nOops! It seems you've entered an unexpected command. Game will be terminated.")
    sys.exit(1)

#part three
city = input ("\nAs you reach the town, you spot an elder woman and a young man chatting by the roadside. Their contrasting appearances hint at a shared bond, amidst the lively backdrop of the bustling town square. Their interaction captivates you, sparking curiosity about the stories they hold and the wisdom they might share.After a few seconds, they go in different directions. You can only follow and talk to one of them. Who do you talk to: an ELDER woman or a young MAN? ").upper()

if city == "ELDER":
    print("\nAs you approach the elder woman in the heart of the town, her warm gaze meets yours, inviting conversation. Her face carries the gentle lines of experience, hinting at a wealth of wisdom accumulated over the years. As you exchange words, her voice is soft yet resonant, weaving tales of the town's history and offering insights born from a lifetime of living. In her presence, you find yourself drawn into a world where time seems to slow, as if each moment holds the promise of discovering something profound amidst the ordinary hustle and bustle of town life. During your conversation she mentions the word IN to you.\n")
elif city == "MAN":
    print("\nApproaching the young man in the bustling town square, you're met with an eager smile and bright eyes filled with curiosity. His youthful energy is contagious as you engage in conversation, exchanging thoughts on dreams, aspirations, and the pulse of the town. With enthusiasm, he shares stories of ambition and optimism, igniting a spark of inspiration within you. In his company, the town feels alive with possibility, each word a thread weaving a tapestry of shared hopes and aspirations for the future. During your conversation he mentions the word WITH to you.\n")
else:
    print("\nOops! It seems you've entered an unexpected command. Game will be terminated.")
    sys.exit(1)

#part four
inn = input("\nYou stumble upon the town inn, its cozy interior beckoning with the warmth of lanterns and a crackling hearth. Welcomed by the friendly innkeeper, you're embraced by the scent of homecooked meals and ale. Taking a seat by the fire, you're enveloped in the comforting atmosphere, finding refuge from your journey within its walls. A group of friendly-looking people ask you to join them. What do you do: TALK to them or leave to your room to go to SLEEP? ").upper()

if inn == "TALK":
    print("\nYou notice a group of friendly-looking people in the cozy inn and decide to join them. As you approach, they welcome you with warm smiles and open arms, inviting you to share in their laughter and conversation. Sitting among them, you feel a sense of belonging, as if you've found a community within the walls of the inn. Together, you share stories and laughter, forging connections that make you feel right at home amidst the camaraderie of newfound friends.\n")
    # part four cont.
    party = input("\nAmidst shared laughter and stories, they extend an invitation for you to stay longer, sensing a kindred spirit in your company. Grateful for their hospitality, you find yourself captivated by their tales and the sense of belonging they offer. Yet you feel exhaustion creeping in. What do you do: STAY with them or go to your room to SLEEP? ").upper()

    if party == "STAY":
        print("\nAs the evening wears on, the fire in the hearth casts a soft, flickering light that dances across the faces of your newfound friends, illuminating the lines of laughter and the sparkle of shared memories. In their company, the worries and cares of the outside world seem to melt away, replaced by a sense of belonging and acceptance that fills you with warmth from the inside out. Time seems to lose its meaning as you lose yourself in the easy rhythm of conversation and companionship. It's as if the inn itself has become a sanctuary, a haven of friendship and fellowship amidst the chaos of the world outside its doors. During your conversation a piece of paper with a word SHADOWS is passed around.\n")
    elif party == "SLEEP":
        print("\nYou ascend the creaky staircase to your room in the cozy inn, the soft glow of lanterns guiding your way. Unlocking the door, you step into a haven of comfort and tranquility. The room is simple yet inviting, with a comfortable bed draped in crisp linens and a small, crackling fire casting a warm glow. With a sigh of relief, you kick off your shoes and sink into the plush mattress, feeling the weight of the day melt away. The sounds of the inn below gradually fade into the background as you nestle beneath the covers, cocooned in a sense of peace and serenity. As sleep beckons, you close your eyes and surrender to its embrace, drifting off into a realm of dreams where worries cease to exist and the promise of tomorrow awaits. In the quiet sanctuary of your room, you find solace and rest, grateful for the refuge that the inn provides amidst the journey of life.\n")
    else:
        print("\nOops! It seems you've entered an unexpected command. Game will be terminated.")
elif inn == "SLEEP":
    print("\nYou ascend the creaky staircase to your room in the cozy inn, the soft glow of lanterns guiding your way. Unlocking the door, you step into a haven of comfort and tranquility. The room is simple yet inviting, with a comfortable bed draped in crisp linens and a small, crackling fire casting a warm glow. With a sigh of relief, you kick off your shoes and sink into the plush mattress, feeling the weight of the day melt away. The sounds of the inn below gradually fade into the background as you nestle beneath the covers, cocooned in a sense of peace and serenity. As sleep beckons, you close your eyes and surrender to its embrace, drifting off into a realm of dreams where worries cease to exist and the promise of tomorrow awaits. In the quiet sanctuary of your room, you find solace and rest, grateful for the refuge that the inn provides amidst the journey of life.\n")
else:
    print("\nOops! It seems you've entered an unexpected command. Game will be terminated.")
    sys.exit(1)

#part five
safe = input("\nYou awaken in the soft light filtering through the curtains of your room in the inn. Stretching languidly, you notice an old safe tucked in the corner, its metallic surface gleaming in the morning light. Curiosity piqued, you approach it and notice a digital keypad, awaiting a four-word password.Your mind races as you contemplate the possibilities. With a sense of determination, you begin to ponder potential combinations, each word holding the promise of unlocking the secrets hidden within. With a deep breath, you prepare to input the password, eager to uncover the mystery that lies behind the safe's unyielding door. \n\nType in password: ").upper()

if safe == "TALES WHISPERED IN SHADOWS":
    print("\nCongratulations on completing the game! Your skill, determination, and strategic prowess have set you apart as a true champion. May this victory be a testament to your dedication and perseverance. Here's to celebrating your well-deserved success!")
    sys.exit(1)
else:
    print("\nGame Over: Unfortunately, your journey has come to an end. But fear not, for every end is a new beginning. Keep striving, keep playing, and you'll conquer new challenges ahead. Restart and embark on another adventure!")
    sys.exit(1)