from models import Track
from models.track.track import Duration
db = [
    {
        "title": "Blinding Lights",
        "artist_name": "The Weeknd",
        "album": "After Hours",
        "duration": 200
    },
    {
        "title": "Watermelon Sugar",
        "artist_name": "Harry Styles",
        "album": "Fine Line",
        "duration": 174
    },
    {
        "title": "Levitating",
        "artist_name": "Dua Lipa",
        "album": "Future Nostalgia",
        "duration": 203
    },
    {
        "title": "Shape of You",
        "artist_name": "Ed Sheeran",
        "album": "÷ (Divide)",
        "duration": 263
    },
    {
        "title": "Good 4 U",
        "artist_name": "Olivia Rodrigo",
        "album": "SOUR",
        "duration": 194
    },
    {
        "title": "Stay",
        "artist_name": "The Kid LAROI & Justin Bieber",
        "album": "F*CK LOVE 3: OVER YOU",
        "duration": 155
    },
    {
        "title": "Peaches",
        "artist_name": "Justin Bieber",
        "album": "Justice",
        "duration": 197
    },
    {
        "title": "Kiss Me More",
        "artist_name": "Doja Cat feat. SZA",
        "album": "Planet Her",
        "duration": 204
    },
    {
        "title": "Save Your Tears",
        "artist_name": "The Weeknd",
        "album": "After Hours",
        "duration": 215
    },
    {
        "title": "Montero (Call Me By Your Name)",
        "artist_name": "Lil Nas X",
        "album": "Montero",
        "duration": 137
    },
    {
        "title": "Industry Baby",
        "artist_name": "Lil Nas X & Jack Harlow",
        "album": "Montero",
        "duration": 201
    },
    {
        "title": "deja vu",
        "artist_name": "Olivia Rodrigo",
        "album": "SOUR",
        "duration": 210
    },
    {
        "title": "drivers license",
        "artist_name": "Olivia Rodrigo",
        "album": "SOUR",
        "duration": 242
    },
    {
        "title": "Bad Habits",
        "artist_name": "Ed Sheeran",
        "album": "=",
        "duration": 230
    },
    {
        "title": "Cold Heart (PNAU Remix)",
        "artist_name": "Elton John & Dua Lipa",
        "album": "The Lockdown Sessions",
        "duration": 207
    },
    {
        "title": "Take My Breath",
        "artist_name": "The Weeknd",
        "album": "After Hours",
        "duration": 200
    },
    {
        "title": "Leave The Door Open",
        "artist_name": "Bruno Mars & Anderson .Paak",
        "album": "An Evening with Silk Sonic",
        "duration": 242
    },
    {
        "title": "Monsters",
        "artist_name": "All Time Low feat. Demi Lovato",
        "album": "Wake Up, Sunshine",
        "duration": 182
    },
    {
        "title": "Good Days",
        "artist_name": "SZA",
        "album": "Ctrl",
        "duration": 229
    },
    {
        "title": "Heartbreak Anniversary",
        "artist_name": "Givēon",
        "album": "Take Time",
        "duration": 212
    },
    {
        "title": "Fancy Like",
        "artist_name": "Walker Hayes",
        "album": "Country Stuff",
        "duration": 182
    },
    {
        "title": "Butter",
        "artist_name": "BTS",
        "album": "Butter",
        "duration": 164
    },
    {
        "title": "Stay (with Justin Bieber)",
        "artist_name": "The Kid LAROI",
        "album": "F*CK LOVE 3: OVER YOU",
        "duration": 155
    },
    {
        "title": "Leave Before You Love Me",
        "artist_name": "Marshmello & Jonas Brothers",
        "album": "Leave Before You Love Me",
        "duration": 178
    },
    {
        "title": "Ghost",
        "artist_name": "Justin Bieber",
        "album": "Justice",
        "duration": 194
    },
    {
        "title": "Shivers",
        "artist_name": "Ed Sheeran",
        "album": "=",
        "duration": 233
    },
    {
        "title": "I Want It That Way",
        "artist_name": "Backstreet Boys",
        "album": "Millennium",
        "duration": 217
    },
    {
        "title": "Perfect",
        "artist_name": "Ed Sheeran",
        "album": "÷ (Divide)",
        "duration": 263
    },
    {
        "title": "Uptown Funk",
        "artist_name": "Mark Ronson feat. Bruno Mars",
        "album": "Uptown Special",
        "duration": 269
    },
    {
        "title": "Rolling in the Deep",
        "artist_name": "Adele",
        "album": "21",
        "duration": 228
    },
    {
        "title": "Someone Like You",
        "artist_name": "Adele",
        "album": "21",
        "duration": 285
    },
    {
        "title": "Shape of You",
        "artist_name": "Ed Sheeran",
        "album": "÷ (Divide)",
        "duration": 263
    },
    {
        "title": "Dance Monkey",
        "artist_name": "Tones and I",
        "album": "The Kids Are Coming",
        "duration": 210
    },
    {
        "title": "Say So",
        "artist_name": "Doja Cat",
        "album": "Hot Pink",
        "duration": 238
    },
    {
        "title": "Goodbye Yellow Brick Road",
        "artist_name": "Elton John",
        "album": "Goodbye Yellow Brick Road",
        "duration": 237
    },
    {
        "title": "Somebody That I Used to Know",
        "artist_name": "Gotye feat. Kimbra",
        "album": "Making Mirrors",
        "duration": 236
    },
    {
        "title": "Call Me Maybe",
        "artist_name": "Carly Rae Jepsen",
        "album": "Kiss",
        "duration": 197
    },
    {
        "title": "Counting Stars",
        "artist_name": "OneRepublic",
        "album": "Native",
        "duration": 257
    },
    {
        "title": "Shallow",
        "artist_name": "Lady Gaga & Bradley Cooper",
        "album": "A Star Is Born",
        "duration": 216
    },
    {
        "title": "Old Town Road",
        "artist_name": "Lil Nas X",
        "album": "7",
        "duration": 157
    },
    {
        "title": "Bad Guy",
        "artist_name": "Billie Eilish",
        "album": "When We All Fall Asleep, Where Do We Go?",
        "duration": 194
    },
    {
        "title": "Truth Hurts",
        "artist_name": "Lizzo",
        "album": "Cuz I Love You",
        "duration": 194
    },
    {
        "title": "Happier",
        "artist_name": "Marshmello feat. Bastille",
        "album": "Happier",
        "duration": 212
    },
    {
        "title": "Thank U, Next",
        "artist_name": "Ariana Grande",
        "album": "Thank U, Next",
        "duration": 202
    },
    {
        "title": "Wrecking Ball",
        "artist_name": "Miley Cyrus",
        "album": "Bangerz",
        "duration": 262
    },
    {
        "title": "Chasing Cars",
        "artist_name": "Snow Patrol",
        "album": "Eyes Open",
        "duration": 234
    },
    {
        "title": "Radioactive",
        "artist_name": "Imagine Dragons",
        "album": "Night Visions",
        "duration": 186
    },
    {
        "title": "Ain't It Fun",
        "artist_name": "Paramore",
        "album": "Paramore",
        "duration": 240
    },
    {
        "title": "Irreplaceable",
        "artist_name": "Beyoncé",
        "album": "B'Day",
        "duration": 238
    },
    {
        "title": "Halo",
        "artist_name": "Beyoncé",
        "album": "I Am... Sasha Fierce",
        "duration": 263
    },
    {
        "title": "Super Bass",
        "artist_name": "Nicki Minaj",
        "album": "Pink Friday",
        "duration": 215
    },
    {
        "title": "We Don't Talk Anymore",
        "artist_name": "Charlie Puth feat. Selena Gomez",
        "album": "Nine Track Mind",
        "duration": 217
    },
    {
        "title": "Sorry",
        "artist_name": "Justin Bieber",
        "album": "Purpose",
        "duration": 196
    },
    {
        "title": "Stitches",
        "artist_name": "Shawn Mendes",
        "album": "Handwritten",
        "duration": 227
    },
    {
        "title": "The Middle",
        "artist_name": "Zedd, Maren Morris & Grey",
        "album": "The Middle",
        "duration": 217
    },
    {
        "title": "Sucker",
        "artist_name": "Jonas Brothers",
        "album": "Happiness Begins",
        "duration": 229
    },
    {
        "title": "Nice For What",
        "artist_name": "Drake",
        "album": "Scorpion",
        "duration": 198
    },
    {
        "title": "One Kiss",
        "artist_name": "Calvin Harris & Dua Lipa",
        "album": "One Kiss",
        "duration": 225
    },
    {
        "title": "Rude",
        "artist_name": "MAGIC!",
        "album": "Don't Kill the Magic",
        "duration": 194
    },
    {
        "title": "What Do You Mean?",
        "artist_name": "Justin Bieber",
        "album": "Purpose",
        "duration": 200
    },
    {
        "title": "Girls Like You",
        "artist_name": "Maroon 5 feat. Cardi B",
        "album": "Red Pill Blues",
        "duration": 235
    },
    {
        "title": "My Heart Will Go On",
        "artist_name": "Celine Dion",
        "album": "Let's Talk About Love",
        "duration": 273
    },
    {
        "title": "You're Still the One",
        "artist_name": "Shania Twain",
        "album": "Come On Over",
        "duration": 258
    },
    {
        "title": "I Gotta Feeling",
        "artist_name": "The Black Eyed Peas",
        "album": "The E.N.D.",
        "duration": 274
    },
    {
        "title": "Dance Again",
        "artist_name": "Jennifer Lopez feat. Pitbull",
        "album": "Dance Again... The Hits",
        "duration": 233
    },
    {
        "title": "Dancing Queen",
        "artist_name": "ABBA",
        "album": "Arrival",
        "duration": 233
    },
    {
        "title": "Livin' on a Prayer",
        "artist_name": "Bon Jovi",
        "album": "Slippery When Wet",
        "duration": 249
    },
    {
        "title": "Sweet Caroline",
        "artist_name": "Neil Diamond",
        "album": "Hot August Night",
        "duration": 238
    },
    {
        "title": "Don't Stop Believin'",
        "artist_name": "Journey",
        "album": "Escape",
        "duration": 251
    },
    {
        "title": "Take On Me",
        "artist_name": "a-ha",
        "album": "Hunting High and Low",
        "duration": 231
    },
    {
        "title": "Wonderwall",
        "artist_name": "Oasis",
        "album": "(What's the Story) Morning Glory?",
        "duration": 258
    },
    {
        "title": "Sex on Fire",
        "artist_name": "Kings of Leon",
        "album": "Only by the Night",
        "duration": 210
    },
    {
        "title": "Rolling in the Deep",
        "artist_name": "Adele",
        "album": "21",
        "duration": 228
    },
    {
        "title": "Chasing Cars",
        "artist_name": "Snow Patrol",
        "album": "Eyes Open",
        "duration": 234
    },
    {
        "title": "The Scientist",
        "artist_name": "Coldplay",
        "album": "A Rush of Blood to the Head",
        "duration": 272
    },
    {
        "title": "Fix You",
        "artist_name": "Coldplay",
        "album": "X&Y",
        "duration": 275
    },
    {
        "title": "Photograph",
        "artist_name": "Ed Sheeran",
        "album": "x",
        "duration": 240
    },
    {
        "title": "Castle on the Hill",
        "artist_name": "Ed Sheeran",
        "album": "÷ (Divide)",
        "duration": 262
    },
    {
        "title": "Perfect",
        "artist_name": "Ed Sheeran",
        "album": "÷ (Divide)",
        "duration": 263
    },
    {
        "title": "Firework",
        "artist_name": "Katy Perry",
        "album": "Teenage Dream",
        "duration": 241
    },
    {
        "title": "Teenage Dream",
        "artist_name": "Katy Perry",
        "album": "Teenage Dream",
        "duration": 240
    },
    {
        "title": "All of Me",
        "artist_name": "John Legend",
        "album": "Love in the Future",
        "duration": 268
    },
    {
        "title": "A Thousand Years",
        "artist_name": "Christina Perri",
        "album": "The Twilight Saga: Breaking Dawn – Part 1",
        "duration": 263
    },
    {
        "title": "Halo",
        "artist_name": "Beyoncé",
        "album": "I Am... Sasha Fierce",
        "duration": 263
    },
    {
        "title": "Let It Go",
        "artist_name": "Idina Menzel",
        "album": "Frozen (Original Motion Picture Soundtrack)",
        "duration": 246
    },
    {
        "title": "Someone You Loved",
        "artist_name": "Lewis Capaldi",
        "album": "Divinely Uninspired to a Hellish Extent",
        "duration": 242
    },
    {
        "title": "Stay With Me",
        "artist_name": "Sam Smith",
        "album": "In the Lonely Hour",
        "duration": 182
    },
    {
        "title": "Love Yourself",
        "artist_name": "Justin Bieber",
        "album": "Purpose",
        "duration": 240
    },
    {
        "title": "When We Were Young",
        "artist_name": "Adele",
        "album": "25",
        "duration": 228
    },
    {
        "title": "Into You",
        "artist_name": "Ariana Grande",
        "album": "Dangerous Woman",
        "duration": 217
    },
    {
        "title": "Lose You To Love Me",
        "artist_name": "Selena Gomez",
        "album": "Rare",
        "duration": 226
    },
    {
        "title": "Drunk in Love",
        "artist_name": "Beyoncé feat. Jay-Z",
        "album": "Beyoncé",
        "duration": 239
    },
    {
        "title": "Love Me Like You Do",
        "artist_name": "Ellie Goulding",
        "album": "Fifty Shades of Grey (Original Motion Picture Soundtrack)",
        "duration": 239
    },
    {
        "title": "Riptide",
        "artist_name": "Vance Joy",
        "album": "Dream Your Life Away",
        "duration": 194
    },
    {
        "title": "Supermarket Flowers",
        "artist_name": "Ed Sheeran",
        "album": "÷ (Divide)",
        "duration": 223
    },
    {
        "title": "Afterglow",
        "artist_name": "Ed Sheeran",
        "album": "Single",
        "duration": 187
    }
]
count = 0
for m in db:
    s = Track(m['title'], m['artist_name'], m['album'], m['duration'])
    count +=1
    print(f't{count} = {s}')