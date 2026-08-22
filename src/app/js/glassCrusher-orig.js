const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.BoxGeometry( 10, 1, 1 );
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const arm = new THREE.Mesh( geometry, material );
scene.add( arm );

camera.position.z = 5;
camera.position.x = 4;
camera.rotation.x = 0.1;
camera.rotation.y = 0.1;
arm.position.x = 5;

function animate() {
    requestAnimationFrame( animate );

    arm.rotation.x += 0.01;
    arm.rotation.y += 0.01;

    renderer.render( scene, camera );
};

animate();