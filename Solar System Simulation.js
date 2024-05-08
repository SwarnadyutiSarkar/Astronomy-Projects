<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Solar System Simulation</title>
<style>
    body {
        margin: 0;
        overflow: hidden;
    }
    canvas {
        display: block;
    }
</style>
</head>
<body>
<canvas id="canvas"></canvas>
<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const sun = { x: canvas.width / 2, y: canvas.height / 2, radius: 30, color: 'yellow' };
    const planets = [
        { name: 'Mercury', distance: 50, radius: 5, color: 'gray', speed: 0.05 },
        { name: 'Venus', distance: 80, radius: 10, color: 'orange', speed: 0.03 },
        { name: 'Earth', distance: 110, radius: 12, color: 'blue', speed: 0.02 },
        { name: 'Mars', distance: 150, radius: 8, color: 'red', speed: 0.015 },
        { name: 'Jupiter', distance: 200, radius: 20, color: 'brown', speed: 0.01 },
        { name: 'Saturn', distance: 250, radius: 18, color: 'goldenrod', speed: 0.008 },
        { name: 'Uranus', distance: 290, radius: 15, color: 'lightblue', speed: 0.006 },
        { name: 'Neptune', distance: 330, radius: 14, color: 'blue', speed: 0.004 }
    ];

    function drawPlanet(planet, angle) {
        const x = sun.x + planet.distance * Math.cos(angle);
        const y = sun.y + planet.distance * Math.sin(angle);
        ctx.beginPath();
        ctx.fillStyle = planet.color;
        ctx.arc(x, y, planet.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // Draw Sun
        ctx.beginPath();
        ctx.fillStyle = sun.color;
        ctx.arc(sun.x, sun.y, sun.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();
        // Draw Planets
        planets.forEach((planet, index) => {
            const angle = planet.speed * Date.now() / 1000;
            drawPlanet(planet, angle);
        });
        requestAnimationFrame(draw);
    }

    draw();
</script>
</body>
</html>
