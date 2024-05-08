<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Astrophysical Data Visualization</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>
<body>
    <script>
        // Setup scene
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Add objects to scene
        const geometry = new THREE.SphereGeometry(1, 32, 32);
        const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
        const sun = new THREE.Mesh(geometry, material);
        scene.add(sun);

        const earth = new THREE.Mesh(geometry, new THREE.MeshBasicMaterial({ color: 0x0000ff }));
        earth.position.x = 5;
        scene.add(earth);

        const mars = new THREE.Mesh(geometry, new THREE.MeshBasicMaterial({ color: 0xffa500 }));
        mars.position.x = -7;
        scene.add(mars);

        // Set camera position
        camera.position.z = 10;

        // Render loop
        function animate() {
            requestAnimationFrame(animate);
            sun.rotation.y += 0.01;
            earth.rotation.y += 0.02;
            mars.rotation.y += 0.03;
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>
