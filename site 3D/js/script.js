const scene = new THREE.Scene();

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 1, 500 );
camera.position.set( 0, 50, 5 );
camera.lookAt( 0, 0, 0 );

const geometry = new THREE.TorusGeometry( 10, 3, 16, 100 );
const material = new THREE.MeshStandardMaterial( { color: 0xfffffff } );
const cube = new THREE.Mesh( geometry, material );
scene.add( cube );

const light = new THREE.HemisphereLight( 0xffffbb, 0x080820, 1 );
light.position.set( -40, 40, -40 );
scene.add( light );

//Load background texture
const loader = new THREE.TextureLoader();
loader.load('https://images.pexels.com/photos/1205301/pexels-photo-1205301.jpeg', function(texture){ scene.background = texture; });


function animate() {
	requestAnimationFrame( animate );
	cube.rotation.x += 0.01;
	cube.rotation.y += 0.01;
	renderer.render( scene, camera );
};

animate();
