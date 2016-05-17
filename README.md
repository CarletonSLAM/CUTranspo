# CUTranspo
**An Entry to SLAM HACKS**

An LED board that will display timings for the next 2 routes for every bus at the main bus stop at Carleton University.

## Inspiration
Waiting for buses is a pain without knowing when they will show up.

## What it does
Displays the next 2 timings for the bus routes at the main Carleton University bus stop.

The production server hosted on https://cu-transpo.herokuapp.com uses the OC Transpo API to pass the times that a bus with come to a particular bus top. The bus stop is given when registering the device.

Visit https://vimeo.com/166373294 for our demo video.

#### Registerting Device:
 ..* POST https://cu-transpo.herokuapp.com/api/Devices  
 ..* body {deviceName:'device', 'stopNo':1234, password: 'pw'}


#### Login Device:
..* POST https://cu-transpo.herokuapp.com/api/Devices/login
..* body {deviceName:'device', password: 'pw'}

#### Getting Bus Times:
  ..* GET https://cu-transpo.herokuapp.com/api/Devices/getTimes

## How we built it
Node.js for the server, Python for the client, OC Transpo API to pull in information about the next 2 timings for each bus, adapted some guy’s API to output text onto the LED board.

## Challenges we ran into
* Being able to connect to the Raspberry Pi on a local network.
* Call bash commands in Python as a subprocess.

## Accomplishments
* Getting internet on the Raspberry Pi without having internet.
* Displaying readable text onto the LED board.
* Effectively parsing JSON and XML data from the OC Transpo API.
* Also proud of the awesome team name.

## What we learned
How to use the OC Transpo API, Node.js, and how to send text to display on the LED board. How to get internet without internet to the Raspberry Pi.

## What's next for CUTranspo
* Scale server to efficiently pass data to all devices
* Use a co-processor to control the
* Larger LED board to display more bus routes and timings at the same time.
* Add solar power with a battery inside a small footprint plastic enclosure.
* Install at the Carleton bus stops.
