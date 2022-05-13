try {if (acceuil[1] === "disable") {title = "Accueil"}} catch (e) {acceuil = ["index.html", "enable"]}    
try {if (themes[1] === "disable") {title = "Thèmes"}} catch (e) {themes = ["themes.html", "enable"]}    
try {if (animaux[1] === "disable") {title = "Zoo des Animaux"}} catch (e) {animaux = ["animaux.html", "enable"]}  
try {if (tierlist[1] === "disable") {title = "TierList"}} catch (e) {tierlist = ["tierlist.html", "enable"]}

document.write(`
<link rel="stylesheet" href="css/navigation.css" />
<section id="top-bar">
    <h1>NSI - ` + title + `</h1>
    <ul id="menu">
        <a href="` + acceuil[0] + `" class="` + acceuil[1] + ` accueil">
            <li>Accueil</li>
        </a>
        <a href="` + themes[0] + `" class="` + themes[1] + ` themes">
            <li>Thèmes</li>
        </a>
        <a href="` + animaux[0] + `" class="` + animaux[1] + ` animaux"> 
            <li>Animaux</li> 
        </a>
        <a href="` + tierlist[0] + `" class="` + tierlist[1] + ` tierlist"> 
            <li>Tierlist</li> 
        </a>
        <button id="menuButton" onclick="showMenu()">Tout voir</button>
    </ul>
</section>
<div id="menuDiv">
<div class="grid">
    <a href="` + acceuil[0] + `">
        <div class="` + acceuil[1] + ` accueil">
            <img src="images/web-dev.png" alt="" />
            <h2>Acceuil</h2>
            <h1>Introduction</h1>
        </div>
    </a>
    <a href="` + themes[0] + `">
        <div class="` + themes[1] + ` themes">
            <img src="images/binaire.png" alt="" />
            <h2>Thèmes</h2>
            <h1>Thèmes de NSI</h1>
        </div>
    </a>
    <a href="` + animaux[0] + `">
        <div class="` + animaux[1] + ` animaux">
            <img src="images/algobox-dev.png" alt="" />
            <h2>Animaux</h2>
            <h1>Promenade avec les animaux</h1>
        </div>
    </a>
    <a href="https://youtu.be/dQw4w9WgXcQ">
        <div class="` + animaux[1] + ` animaux"">
            <img src="images/python-logo.jpg" alt="" />
            <h2>Youtube</h2>
            <h1>Never Gonna Give You Up</h1>
        </div>
    </a>
</div>
</div>
`);