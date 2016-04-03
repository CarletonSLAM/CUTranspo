# CUTranspo

SLAM HACKS - CUTranspo

An LED board that will display timings for the next 3 routes for every bus at the main bus stop at Carleton University.

Inspiration
Waiting for buses is a pain without knowing when they will show up.
What it does


How we built it
Node.js for the server, Python for the client, OC Transpo API to pull in information about the next 3 timings for each bus, adapted some guy’s API to output text onto the LED board.

Challenges we ran into
Being able to connect to the Raspberry Pi on a local network. Call bash commands in Python as a subprocess.

Accomplishments that I'm proud of


What we learned
How to use the OC Transpo API, Node.js, and how to send text to display on the LED board. How to get internet without internet to the Raspberry Pi.

What's next for CUTranspo
Scale to all bus stops and larger LED board to display more bus routes and timings at the same time. Add solar power with a battery inside a small footprint plastic enclosure. Install at the Carleton bus stops.

