acceuil = ["#", "disable"]
theme1 = ["themes/theme1.html", "enable"]
theme2 = ["themes/theme2.html", "enable"]
theme3 = ["themes/theme3.html", "enable"]
theme4 = ["themes/https://youtu.be/dQw4w9WgXcQ", "enable"]
theme5 = ["themes/animaux.html", "enable"]
theme6 = ["themes/tierlist.html", "enable"]

document.write(`
<section id="top-bar">
    <h1>NSI - Acceuil</h1>
    <ul id="menu">
        <a href="` + acceuil[0] + `" target="_parent" class="` + acceuil[1] + ` zero">
            <li>Accueil</li>
        </a>
        <a href="` + theme1[0] + `" class="` + theme1[1] + ` one">
            <li>Theme 1</li>
        </a>
        <a href="` + theme2[0] + `" class="` + theme2[1] + ` two"> 
            <li>Theme 2</li> 
        </a>
        <a href="` + theme3[0] + `" class="` + theme3[1] + ` three">
            <li>Theme 3</li>
        </a>
        <a href="` + theme4[0] + `" class="` + theme4[1] + ` four">
            <li>Theme 4</li>
        </a>
        <a href="` + theme5[0] + `" class="` + theme5[1] + ` five">
            <li>Theme 5</li>
        </a>
        <a href="` + theme6[0] + `" class="` + theme6[1] + ` six">
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