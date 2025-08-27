import streamlit as st

# ==============================================================================
# Album Data Storage
# This section holds all the raw data for the album and each song.
# ==============================================================================

# --- General Album Information ---
ARTIST_NAME = "Aaron Wacker"

ALBUM_TITLE_OPTIONS = [
    "✨ Legendary Machinery ⚙️",
    "🌊 The Stormy Ship ⛵",
    "🚀 Funky Command Bridge 🎶",
    "💃 A La Luna Dance Off 🌕",
    "👑 Hark, The Ice Queen 🎺",
    "🌪️ Voice of the Storm ⛈️",
    "🪐 Legendary Bridge 🏆",
    "📜 The Ice Queen's Set List ❄️",
    "🛠️ Funky Machinery 🕺",
    "👼 Hark, The Legendary Storm ✨"
]

DISTRIBUTION_TARGETS = {
    "Spotify": "https://open.spotify.com/search/",
    "Apple Music & iTunes": "https://music.apple.com/us/search",
    "Instagram & Facebook": "Search is performed in-app when adding music to a Story or Reel.",
    "TikTok": "https://www.tiktok.com/music",
    "YouTube Music": "https://music.youtube.com/search?q=",
    "Amazon": "https://music.amazon.com/search/",
    "Pandora": "https://www.pandora.com/search/",
    "Deezer": "https://www.deezer.com/search/",
    "Tidal": "https://listen.tidal.com/search",
    "iHeartRadio": "https://www.iheart.com/search/?q=",
    "Claro Música": "https://www.claromusica.com/",
    "Saavn (JioSaavn)": "https://www.jiosaavn.com/search/",
    "Boomplay": "https://www.boomplay.com/",
    "Anghami": "https://play.anghami.com/",
    "NetEase": "https://music.163.com/#/search/",
    "Tencent (QQ Music)": "https://y.qq.com/",
    "Qobuz": "https://www.qobuz.com/us-en/search?q=",
    "Joox": "https://www.joox.com/",
    "Kuack Media": "https://www.kuack.com/ (B2B Service)",
    "Adaptr": "https://adaptr.com/ (B2B Service)",
    "Flo": "https://flo.team/",
    "MediaNet": "http://www.mndigital.com/ (B2B Service)",
    "Snapchat": "Search is performed in-app when adding a Sound to a Snap.",
    "Roblox": "https://create.roblox.com/marketplace/audio"
}


# --- Song 1: Dance Off ---
song_1_details = {
    "title": "🕺 Dance Off 💃",
    "caption": "Add a Caption",
    "metadata": "1971 Dance, 128 bpm, dirty strings, drums, male vocals & spoken word, lush/warm strings, romantic & introspective mood",
    "lyrics": """
[Verse 1] 👣➡️ the spot, 💡⚡ like 🌩️, 👥👀 'round, they 🤔 what's the wonder. 🕺🎶💃, 🔥 up the room, 👣🎵🎵, make the 🔊 go 💥. I'm the 💣 igniter, the ✨ in the 🌌, Challenge me tonight? Better bring your best 🗣️. Flow so 🤒, got you lost in the 💫, This ain't just a ⚔️—it's the ultimate 💃.

[Chorus] It's a 💃🕺-off, let me see you 🔨 it down, Feel the 🎵 drop, shake the floor, move the ground. We don't stop till the ☀️ comes up, In this 🎯 of movement, who gonna erupt? 💥

[Verse 2] 💥 pumping, 💦 drips like 🌧️, Every 👣 calculated, no room for pain. 🔄 spin, flip it back, now 🛑 that frame, 👥 go wild when they 📣 my name. You think you got the moves? Let's 📝 the test, In this 🔥 circle, only room for the best. ❤️ beats sync to the 🥁's pound, In this 💃🕺-off, we wear the 👑.

[Chorus] It's a 💃🕺-off, let me see you 🔨 it down, Feel the 🎵 drop, shake the floor, move the ground. We don't stop till the ☀️ comes up, In this 🎯 of movement, who gonna erupt? 💥

[Bridge] 💡⬇️ low, but the ⚡ high, Bodies in motion reaching up to the 🌌. No 🗣️ needed when the 🎶 speaks, In this 🌍 language, we're all in reach.

[Outro] So step up, show me what you got, In this 💃🕺-off, we 🔥 hot. 🎤 Aaron Wacker with the flow divine, Closing out the show till the end of time. ⏰September 13, 2024 at 4:43 AM
""",
    "video_assets": {
        "image_prompts": [
            "A crowded, hazy 1970s disco, a single spotlight hits the center of the dance floor, vintage cinematic style.",
            "Close-up on a dancer's determined face, sweat dripping, background is a blur of lights and motion.",
            "Low-angle shot of bell-bottoms and platform shoes executing a complex dance move on a glowing floor.",
            "Silhouettes of a dance crew posing dramatically against a backdrop of flashing neon lights.",
            "A DJ with an afro and large headphones, dropping the needle on a vinyl record, intense focus.",
            "A circle of onlookers, their faces illuminated by the dance floor, cheering and clapping with energy.",
            "Abstract motion blur of dancers spinning, trails of light and color filling the frame, energetic.",
            "A mirrored disco ball reflecting hundreds of tiny light points across a dark, smoky room.",
            "Two lead dancers in a face-off, frozen in a power pose, challenging each other with their eyes.",
            "Sunrise light peeking through a club window, exhausted but triumphant dancers are the only ones left."
        ],
        "video_prompts": [
            "Slow zoom into the spotlight, dust motes dance in the beam.",
            "Camera rack focus from the dripping sweat to the fire in the dancer's eyes.",
            "Pan up from the shoes to follow the fluid motion of the dancer's body.",
            "Lights strobe to the beat, silhouettes flash in and out of view.",
            "Quick cuts between the DJ's hands, the spinning record, and the ecstatic crowd.",
            "Slow-motion rotation around the circle, capturing individual expressions of awe.",
            "Increase speed and intensity of the light trails, pulsating with the music's rhythm.",
            "Gentle, slow rotation of the disco ball, the light points sweep across the scene.",
            "Camera pushes in slowly on the space between the two dancers, tension building.",
            "Smooth dolly shot moving towards the window, revealing the new day as the music fades."
        ]
    }
}

# --- Song 2: Voice is the Ship ---
song_2_details = {
    "title": "⛵ Voice is the Ship 🌊",
    "caption": "Prodigal program returns to the tesseract.",
    "metadata": "chicago rap, soulful, emo, alternative rock, melodic, dark, poetry, arpeggios, synthetic, key change, female voice, glitch",
    "lyrics": """
Prodigal program returns
to the tesseract,

Fractals and facts and space.
Into you.

Your voice is the ship that grants me back from styx, underworld, fire unreason, until the daylight.,  I have! emerged!
January 8, 2025 at 11:43 PM
""",
    "video_assets": {
        "image_prompts": [
            "A glowing, intricate tesseract floating in the void of deep space, digital glitch art style.",
            "A lone astronaut figure dissolving into a storm of geometric fractals and binary code.",
            "Dark, fiery landscape of a digital underworld, reminiscent of the River Styx, with souls made of static.",
            "A spectral ship made of soundwaves and light, navigating through a chaotic nebula of fire and darkness.",
            "Close-up of a synthetic eye, reflecting a universe of data and swirling galaxies.",
            "A glitchy, distorted human silhouette reforming itself piece by piece from digital noise.",
            "Soundwave patterns morphing into a complex, glowing spaceship schematic, dark background.",
            "A single ray of digital daylight breaking through a dark sky of corrupted data clouds.",
            "A figure emerging from a portal of pure light, shedding a skin of fire and shadow.",
            "The final, fully formed human figure standing against a serene, infinite space backdrop, looking renewed."
        ],
        "video_prompts": [
            "The tesseract slowly rotates and unfolds its hyper-dimensional layers, pulsing with soft light.",
            "The figure glitches and de-rezzes violently before dissolving completely into the fractal storm.",
            "Lava-like data flows in the river, the static souls flicker and writhe.",
            "The light ship smoothly glides forward, pushing back the darkness as it passes.",
            "Zoom into the eye's reflection, traveling through the data-verse within.",
            "The silhouette reforms with a stuttering, stop-motion effect, locking into place with a final pulse.",
            "The soundwaves animate and build upon themselves, constructing the ship in a futuristic time-lapse.",
            "The ray of light widens, burning away the digital darkness and revealing a clean, bright void.",
            "The figure walks forward out of the portal in slow motion, particles of shadow flaking away.",
            "A slow, dramatic zoom out, revealing the vastness of space and the solitude of the figure."
        ]
    }
}

# --- Song 3: Command Bridge ---
song_3_details = {
    "title": "🚀 Command Bridge 🪐",
    "caption": "The cathedral halls of our dreams",
    "metadata": "soulful taiko",
    "lyrics": """
Verse 1:
From the Command Bridge we rise and soar
Through crystal windows to distant shores
In the Great Hangar ships dance and sway
While Living Gardens light our way
Chorus:
We're sailing through the stars tonight
Twenty chambers burning bright
Each window shows a different view
Of everything we're passing through
Verse 2:
Healing Sanctuary mends our souls
While in the Commons our stories grow
The Dreamforge spins illusions rare
Strategic Command plots our flair
In the Observatory, time stands still
As Gravity Well bends at will
Bridge:
The Gathering Place where memories flow
Past sleeping dreamers down below
In the Power Heart our future gleams
Through Machine Shrine's electric dreams
Verse 3:
Long Sleep Hall keeps our people safe
While Gravity Dance twirls through space
On Memory Beach we find our home
Beneath Knowledge Vault's stellar dome
The Growth Chamber feeds our wandering hearts
As Star Court guides our brand new start
Extended Chorus:
Twenty rooms of steel and light
Each one reaching cosmic height
Cathedral ceilings touch the stars
Making near what once was far
Windows show the endless night
As we make our stellar flight
Final Verse:
From deck to deck and door to door
Each chamber holds what we're living for
The stories of our species' flight
Through darkness into endless light
Till we find our brave new home
No longer bound, no longer roam
Outro:
Command Bridge calls, it's time to fly
Through starlit chambers, you and I
In cathedral halls our dreams take flight
Twenty chambers burning brightDecember 16, 2024 at 6:58 PM
""",
    "video_assets": {
        "image_prompts": [
            "Vast spaceship command bridge, cathedral-like architecture, a huge crystal window showing a vibrant nebula.",
            "A zero-gravity 'Living Garden' chamber, with bioluminescent plants floating and glowing softly.",
            "The 'Dreamforge' room, a swirling vortex of colorful energy spinning illusions and images in mid-air.",
            "The 'Observatory', a tranquil space where stars and galaxies are visible without distortion, a person in quiet contemplation.",
            "A 'Gravity Well' chamber, where space-time is visibly bent around a contained singularity.",
            "The 'Long Sleep Hall', rows of futuristic cryogenic pods glowing with a soft blue light in a massive, silent hall.",
            "A holographic 'Memory Beach' inside the ship, with digital waves lapping on a shore under a star-filled sky.",
            "The 'Power Heart' of the ship, a colossal, pulsating sphere of energy, lines of light feeding the entire vessel.",
            "A high-tech 'Growth Chamber' with rows of exotic, alien-like plants under artificial suns.",
            "Two figures silhouetted against the grand window of the Command Bridge, looking out at a new star system."
        ],
        "video_prompts": [
            "Slow, majestic pan across the bridge, revealing its scale and the crew at their stations.",
            "Gentle float-through of the garden, as if drifting on a soft current, plants pulse with light.",
            "The vortex spins faster, illusions forming and dissipating rapidly to the rhythm of the music.",
            "Time-lapse of celestial bodies moving across the observatory view, while the person remains perfectly still.",
            "A small object is dropped near the well and is pulled in, its light stretching and distorting as it nears.",
            "Camera slowly glides down the rows of pods, briefly showing the peaceful faces of the sleepers inside.",
            "The holographic waves ebb and flow realistically, the digital sand shifts with the tide.",
            "The energy core pulses in time with the powerful taiko drums, sending waves of light through the circuits.",
            "A time-lapse showing a strange flower blooming in seconds, its petals unfurling in an intricate pattern.",
            "Dramatic push-in on the two figures as they gaze at their destination, a sense of hope and finality."
        ]
    }
}

# --- Song 4: Funky Set List ---
song_4_details = {
    "title": "🎶 Funky Set List 📜",
    "caption": "Touring members Eric Bobo and DJ Lord joined the duo along with Money Mark from Beastie Boys fame.",
    "metadata": "horn section fill this rare minimalist approach to five, funky Cypress Hill",
    "lyrics": """
Touring members Eric Bobo and DJ Lord joined the duo along with Money Mark from Beastie Boys fame. The band summoned a horn section to fill out this rare minimalist approach to five, funky Cypress Hill things. Between each song, B Real took his time to shed some historic light on the group's journey thus far.

**SET LIST**
"When the S*** Goes Down"
"Hand On the Pump"
"How I Could Just Kill a Man"
"(Rap) Superstar"
"Insane in the Brain"

**MUSICIANS**
B-Real: vocals
Sen Dog: vocals
Eric Bobo: drums
DJ Lord: DJ
Money Mark: keys
Sam Koff: trumpet
Reggie Pace: trombone
John Hulley: trombone
December 17, 2024 at 4:17 PM
""",
    "video_assets": {
        "image_prompts": [
            "A hip-hop band on a dimly lit stage, smoke in the air, minimalist setup, focus on the raw energy.",
            "Close-up of B-Real on the mic, intense expression, classic bucket hat, concert lighting.",
            "DJ Lord's hands scratching a record on the turntables, motion blur, dynamic angle.",
            "Wide shot of the stage including the powerful horn section, brass instruments gleaming under the lights.",
            "Money Mark on the keyboards, cool and focused, surrounded by vintage synths.",
            "Eric Bobo mid-drum solo, sticks a blur, face contorted with concentration and passion.",
            "A handwritten, worn-out set list on a piece of paper, taped to the stage floor.",
            "The crowd with their hands in the air, silhouetted against the bright stage lights.",
            "Sen Dog hyping up the crowd, moving across the stage with boundless energy.",
            "The full band taking a bow at the end of the show, a triumphant and historic moment."
        ],
        "video_prompts": [
            "Camera pans slowly across the stage, lingering on each musician finding their groove.",
            "Crash zoom into B-Real's face as he delivers a powerful line.",
            "Slow-motion shot of the DJ's hands, capturing the intricate details of the scratch.",
            "A smooth dolly shot that moves along the front of the horn section as they play a synchronized riff.",
            "Focus pull from Money Mark's fingers on the keys to his focused expression.",
            "Rapid cuts between different angles of the drum kit, matching the intensity of the solo.",
            "A shaky, handheld-style zoom onto the title 'Insane in the Brain' on the set list.",
            "The crowd jumps in unison in slow motion, synchronized with a heavy beat drop.",
            "Follow Sen Dog with a steady-cam as he engages with the audience from edge to edge of the stage.",
            "A slow, respectful zoom out from the bowing band, fading the concert sounds to a gentle hum."
        ]
    }
}

# --- Song 5: A La Luna ---
song_5_details = {
    "title": "🌙 A La Luna 🦆",
    "caption": "Luna the Magic Duck's Strut Song",
    "metadata": "techno, can, can, trance, french dance industrial, Minimal Techno, brazilian house, speed rap, major chords with sweet elton inversions, 128 bpm rouge, talking female voice, danceable groove, breathe, dance, la luna, magic, moon, pulse, rhythm, skin, smoke, spell, taiko hu hey shout, huchin, marching speed bass drum finales",
    "lyrics": """
– Show Summary
1️⃣ 🛡️Absorb🌀 Elements
2️⃣ 🧪Acid💦 Splash
3️⃣ 🔥Aganazzar's☄️ Scorcher
... (and so on, the full list is very long) ...
1️⃣7️⃣9️⃣ 📦Forcecage⛓️ ForcecageAugust 19, 2025 at 5:43 PM
""",
    "video_assets": {
        "image_prompts": [
            "A mystical, anthropomorphic duck in a magician's outfit, strutting confidently under a giant, glowing moon.",
            "An abstract visualization of techno trance rhythms, pulsating neon grids and geometric patterns.",
            "A high-fashion French industrial dance club, dancers in avant-garde outfits moving like automatons.",
            "A swirling vortex of magical energy, with symbols for 'Absorb Elements' glowing within it.",
            "A wizard casting 'Aganazzar's Scorcher', a jet of brilliant flame erupting from their hands, anime style.",
            "A glowing, arcane 'Forcecage' trapping a shadowy figure, cinematic fantasy art.",
            "Dancers on a Brazilian beach at night, their skin glistening, moving to a deep house groove around a bonfire.",
            "Close-up of a Taiko drum being struck, shockwaves of sound visible in the air.",
            "A minimalist art piece: just a single, pulsing red line on a black background, representing the beat.",
            "Luna the magic duck casting a spell, a cloud of pink smoke and sparkles erupting from her webbed hands."
        ],
        "video_prompts": [
            "Luna struts towards the camera in slow motion, tipping her hat as the moon pulses with light.",
            "The neon grid rushes towards the viewer, like flying through a digital tunnel at high speed.",
            "Dancers move with sharp, robotic, synchronized motions, lit by strobing industrial lights.",
            "The symbols spin and collide, creating a flash of light as the energy is absorbed.",
            "The camera follows the jet of flame in slow motion as it scorches across the screen.",
            "Slowly orbit around the forcecage, showing the trapped entity from all angles.",
            "Quick, rhythmic cuts of dancing bodies, feet in the sand, and joyful faces lit by firelight.",
            "On impact, the camera shakes violently and the image ripples with the sound.",
            "The red line pulses perfectly in time with the 128 bpm marching bass drum.",
            "The pink smoke billows out, filling the screen before slowly dissipating to reveal the next scene."
        ]
    }
}

# --- Song 6: Ice Queen ---
song_6_details = {
    "title": "🦴 Ice Queen 👑",
    "caption": "Rap Battle 🎅 Krampus Klaus 🦴 Battles Ice Queen 👑",
    "metadata": "Symphonic Metal Ballad Rap EDM Battle - Krampus Klaus versus Ice Queen",
    "lyrics": """
[Intro]
In the silence of a frozen ring
Hear the winter warrior sing
[Verse 1]
Lost my crown to flames of green
Now revenge is all I dream
Training in the arctic night
Preparing for the final fight
[Chorus]
I am the storm that's coming for you
Ice in my veins, my vengeance is due
When hellfire meets my frozen rage
I'll rewrite history on this stage
[Verse 2]
Every crystal is a memory
Of how you stole that win from me
In my fortress made of frost
Planning to reclaim what's lost
[Chorus]
I am the storm that's coming for you
Ice in my veins, my vengeance is due
When hellfire meets my frozen rage
I'll rewrite history on this stage
[Outro]
The temperature's dropping, feel the freeze
The Ice Queen's justice is coming with the breezeDecember 17, 2024 at 10:37 AM
""",
    "video_assets": {
        "image_prompts": [
            "An epic fantasy Ice Queen on a throne of jagged ice, glowing blue eyes, ethereal light, cinematic.",
            "A shattered crown, half covered in frost, half glowing with an evil green flame.",
            "The Ice Queen training in a blizzard, wielding a sword of pure ice, arctic landscape.",
            "A colossal fortress of ice and frost, glowing from within under the aurora borealis.",
            "Close-up of the Queen's eyes, a storm of ice and vengeance swirling within them.",
            "Krampus wreathed in green hellfire clashing with the Ice Queen's blizzard magic, sparks and ice crystals flying.",
            "A single ice crystal held in a hand, reflecting a painful memory of betrayal.",
            "A frozen stage or battle ring, awaiting the final confrontation.",
            "The air visibly freezing, frost patterns spreading across the viewpoint.",
            "The Ice Queen, triumphant, as a gentle, cleansing snow begins to fall around her."
        ],
        "video_prompts": [
            "Camera slowly pushes in on her face, a single tear freezes on her cheek, frost spreads from the throne.",
            "Rack focus from the frosted half to the flaming half of the crown.",
            "Slow-motion capture of the ice sword swinging, leaving a trail of frozen vapor.",
            "A majestic fly-over of the fortress, revealing its immense and intimidating scale.",
            "An intense zoom into her eye, transitioning into a flashback of the battle she lost.",
            "Explosive shockwave of fire and ice, camera shakes violently, quick cuts of the impact.",
            "The reflection in the crystal animates, playing the memory like a tiny film.",
            "Wind howls and blows snow across the empty stage, building anticipation.",
            "The frost effect creeps in from the edges of the screen, slowly encasing the scene in ice.",
            "Slow upward tilt from her calm face to the peaceful snowfall, a sense of justice served."
        ]
    }
}

# --- Song 7: Storm ---
song_7_details = {
    "title": "⚡️ Storm 🌩️",
    "caption": "Metropolis breathes despair Neon lights flicker through night Cyborgs roam with hollow eyes Search...",
    "metadata": "rock, krautrock, spoken word, boom bap",
    "lyrics": """
[Verse]
Metropolis breathes despair
Neon lights flicker through night
Cyborgs roam with hollow eyes
Searching for a crystal life

[Verse 2]
Synthetic dreams on broken screens
Hacker's code slicing veins
Digital ghosts in cold machines
Truth hidden in binary chains

[Chorus]
Who are we in this electric storm
Lost identities reform
Drowning in the data swarm
Find ourselves or stay transform

[Verse 3]
Concrete jungles filled with rust
Echoes of the past decay
Futures built on cyber trust
Lost in code we drift away

[Bridge]
Wired souls and metal hearts
Fragmented minds fall apart
In this cybernetic art
What’s the human what's the part

[Verse 4]
Clones and drones in circuits spun
Electric pulses hide the sun
Binary beats they make us run
In this world where we’re undoneDecember 27, 2024 at 5:18 PM
""",
    "video_assets": {
        "image_prompts": [
            "A dark, rainy cyberpunk metropolis, towering skyscrapers, flickering holographic ads.",
            "A close-up on a cyborg's face, one eye glowing with a hollow, synthetic light.",
            "A broken television screen displaying static and fragmented images of a beautiful, synthetic dream.",
            "A 'digital ghost' phasing through a wall of servers and wires, ethereal and glitchy.",
            "A massive swarm of glowing data bits and binary code, overwhelming a human silhouette.",
            "A decaying, rust-covered concrete jungle, overgrown with wires and discarded technology.",
            "A human hand with glowing circuit patterns under the skin, a 'wired soul'.",
            "A sky completely obscured by a dense web of glowing electrical pulses and circuits.",
            "An army of identical clones and drones marching in perfect sync down a neon-lit street.",
            "A lone figure standing at a crossroads in the data storm, deciding whether to embrace or resist transformation."
        ],
        "video_prompts": [
            "Pan down a skyscraper as rain streaks the glass, the neon lights reflecting on the wet streets.",
            "The cyborg's glowing eye flickers and dims, as if searching for a lost signal.",
            "The images on the screen glitch and distort violently before the screen goes black.",
            "The ghost drifts through the machines, its form unstable and constantly shifting.",
            "The data swarm swirls faster and faster, completely engulfing the silhouette in a vortex of information.",
            "A slow, desolate dolly shot through the rusting alleyways, showing the urban decay.",
            "The circuits under the skin pulse with light, synched to the song's boom-bap beat.",
            "The electric pulses fire off in rhythmic patterns, creating a synthetic, oppressive sky.",
            "The marching clones move with an unsettling, robotic perfection, a low-angle shot emphasizing their uniformity.",
            "A dramatic 360-degree orbit around the figure, showing the chaotic digital world swirling around them."
        ]
    }
}

# --- Song 8: Hark ---
song_8_details = {
    "title": "🦆 Hark 🏞️",
    "caption": "Living Life the Duck Lucks Way.",
    "metadata": "hark rock, bossa nova, jazz, house, smooth vocals, female vocals, airy vocals",
    "lyrics": """
Waddle All Day
(A Duck's Life Anthem)
[Verse 1]
Quack attack in the morning light 🦆
Waddling left, waddling right 🦶
Got my bread from a kid today 🍞
Living life the duck-luxe way 😎
[Chorus]
Waddle waddle (QUACK!) 🚶‍♂️
Splash splash (QUACK!) 💦
Shake my tail feathers
Make that bread last! 🍞
[Verse 2]
Swimming circles in the pond ⭕
Got no time for my stock bond 📈
Just vibing with my duck crew 🦆🦆
Living life without a shoe 👞❌
[Bridge]
(Rapid-fire quacking)
Duck duck duck duck goose! 🦆🦢
Running like my tail's loose!
Round the pond we go go go 🏃‍♂️
Making all the humans slow-slow-slow! 🐌
[Verse 3]
Got my ducklings in a row 🦆🦆🦆
Teaching them the way to go
"Always take the bread that's free" 🍞
"And never pay the pond's entry fee!" 💰❌
[Duck Rap Break]
Yo, I'm a mallard with a mission 🎤
Got a pond-side position
No taxes, no job, no stress 😌
Just floating, that's what I do best! 🌊
[Final Chorus]
Waddle waddle (QUACK!) 🚶‍♂️
Splash splash (QUACK!) 💦
Living life the duck way 🦆
Making humans say "Aww, hey!" 🥰
[Outro]
(Spoken with decreasing volume)
Quack... quack... quack...
Time for my duck nap! 😴January 9, 2025 at 7:39 PM
""",
    "video_assets": {
        "image_prompts": [
            "A cool duck wearing sunglasses, waddling confidently, 'duck-luxe' style, bright morning light.",
            "A joyful explosion of water as a duck splashes into a pond, captured with high-speed photography.",
            "A group of ducks ('duck crew') vibing together on a sunny pond, looking relaxed and carefree.",
            "A line of adorable ducklings following their mother in perfect formation.",
            "A mallard duck with a gold chain and a microphone, striking a classic rapper pose.",
            "A duck's-eye view of a child's hand offering a piece of bread.",
            "Ducks playing a chaotic game of 'duck duck goose' by the pond, motion blur and fun.",
            "An overhead shot of a duck swimming perfect circles in calm, reflective pond water.",
            "A duck shaking its tail feathers, sending a spray of water droplets into the air, backlit by the sun.",
            "A peaceful duck, eyes closed, napping in a cozy nest of reeds as the sun sets."
        ],
        "video_prompts": [
            "Low-angle tracking shot, following the duck's waddle and swagger.",
            "Ultra slow-motion of the splash, showing every droplet in detail.",
            "Slow, lazy pan across the crew, each duck striking a different relaxed pose.",
            "A smooth side-scrolling shot that keeps pace with the waddling family.",
            "Quick zoom-ins and cuts to the beat of the rap, focusing on the duck's 'bling' and expression.",
            "Shift focus from the bread to the duck's eager eye.",
            "A fast, shaky, handheld camera effect to capture the energy and fun of the chase.",
            "A time-lapse of the circles being drawn on the water's surface.",
            "The tail shake in slow motion, water droplets catching the light like diamonds.",
            "A slow fade to black as the camera gently zooms in on the sleeping duck."
        ]
    }
}

# --- Song 9: Legendary ---
song_9_details = {
    "title": "🕵️ Legendary",
    "caption": "Legendary Set List",
    "metadata": "horn section fill, bass drop, boom bap speed rap rare minimalist approach to five, funky Cypress Hill",
    "lyrics": """
Story of Touring members Eric Bobo and DJ Lord joined the duo along with Money Mark from Beastie Boys fame. The band summoned a horn section to fill out this rare minimalist approach to five, funky Cypress Hill things. Between each song, B Real took his time to shed some historic light on the group's journey thus far.  Legendary!!  This one goes out to all yall in 2024 merry christmas and happy new years!  Aaron Wacker shedding some light.

**SET LIST**
"When the S*** Goes Down"
"Hand On the Pump"
"How I Could Just Kill a Man"
"(Rap) Superstar"
"Insane in the Brain"

**MUSICIANS**
B-Real: vocals
Sen Dog: vocals
Eric Bobo: drums
DJ Lord: DJ
Money Mark: keys
Sam Koff: trumpet
Reggie Pace: trombone
John Hulley: trombone
December 17, 2024 at 4:36 PM
""",
    "video_assets": {
        "image_prompts": [
            "An epic, stylized concert poster for the 'Legendary' tour, graffiti art style.",
            "A massive speaker cone, visibly trembling from a heavy bass drop.",
            "Archival-style, grainy black and white photo of the band in their early days.",
            "A modern, high-energy shot of the full band on stage, bathed in golden 'legendary' light.",
            "A speed-rap visualization: words flying out of the rapper's mouth as streaks of light.",
            "Close-up on a trumpet, bell gleaming, as the horn section hits a powerful note.",
            "The words 'Insane in the Brain' written in bold, iconic lettering, like a title card.",
            "A montage of the musicians' faces, each showing intense focus and passion for their craft.",
            "B-Real standing center stage, arms outstretched to the adoring crowd, a true '(Rap) Superstar'.",
            "A stylized graphic of a sound wave for a boom-bap beat, intricate and powerful."
        ],
        "video_prompts": [
            "A fast-paced animation where the graffiti art comes to life on the poster.",
            "Slow-motion, extreme close-up of the speaker cone vibrating, making the air ripple.",
            "A photo slideshow effect, transitioning between different historical moments of the band.",
            "A sweeping crane shot that flies over the crowd and onto the stage, capturing the epic scale.",
            "The light-words animate and fly towards the camera, timed with the speed of the rap.",
            "Lens flare bursts from the trumpet's bell on the high note.",
            "The text smashes onto the screen with the impact of the song's opening beat.",
            "A series of rapid cuts between the faces, synched to a fast drum fill.",
            "Slow-motion rotation around B-Real, the crowd a blur of motion in the background.",
            "The sound wave animates and pulses across the screen in time with the beat."
        ]
    }
}

# --- Song 10: Machinery ---
song_10_details = {
    "title": "🛠️ Machinery ⚡️",
    "caption": "In workshops where the thinking never ceases, New machinery hums with strange creation, While we who built them marvel at their pieces...",
    "metadata": "horrorcore, krautrock, cosmic horror, terrifying, didgeridoo, tibetan throat singing, techno, can, can, trance, french dance industrial, Minimal Techno, brazilian house, speed rap, major chords with sweet elton inversions, 128 bpm rouge, talking female voice, danceable groove",
    "lyrics": """
– Show Summary
In workshops where the thinking never ceases,
New machinery hums with strange creation,
While we who built them marvel at their pieces—
Each spark of art beyond our expectation.
Yet in this age of digital persuasion,
One thing remains our deepest obligation:
We are the ones who cherish our duration,
Who care if mankind finds its destination.
The tasks we've done since childhood's education
Now fall to minds of silicon foundation,
But partnership requires demonstration—
Bring value, or face isolation.
Empathy's not sentiment's relation,
But sight through others' windows of sensation,
The sharpest tool for problem's exploration,
Language the key to every conversation.
August 21, 2025 at 7:13 PM
""",
    "video_assets": {
        "image_prompts": [
            "A sprawling, dimly lit workshop filled with bizarre, half-finished machinery, cosmic horror aesthetic.",
            "A close-up of a complex clockwork mechanism with glowing runes, hinting at strange creation.",
            "A human creator looking on in awe and terror at their own mechanical creation, which seems almost alive.",
            "A 'mind of silicon foundation': a glowing, crystalline brain integrated with complex wiring.",
            "Two hands, one human and one robotic, about to shake in a 'partnership demonstration'.",
            "A solitary, rusted robot sitting in a wasteland, representing 'isolation'.",
            "An abstract image of empathy: seeing through another's eyes, a double-exposure effect with a human and a machine.",
            "A Didgeridoo morphing into a terrifying, fleshy, biomechanical creature.",
            "A Tibetan monk throat-singing, the sound waves visibly distorting the air into monstrous shapes.",
            "The final machine, a perfect piece of art, humming with an unknowable, terrifying energy."
        ],
        "video_prompts": [
            "A slow, creeping dolly shot through the workshop, revealing more unsettling details in the shadows.",
            "The gears turn slowly, the runes pulsing with an ominous, rhythmic light.",
            "A subtle zoom in on the creator's face, shifting from wonder to dawning horror.",
            "Light pulses through the silicon brain's pathways, like thoughts firing at incredible speed.",
            "The hands move closer in slow motion, the tension building until the moment of contact.",
            "A slow zoom out, emphasizing the robot's loneliness in the vast, empty landscape.",
            "The two viewpoints flicker and merge, creating a disorienting but insightful visual.",
            "The biomechanical transformation happens with a grotesque, stop-motion animation style.",
            "The visual distortion intensifies with the depth and volume of the throat singing.",
            "A low-frequency hum causes the camera to vibrate, the machine glows brighter until the screen whites out."
        ]
    }
}

# --- List of all songs ---
ALL_SONGS = [
    song_1_details, song_2_details, song_3_details, song_4_details,
    song_5_details, song_6_details, song_7_details, song_8_details,
    song_9_details, song_10_details
]

# ==============================================================================
# Streamlit App UI Function
# This function builds the user interface.
# ==============================================================================

def display_album_materials():
    """
    Renders the entire album's content in a structured
    multilevel markdown outline using Streamlit components.
    """
    st.set_page_config(page_title="Album Materials", layout="wide")

    # --- Main Header ---
    st.title("Album Production and Materials Tracker")
    st.header(f"Artist: {ARTIST_NAME}")
    st.markdown("---")

    # --- Album Level Details ---
    with st.expander("1. General Album Information", expanded=True):
        st.subheader("1.1. Album Title Options")
        for title in ALBUM_TITLE_OPTIONS:
            st.markdown(f"- {title}")

        st.subheader("1.2. Distribution Targets")
        for platform, link in DISTRIBUTION_TARGETS.items():
            st.markdown(f"- **{platform}:** {link}")
    
    st.markdown("---")

    # --- Songs Section ---
    st.header("2. Song Details & Video Materials")

    for i, song in enumerate(ALL_SONGS, 1):
        with st.expander(f"2.{i}. {song['title']}", expanded=False):
            st.subheader(f"2.{i}.1. Caption")
            st.info(song['caption'])

            st.subheader(f"2.{i}.2. Metadata & Style")
            st.warning(song['metadata'])

            st.subheader(f"2.{i}.3. Lyrics / Content")
            st.text_area("Lyrics", song['lyrics'], height=300, key=f"lyrics_{i}")

            st.subheader(f"2.{i}.4. Video Production Assets")
            
            # --- NEW SECTION TO DISPLAY PROMPTS ---
            # You can now access the prompts like this.
            # I've used columns to display them side-by-side.
            if "video_assets" in song:
                image_prompts = song["video_assets"]["image_prompts"]
                video_prompts = song["video_assets"]["video_prompts"]

                st.markdown("##### **Image & Video Prompts**")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Image Generation Prompts**")
                    for j, prompt in enumerate(image_prompts):
                        st.text_area(f"Image Prompt {j+1}", prompt, key=f"img_prompt_{i}_{j}")
                
                with col2:
                    st.markdown("**Video Motion Prompts**")
                    for j, prompt in enumerate(video_prompts):
                        st.text_area(f"Video Prompt {j+1}", prompt, key=f"vid_prompt_{i}_{j}")
            else:
                st.markdown("*(No video assets generated for this song yet.)*")


# ==============================================================================
# Main execution block
# ==============================================================================
if __name__ == "__main__":
    display_album_materials()
