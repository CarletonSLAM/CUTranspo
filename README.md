# CUTranspo

<h1>SLAM HACKS - CUTranspo<h1>

An LED board that will display timings for the next 2 routes for every bus at the main bus stop at Carleton University.

<h3>Inspiration</h3>

Waiting for buses is a pain without knowing when they will show up.

<h3>What it does</h3>

Displays the next 2 timings for the bus routes at the main Carleton University bus stop.

<h3>How we built it</h3>

Node.js for the server, Python for the client, OC Transpo API to pull in information about the next 2 timings for each bus, adapted some guy’s API to output text onto the LED board.

<h3>Challenges we ran into</h3>

Being able to connect to the Raspberry Pi on a local network. Call bash commands in Python as a subprocess.

<h3>Accomplishments that I'm proud of</h3>

Getting internet on the Raspberry Pi without having internet. Displaying readable text onto the LED board. Effectively parsing JSON and XML data from the OC Transpo API. Also proud of the awesome team name.

<h3>What we learned</h3>

How to use the OC Transpo API, Node.js, and how to send text to display on the LED board. How to get internet without internet to the Raspberry Pi.

<h3>What's next for CUTranspo,</h3>

Scale to all bus stops and larger LED board to display more bus routes and timings at the same time. Add solar power with a battery inside a small footprint plastic enclosure. Install at the Carleton bus stops.
