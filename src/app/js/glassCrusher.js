let camera, scene, renderer, cube;

init();

function init() {

  camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 0.01, 10);
  camera.position.z = 4;

  scene = new THREE.Scene();

  const piece = new THREE.BoxGeometry(1, 1, 1).toNonIndexed();
  const material = new THREE.MeshBasicMaterial({
    vertexColors: true
  });
  const positionAttribute = piece.getAttribute('position');
  var colors = [];
  var colorsTemp = [];

  var color = new THREE.Color();

  var color = new THREE.Color(1, 0, 0);
  colorsTemp.push(color);

  var color = new THREE.Color(0, 1, 0);
  colorsTemp.push(color);

  var color = new THREE.Color(0, 0, 1);
  colorsTemp.push(color);

  var color = new THREE.Color(1, 0, 1);
  colorsTemp.push(color);

  var color = new THREE.Color(1, 1, 1);
  colorsTemp.push(color);

  var color = new THREE.Color(1, 1, 0);
  colorsTemp.push(color);

  var color = new THREE.Color(1, 1, 1);
  colorsTemp.push(color);

  // specific chosen colors
  for (let i = 0; i < positionAttribute.count; i += 6) {

    color = colorsTemp[((i+6)/6)-1];

    colors.push(color.r, color.g, color.b);
    colors.push(color.r, color.g, color.b);
    colors.push(color.r, color.g, color.b);

    colors.push(color.r, color.g, color.b);
    colors.push(color.r, color.g, color.b);
    colors.push(color.r, color.g, color.b);
  }
  
  // random colors
  /*
  for (let i = 0; i < positionAttribute.count; i += 6) {

    color.setHex(0xffffff * Math.random());

    colors.push(color.r, color.g, color.b);
    colors.push(color.r, color.g, color.b);
    colors.push(color.r, color.g, color.b);

    colors.push(color.r, color.g, color.b);
    colors.push(color.r, color.g, color.b);
    colors.push(color.r, color.g, color.b);
  }
  */

  // define the new attribute
  piece.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));

  cube = new THREE.Mesh(piece, material);
  scene.add(cube);

  renderer = new THREE.WebGLRenderer({
    antialias: true
  });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setAnimationLoop(animation);
  document.body.appendChild(renderer.domElement);

}

function animation(time) {

  cube.rotation.x = time / 2000;
  cube.rotation.y = time / 1000;

  renderer.render(scene, camera);

}



