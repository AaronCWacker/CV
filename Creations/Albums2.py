help me compose for each song a set of ten image prompts which will allow me to generate images then videos for the music videos (10).  For each song I need about ten solid artistic prompts which have scenes to match the songs individually.  I plan to use Krea and prompt limit is about the size of song one per prompt.  I think too we can have an image gen set and a video set which is same scene, just text image prompt that together with image it creates the perfect video for the image and pormpt text where video might have tips on the motion in the video prompt.  Amend all content into my app as data inline within code.  So for each song I would get ten short image prompts, ten short image to video prompts and these will match my lyrics data for same song:  import streamlit as st



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

"""

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



Your voice is the ship that grants me back from styx, underworld, fire unreason, until the daylight.,  I have! emerged!

January 8, 2025 at 11:43 PM

"""

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

"""

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

"""

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

"""

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

"""

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

"""

}



# --- Song 8: Hark ---

song_8_details = {

    "title": "🦆 Hark 🏞️",

    "caption": "Living Life the Duck Lucks Way.",

    "metadata": "hark rock, bossa nova, jazz, house, house, smooth vocals, female vocals, airy vocals",

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

"""

}



# --- Song 9: Legendary ---

song_9_details = {

    "title": "🕵️ Legendary",

    "caption": "Legendary Set List",

    "metadata": "horn section fill, bass drop, boom bap speed rap rare minimalist approach to five, funky Cypress Hill",

    "lyrics": """

Story of Touring members Eric Bobo and DJ Lord joined the duo along with Money Mark from Beastie Boys fame. The band summoned a horn section to fill out this rare minimalist approach to five, funky Cypress Hill things. Between each song, B Real took his time to shed some historic light on the group's journey thus far.  Legendary!!  This one goes out to all yall in 2024 merry christmas and happy new years!  Aaron Wacker shedding some light.



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

"""

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

"""

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

            st.text_area("Lyrics", song['lyrics'], height=300)



            st.subheader(f"2.{i}.4. Video Production Assets")

            st.markdown("*(This is where you will track image gen, video gen, and composite assets)*")

            # You can add file uploaders or text inputs here later

            # e.g., st.file_uploader(f"Upload Image for Lyric Line 1", key=f"img_{i}_1")

            # e.g., st.text_input("Video Scene Description", key=f"vid_desc_{i}_1")





# ==============================================================================

# Main execution block

# ==============================================================================

if __name__ == "__main__":

    display_album_materials()

