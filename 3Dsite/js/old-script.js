import * as THREE from 'https://cdn.skypack.dev/pin/three@v0.137.4-DAqQNeDi0quLokNUIO1Y/mode=imports/optimized/three.js';

const scene = new THREE.Scene();

const renderer = new THREE.WebGLRenderer({
	canvas: document.querySelector('#bg'),
  });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 500);
// camera.position.set(-50, 0, 0);
camera.lookAt(0, 0, 0);

const geometry = new THREE.TorusGeometry( 10, 3, 16, 100 );
const material = new THREE.MeshStandardMaterial( { color: 0xfffffff } );
const torus = new THREE.Mesh( geometry, material );
torus.position.set(0, 0, 0)
scene.add( torus );

const light = new THREE.HemisphereLight( 0xffffff, 10, 1 );
light.position.set(-40, 40, -40);
scene.add(light);

// Load background texture
const spaceTexture = new THREE.TextureLoader().load('space.jpg');
scene.background = spaceTexture;
