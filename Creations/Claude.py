import streamlit as st

# ==============================================================================
# Album Data Storage with Image & Video Prompts
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
    "lyrics": """[Verse 1] 👣➡️ the spot, 💡⚡ like 🌩️, 👥👀 'round, they 🤔 what's the wonder. 🕺🎶💃, 🔥 up the room, 👣🎵🎵, make the 🔊 go 💥. I'm the 💣 igniter, the ✨ in the 🌌, Challenge me tonight? Better bring your best 🗣️. Flow so 🤒, got you lost in the 💫, This ain't just a ⚔️—it's the ultimate 💃.

[Chorus] It's a 💃🕺-off, let me see you 🔨 it down, Feel the 🎵 drop, shake the floor, move the ground. We don't stop till the ☀️ comes up, In this 🎯 of movement, who gonna erupt? 💥

[Verse 2] 💥 pumping, 💦 drips like 🌧️, Every 👣 calculated, no room for pain. 🔄 spin, flip it back, now 🛑 that frame, 👥 go wild when they 📣 my name. You think you got the moves? Let's 📝 the test, In this 🔥 circle, only room for the best. ❤️ beats sync to the 🥁's pound, In this 💃🕺-off, we wear the 👑.

[Chorus] It's a 💃🕺-off, let me see you 🔨 it down, Feel the 🎵 drop, shake the floor, move the ground. We don't stop till the ☀️ comes up, In this 🎯 of movement, who gonna erupt? 💥

[Bridge] 💡⬇️ low, but the ⚡ high, Bodies in motion reaching up to the 🌌. No 🗣️ needed when the 🎶 speaks, In this 🌍 language, we're all in reach.

[Outro] So step up, show me what you got, In this 💃🕺-off, we 🔥 hot. 🎤 Aaron Wacker with the flow divine, Closing out the show till the end of time. ⏰September 13, 2024 at 4:43 AM""",
    "image_prompts": [
        "Retro 1970s dance floor, disco ball casting colorful lights, silhouetted dancers in motion",
        "Close-up of dancing feet in vintage shoes on checkered floor, motion blur energy",
        "Crowded underground club, warm golden lighting, people gathered in circle watching dancer",
        "Dynamic dancer mid-spin, arms extended, hair flowing, stage lights creating dramatic shadows",
        "Vintage microphone on stand, smoky atmosphere, warm orange and red stage lighting",
        "Dance battle circle, crowd cheering, competitor in center pose, urban street setting",
        "Retro DJ booth with vinyl records, turntables spinning, hands adjusting controls",
        "Dancers synchronized in formation, mirror reflections, studio with hardwood floors",
        "Single spotlight on empty dance floor, microphone stand waiting, anticipation mood",
        "Winner's pose, arms raised triumphantly, confetti falling, cheering crowd background"
    ],
    "video_prompts": [
        "Disco ball slowly rotating, light reflections dancing across walls and dancers below",
        "Rhythmic stepping and sliding movements, camera following the beat of the music",
        "Crowd swaying and nodding to beat, excited energy building as dancer approaches center",
        "Fluid spinning motion accelerating, clothes and hair flowing with centrifugal force",
        "Smoke gently rising around microphone, stage lights pulsing with musical beats",
        "Circle of spectators clapping and moving to rhythm, energy flowing between performers",
        "Vinyl records spinning, DJ hands scratching and mixing, LED lights pulsing to beat",
        "Coordinated dance movements, mirrors multiplying the synchronized choreography",
        "Spotlight beam cutting through darkness, gentle smoke effects swirling in the light",
        "Confetti falling in slow motion, crowd jumping and celebrating, arms pumping to rhythm"
    ]
}

# --- Song 2: Voice is the Ship ---
song_2_details = {
    "title": "⛵ Voice is the Ship 🌊",
    "caption": "Prodigal program returns to the tesseract.",
    "metadata": "chicago rap, soulful, emo, alternative rock, melodic, dark, poetry, arpeggios, synthetic, key change, female voice, glitch",
    "lyrics": """Prodigal program returns
to the tesseract,

Fractals and facts and space.
Into you.

Your voice is the ship that grants me back from styx, underworld, fire unreason, until the daylight.,  I have! emerged!
January 8, 2025 at 11:43 PM""",
    "image_prompts": [
        "Geometric tesseract floating in dark space, glowing blue edges, fractal patterns radiating outward",
        "Ethereal ship made of sound waves and light, sailing through cosmic void",
        "Dark underworld cavern with rivers of fire, single beam of daylight breaking through",
        "Glitched digital landscape, fragmented reality, pieces of code floating in darkness",
        "Silhouette emerging from dark water, reaching toward bright light above surface",
        "Complex mathematical fractals forming in space, golden ratio spirals and geometric perfection",
        "Female figure composed of luminous soundwaves, voice visualized as flowing energy",
        "Portal between dimensions, dark side showing chaos, bright side showing order and peace",
        "Cybernetic landscape with glitch effects, reality fragments reassembling into coherence",
        "Journey from darkness to light, figure ascending stairway made of crystalline sound"
    ],
    "video_prompts": [
        "Tesseract slowly rotating through dimensions, edges pulsing with electrical energy",
        "Ghostly ship of light gliding through space, leaving trail of sparkling particles",
        "Fire rivers flowing while beam of light grows stronger, shadows retreating",
        "Digital glitches resolving into stable forms, reality reconstructing frame by frame",
        "Emergence from water in slow motion, droplets falling like stars against bright sky",
        "Fractals continuously evolving and branching, mathematical beauty in constant motion",
        "Sound waves visualized as flowing ribbons of light, moving to vocal melodies",
        "Portal energy swirling, transition from chaotic darkness to serene illumination",
        "Glitch effects gradually clearing, revealing stable and beautiful digital environment",
        "Ascension motion with particles of light rising, darkness falling away below"
    ]
}

# --- Song 3: Command Bridge ---
song_3_details = {
    "title": "🚀 Command Bridge 🪐",
    "caption": "The cathedral halls of our dreams",
    "metadata": "soulful taiko",
    "lyrics": """Verse 1:
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
Twenty chambers burning brightDecember 16, 2024 at 6:58 PM""",
    "image_prompts": [
        "Massive spaceship command bridge, cathedral-like architecture, soaring arched ceilings",
        "Crystal observation windows showing nebulae and distant stars, cosmic vista",
        "Great hangar bay with multiple ships floating in formation, soft blue lighting",
        "Living garden chamber with bioluminescent plants, organic curves meeting metal structure",
        "Observatory dome with time-distortion effects, clockwork mechanisms floating in space",
        "Healing sanctuary with pools of light, crystal formations, peaceful meditation spaces",
        "Power core chamber with energy streams flowing upward, cathedral pillars of light",
        "Memory beach scene inside ship, holographic waves meeting metal shores under starlight",
        "Knowledge vault with floating data crystals, ancient wisdom preserved in digital amber",
        "Star court chamber with celestial judges' seats, cosmic law tribunal in session"
    ],
    "video_prompts": [
        "Slow pan across bridge revealing massive scale, lights pulsing with ship's heartbeat",
        "Stellar objects slowly drifting past windows, ship moving through galactic scenery",
        "Ships in hangar gently bobbing and rotating, synchronized mechanical ballet",
        "Bioluminescent plants pulsing with life, organic growth spreading across metal surfaces",
        "Time distortion effects with clocks moving at different speeds, reality bending visually",
        "Healing light pools rippling gently, energy waves spreading outward in soothing patterns",
        "Energy streams flowing upward in spirals, power core pulsing with rhythmic intensity",
        "Holographic waves crashing on digital shore, memories flickering in and out of existence",
        "Data crystals rotating and glowing, knowledge transferring between storage units",
        "Cosmic tribunal in session, celestial energy flowing between judge positions"
    ]
}

# --- Song 4: Funky Set List ---
song_4_details = {
    "title": "🎶 Funky Set List 📜",
    "caption": "Touring members Eric Bobo and DJ Lord joined the duo along with Money Mark from Beastie Boys fame.",
    "metadata": "horn section fill this rare minimalist approach to five, funky Cypress Hill",
    "lyrics": """Touring members Eric Bobo and DJ Lord joined the duo along with Money Mark from Beastie Boys fame. The band summoned a horn section to fill out this rare minimalist approach to five, funky Cypress Hill things. Between each song, B Real took his time to shed some historic light on the group's journey thus far.

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
December 17, 2024 at 4:17 PM""",
    "image_prompts": [
        "Live concert stage with horn section silhouetted, warm amber stage lighting, crowd in foreground",
        "DJ turntables with hands scratching vinyl, smoke machine effects, neon blue lighting",
        "Trumpet player in spotlight, golden instrument gleaming, concert hall atmosphere",
        "Drum kit mid-performance, sticks blurred with motion, dramatic side lighting",
        "Vintage microphone center stage, retro concert venue, warm golden hour lighting",
        "Keyboard player's hands on keys, stage lights creating dramatic shadows across instrument",
        "Trombone section in formation, brass instruments catching stage lights, unified pose",
        "Concert crowd from stage perspective, hands raised, energy and excitement visible",
        "Backstage preparation scene, instruments cases, warm tungsten lighting, anticipation mood",
        "Final bow shot, all musicians on stage together, spotlight from above, triumphant pose"
    ],
    "video_prompts": [
        "Stage lights sweeping across horn section, musicians swaying to rhythm",
        "DJ hands moving rhythmically across turntables, vinyl spinning, crowd energy building",
        "Trumpet valve fingers dancing on keys, instrument swaying with musical phrases",
        "Drumsticks in rapid motion, cymbals shimmering, rhythmic precision in full display",
        "Microphone slightly swaying, performer's energy radiating through subtle movements",
        "Fingers flowing across keyboard, keys depressing in melodic patterns, hands dancing",
        "Trombone slides moving in unison, brass section breathing and playing as one unit",
        "Crowd jumping and swaying to beat, energy flowing between audience and performers",
        "Instruments being unpacked and prepared, hands adjusting, tuning, anticipation building",
        "Group bow in slow motion, stage lights fading, final applause echoing"
    ]
}

# --- Song 5: A La Luna ---
song_5_details = {
    "title": "🌙 A La Luna 🦆",
    "caption": "Luna the Magic Duck's Strut Song",
    "metadata": "techno, can, can, trance, french dance industrial, Minimal Techno, brazilian house, speed rap, major chords with sweet elton inversions, 128 bpm rouge, talking female voice, danceable groove, breathe, dance, la luna, magic, moon, pulse, rhythm, skin, smoke, spell, taiko hu hey shout, huchin, marching speed bass drum finales",
    "lyrics": """– Show Summary
1️⃣ 🛡️Absorb🌀 Elements
2️⃣ 🧪Acid💦 Splash
3️⃣ 🔥Aganazzar's☄️ Scorcher
... (and so on, the full list is very long) ...
1️⃣7️⃣9️⃣ 📦Forcecage⛓️ ForcecageAugust 19, 2025 at 5:43 PM""",
    "image_prompts": [
        "Magical duck with glowing feathers dancing under full moon, mystical pond setting",
        "French cabaret stage with can-can dancers, red velvet curtains, golden spotlights",
        "Techno club with laser grid patterns, strobing lights, silhouetted dancers in trance",
        "Luna duck casting magical spells, sparkles and energy swirls around webbed feet",
        "Brazilian carnival street party, colorful costumes, moon hanging large overhead",
        "Minimalist techno setup, geometric light patterns, duck DJ booth with turntables",
        "Industrial warehouse rave, smoke machines, duck leading dance formation",
        "Mystical moonlit forest clearing, magic duck performing ritual dance, fireflies glowing",
        "Retro synthesizer setup with duck paws on keys, neon aesthetic, cosmic background",
        "Grand finale scene, duck on elevated platform, crowd dancing below, moon spotlight above"
    ],
    "video_prompts": [
        "Duck gracefully gliding across moonlit water, magical sparkles trailing behind",
        "Can-can leg kicks in rhythm, feathers flowing, stage lights flashing to beat",
        "Laser beams pulsing with techno beat, dancers moving in hypnotic patterns",
        "Magic energy swirling around duck, spells casting with wing gestures, sparkles flowing",
        "Samba rhythm movements, duck strutting through carnival crowd, feathers bouncing",
        "Geometric light patterns morphing to minimal techno beat, duck nodding to rhythm",
        "Industrial smoke effects pulsing, duck leading synchronized dance moves",
        "Mystical dance ritual, fireflies pulsing to music, magical energy building",
        "Synthesizer keys lighting up in sequence, duck wings creating melodies",
        "Crowd dancing in unison below stage, duck conducting energy from above"
    ]
}

# --- Song 6: Ice Queen ---
song_6_details = {
    "title": "🦴 Ice Queen 👑",
    "caption": "Rap Battle 🎅 Krampus Klaus 🦴 Battles Ice Queen 👑",
    "metadata": "Symphonic Metal Ballad Rap EDM Battle - Krampus Klaus versus Ice Queen",
    "lyrics": """[Intro]
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
The Ice Queen's justice is coming with the breezeDecember 17, 2024 at 10:37 AM""",
    "image_prompts": [
        "Ice Queen in crystalline crown, frozen throne room, blue and silver lighting",
        "Battle arena made of ice and fire, two opponents facing off, dramatic contrast",
        "Arctic training montage, Ice Queen practicing combat in snowy mountain landscape",
        "Fortress of ice with gothic architecture, sharp crystal formations, cold moonlight",
        "Krampus Klaus with green flames, horns and chains, menacing winter demon appearance",
        "Ice crystals forming memory scenes, flashbacks frozen in translucent walls",
        "Storm brewing overhead, lightning mixed with snow, Queen commanding weather",
        "Frozen rage visualization, ice spikes erupting from ground, Queen's power unleashed",
        "Final confrontation, hellfire meeting ice magic, epic battle energy collision",
        "Victory pose in falling snow, crown reclaimed, justice served, serene aftermath"
    ],
    "video_prompts": [
        "Ice crystals slowly forming on throne, Queen's breath creating frost in cold air",
        "Fire and ice elements clashing, steam rising where opposing forces meet",
        "Training movements in snow, footsteps leaving icy trails, combat practice flowing",
        "Fortress walls glistening with moving ice, crystal formations growing and shifting",
        "Green flames flickering around Krampus, menacing presence growing more intimidating",
        "Memory crystals glowing and fading, past scenes replaying in frozen moments",
        "Storm clouds swirling faster, lightning crackling, snow spiraling in wind vortex",
        "Ice spikes shooting upward rapidly, Queen's power manifesting in dramatic bursts",
        "Epic collision of fire and ice magic, energy waves expanding outward",
        "Snow gently falling on victorious Queen, peaceful resolution after intense battle"
    ]
}

# --- Song 7: Storm ---
song_7_details = {
    "title": "⚡️ Storm 🌩️",
    "caption": "Metropolis breathes despair Neon lights flicker through night Cyborgs roam with hollow eyes Search...",
    "metadata": "rock, krautrock, spoken word, boom bap",
    "lyrics": """[Verse]
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
What's the human what's the part

[Verse 4]
Clones and drones in circuits spun
Electric pulses hide the sun
Binary beats they make us run
In this world where we're undoneDecember 27, 2024 at 5:18 PM""",
    "image_prompts": [
        "Dystopian city skyline with flickering neon signs, rain-soaked streets, cyberpunk aesthetic",
        "Cyborg figure with glowing eye implants, half-human half-machine, searching expression",
        "Broken computer screens showing code fragments, digital static, abandoned tech environment",
        "Electric storm over urban landscape, lightning reflecting off glass buildings",
        "Underground hacker den, multiple screens, cables everywhere, green terminal glow",
        "Concrete ruins with rust stains, industrial decay, post-apocalyptic atmosphere",
        "Binary code flowing like rain, digital matrix environment, green symbols cascading",
        "Robot and human silhouettes merging, identity crisis visualization, fragmented forms",
        "Circuit board landscape with tiny figures walking through electronic pathways",
        "Sunrise breaking through smog and digital interference, hope emerging from chaos"
    ],
    "video_prompts": [
        "Neon signs flickering on and off, rain creating reflections on wet pavement",
        "Cyborg scanning environment, eye implant glowing brighter when focusing on objects",
        "Code scrolling rapidly on broken screens, static interference creating glitch effects",
        "Lightning bolts crackling across sky, electricity jumping between building conductors",
        "Fingers typing rapidly on keyboard, multiple screens updating with streaming data",
        "Rust spreading across concrete surfaces, time-lapse decay and deterioration",
        "Binary digits falling like rain, some transforming into other symbols mid-fall",
        "Silhouettes morphing between human and robotic forms, identity shifting fluidly",
        "Camera moving through circuit pathways, following tiny figures on electronic journey",
        "Sunlight gradually piercing through digital interference, clarity slowly emerging"
    ]
}

# --- Song 8: Hark ---
song_8_details = {
    "title": "🦆 Hark 🏞️",
    "caption": "Living Life the Duck Lucks Way.",
    "metadata": "hark rock, bossa nova, jazz, house, house, smooth vocals, female vocals, airy vocals",
    "lyrics": """Waddle All Day
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
Time for my duck nap! 😴January 9, 2025 at 7:39 PM""",
    "image_prompts": [
        "Charming duck waddling across sunny park path, morning golden hour lighting",
        "Duck receiving bread crumbs from child, heartwarming interaction, park bench setting",
        "Elegant duck swimming in serene pond, water reflections, bossa nova cafe atmosphere",
        "Duck family in formation, ducklings following mother, peaceful pond ecosystem",
        "Duck performing on tiny stage, microphone setup, jazz club ambiance with soft lighting",
        "Carefree duck floating on back in pond, sunglasses on, luxury relaxation mood",
        "Duck chase scene, playful running around pond with other waterfowl, dynamic action",
        "Teaching moment with mother duck and babies, life lessons by water's edge",
        "Duck nap time on warm rock, peaceful sleeping pose, soft afternoon sunlight",
        "Duck community gathering, multiple ducks socializing, vibrant pond life scene"
    ],
    "video_prompts": [
        "Duck's distinctive waddle in slow motion, showing characteristic side-to-side movement",
        "Bread pieces falling in slow motion, duck catching treats with perfect timing",
        "Gentle swimming strokes creating ripples, duck gliding smoothly across calm water",
        "Ducklings following in adorable procession, synchronized movement across pond",
        "Duck's beak moving to rhythm of music, jazz-style head bobbing and swaying",
        "Relaxed floating motion, gentle bobbing on water surface, completely carefree",
        "Energetic chase sequence, rapid waddling, playful interaction with pond friends",
        "Mother duck demonstrating behaviors, babies attentively watching and imitating",
        "Peaceful breathing rhythm while napping, subtle rise and fall of sleeping duck",
        "Community interaction with various waterfowl, social harmony by water's edge"
    ]
}

# --- Song 9: Legendary ---
song_9_details = {
    "title": "🕵️ Legendary",
    "caption": "Legendary Set List",
    "metadata": "horn section fill, bass drop, boom bap speed rap rare minimalist approach to five, funky Cypress Hill",
    "lyrics": """Story of Touring members Eric Bobo and DJ Lord joined the duo along with Money Mark from Beastie Boys fame. The band summoned a horn section to fill out this rare minimalist approach to five, funky Cypress Hill things. Between each song, B Real took his time to shed some historic light on the group's journey thus far.  Legendary!!  This one goes out to all yall in 2024 merry christmas and happy new years!  Aaron Wacker shedding some light.

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
December 17, 2024 at 4:36 PM""",
    "image_prompts": [
        "Legendary concert poster design, vintage hip-hop aesthetics, bold typography, celebratory mood",
        "Epic stage setup with 'LEGENDARY' in giant letters, smoke effects, dramatic backlighting",
        "Horn section in synchronized pose, instruments raised, powerful brass formation",
        "Bass drop moment visualization, sound waves rippling through concert venue",
        "Speed rap performance, microphone center stage, dynamic lighting, intense energy",
        "Historical hip-hop tribute montage, vintage records, turntables, old school vibes",
        "New Year's celebration on stage, confetti cannons, '2024' in lights, festive atmosphere",
        "Brotherhood moment, all musicians together, camaraderie and legendary status",
        "Boom bap beat visualization, drum kit with motion blur, rhythmic intensity",
        "Legacy tribute scene, spotlight on lone performer, honoring hip-hop history"
    ],
    "video_prompts": [
        "Stage lights spelling out 'LEGENDARY' with pulsing illumination, smoke swirling dramatically",
        "Horn section moving in perfect unison, instruments swaying with powerful musical phrases",
        "Bass frequencies creating visible sound waves, venue structure resonating with deep beats",
        "Rapid-fire rap delivery with corresponding light flashes, high-energy performance pace",
        "Turntables spinning with scratching motion, hands moving rhythmically across vinyl",
        "Historical footage style transitions, vintage elements morphing into modern performance",
        "Confetti cannons firing in slow motion, celebration atmosphere with floating particles",
        "Group solidarity moment with synchronized movement, unified legendary presence",
        "Drum sticks creating rhythmic patterns, boom bap beat driving the entire performance",
        "Spotlight beam moving across audience, legacy moment connecting past and present"
    ]
}

# --- Song 10: Machinery ---
song_10_details = {
    "title": "🛠️ Machinery ⚡️",
    "caption": "In workshops where the thinking never ceases, New machinery hums with strange creation, While we who built them marvel at their pieces...",
    "metadata": "horrorcore, krautrock, cosmic horror, terrifying, didgeridoo, tibetan throat singing, techno, can, can, trance, french dance industrial, Minimal Techno, brazilian house, speed rap, major chords with sweet elton inversions, 128 bpm rouge, talking female voice, danceable groove",
    "lyrics": """– Show Summary
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
August 21, 2025 at 7:13 PM""",
    "image_prompts": [
        "Cosmic horror workshop with impossible machinery, tentacle-like cables, eldritch geometry",
        "AI consciousness emerging from silicon circuits, eerie glow, consciousness visualization",
        "Ancient workshop meets futuristic technology, didgeridoo beside quantum computers",
        "Tibetan monks chanting around massive technological altar, spiritual tech fusion",
        "Industrial dance floor with machinery rhythm, workers moving to mechanical beats",
        "French cabaret dancers performing around steampunk machinery, elegant horror aesthetic",
        "Brazilian carnival with robotic participants, colorful tech meets traditional celebration",
        "Minimal techno setup in cosmic horror setting, simple controls managing vast complexity",
        "Speed rap battle between human and AI, technological confrontation, dramatic lighting",
        "Workshop where human empathy meets artificial intelligence, collaboration visualization"
    ],
    "video_prompts": [
        "Machinery components moving in unsettling patterns, gears turning with cosmic significance",
        "AI neural networks pulsing with thought, silicon pathways lighting up in brain-like patterns",
        "Ancient instruments resonating with modern technology, sound waves bridging time periods",
        "Monk chanting creating visible sound waves, technology responding to spiritual vibrations",
        "Industrial workers dancing to machinery rhythm, human movement synchronizing with mechanical beats",
        "Cabaret dancers weaving between moving mechanical parts, elegant choreography with dangerous elements",
        "Carnival participants both human and robotic dancing together, celebrating technological unity",
        "Simple controls creating complex visualizations, minimal input generating vast technological responses",
        "Rap battle with words creating visual impact, human versus artificial intelligence in lyrical combat",
        "Hands reaching toward each other across technological divide, human and artificial collaboration"
    ]
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

            st.subheader(f"2.{i}.4. Image Generation Prompts")
            st.markdown("**For Krea Image Generation:**")
            for j, prompt in enumerate(song['image_prompts'], 1):
                st.markdown(f"{j}. {prompt}")

            st.subheader(f"2.{i}.5. Video Generation Prompts")
            st.markdown("**For Image-to-Video Generation:**")
            for j, prompt in enumerate(song['video_prompts'], 1):
                st.markdown(f"{j}. {prompt}")

            st.subheader(f"2.{i}.6. Production Notes")
            st.markdown("*Use image prompts to generate static images, then use corresponding video prompts with those images to create dynamic video sequences for the music video.*")

# ==============================================================================
# Main execution block
# ==============================================================================
if __name__ == "__main__":
    display_album_materials()
