import * as THREE from 'https://cdn.skypack.dev/pin/three@v0.137.4-DAqQNeDi0quLokNUIO1Y/mode=imports/optimized/three.js';

let camera, light, scene, spaceTexture, renderer;
let geometry, material, mesh, torus;

init();
document.body.onscroll = moveCamera;
moveCamera();

function init() {
    // Camera
    camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 0.01, 10 );
    camera.position.z = 1;
    camera.lookAt(0, 0, 0);

    // Scene
    scene = new THREE.Scene();

    // Torus
    geometry = new THREE.TorusGeometry( 10, 3, 16, 100 );
    material = new THREE.MeshStandardMaterial( { color: 0xfffffff } );
    torus = new THREE.Mesh( geometry, material );
    torus.position.set(0, 0, 0)
    scene.add( torus );

    // Light
    light = new THREE.HemisphereLight( 0xffffff, 10, 1 );
    light.position.set(-40, 40, -40);
    scene.add(light);

    // Add Stars
    Array(200).fill().forEach(addStar);

    // Load BG texture
    spaceTexture = new THREE.TextureLoader().load('space.jpg');
    scene.background = spaceTexture;

    // Renderer
    renderer = new THREE.WebGLRenderer( { antialias: true, canvas: document.querySelector('#bg'),} );

    renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.setAnimationLoop( animation );
    document.body.appendChild( renderer.domElement );

}

function addStar() {
	const geometry = new THREE.SphereGeometry(0.25, 24, 24);
	const material = new THREE.MeshStandardMaterial({ color: 0xffffff });
	const star = new THREE.Mesh(geometry, material);
  
	const [x, y, z] = Array(3)
	  .fill()
	  .map(() => THREE.MathUtils.randFloatSpread(100));
  
	star.position.set(x, y, z);
	scene.add(star);
}

function animation( time ) {
    torus.rotation.x += 0.01;
	torus.rotation.y += 0.01;
    renderer.render( scene, camera );
}

function moveCamera() {
	let t = document.body.getBoundingClientRect().top;
	console.log(t);
	camera.position.z = 25 + t * -0.01;
	// camera.position.y = t * -0.002;
	// camera.rotation.y = t * -0.0001;
}