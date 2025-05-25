- Looking at /js/script.js, we find a list of targetPositions
```
targetPositions = [{ x: 367, y: 238, colorHue: 0 }, { x: 412, y: 293, colorHue: 40 }, { x: 291, y: 314, colorHue: 60 }, { x: 392, y: 362, colorHue: 120 }, { x: 454, y: 319, colorHue: 240 }, { x: 349, y: 252, colorHue: 280 }, { x: 433, y: 301, colorHue: 320 }]
```
- We also see a function `retrieveFlag()`, that checks given particle positions and retrieves the flag through an api call to `/api/verify-ctf-solution`
- So we just send a POST request to the endpoint with the `targetPositions` data, and we get the flag : `flag{6ff0c72ad11bf174139e970559d9b5d2}`