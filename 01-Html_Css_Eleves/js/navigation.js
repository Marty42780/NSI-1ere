if (docname === "index") {acceuilLink = '#'} else {acceuilLink = '../index.html'}
if (docname === "index") {acceuilLink = 'themes/'} else {acceuilLink = 'index.html'}


document.write(`
<section id="top-bar">
    <h1>NSI - Acceuil</h1>
    <ul id="menu">
        <a href="` + acceuilLink + `" target="_parent" class="` + class0 + ` zero">
            <li>Accueil</li>
        </a>
        <a href="` + themeLink + `" class="` + class1 + ` one">
            <li>Theme 1</li>
        </a>
        <a href="themes/theme2.html" class="enable two"> 
            <li>Theme 2</li> 
        </a>
        <a href="themes/theme3.html" class="enable three">
            <li>Theme 3</li>
        </a>
        <a href="https://youtu.be/dQw4w9WgXcQ" class="enable four">
            <li>Theme 4</li>
        </a>
        <a href="themes/animaux.html" class="enable five">
            <li>Theme 5</li>
        </a>
        <a href="themes/tierlist.html" class="enable six">
            <li>Theme 6</li>
        </a>
        <button id="menuButton" onclick="showMenu()">Tout voir</button>
    </ul>
</section>
<div id="menuDiv">
<div class="grid">
    <a href="themes/theme1.html">
        <div class="theme1">
            <img src="images/web-dev.png" alt="" />
            <h2>Thème 1</h2>
            <h1>Développement Web</h1>bju,
        </div>
    </a>
    <a href="themes/theme2.html">
        <div class="theme2">
            <img src="images/binaire.png" alt="" />
            <h2>Thème 2</h2>
            <h1>Binaire et Hexadécimal</h1>
        </div>
    </a>
    <a href="themes/theme3.html">
        <div class="theme3">
            <img src="images/algobox-dev.png" alt="" />
            <h2>Thème 3</h2>
            <h1>Algorithmique alogobox</h1>
        </div>
    </a>
    <a href="https://youtu.be/dQw4w9WgXcQ">
        <div class="theme4">
            <img src="images/python-logo.jpg" alt="" />
            <h2>Thème 4</h2>
            <h1>Introduction Python</h1>
        </div>
    </a>
    <a href="themes/animaux.html">
        <div class="theme5">
            <img src="images/lezard.jpg" alt="">
            <h2>Thème 5</h2>
            <h1>Promenade avec les animaux</h1>
        </div>
    </a>
</div>
</div>
`);