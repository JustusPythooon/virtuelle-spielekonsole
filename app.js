let coins=Number(localStorage.getItem('coins'))||100;
let avatarStored=localStorage.getItem('avatar')||'🤖';
let themeStored=localStorage.getItem('theme')||'#1a1e3f';

document.addEventListener('DOMContentLoaded',()=>{
 coinDisplay.innerText=coins;
 avatar.innerText=avatarStored;
 document.documentElement.style.setProperty('--bg',themeStored);
});

async function init(){let py=await loadPyodide();await py.runPythonAsync(await (await fetch('main.py')).text());window.py=py;}
init();

function boot(){setTimeout(()=>{boot-screen.hidden=true;main-ui.hidden=false;menu.hidden=false},600)}
function openApp(a){app-view.innerHTML=py.runPython(`console.open_app('${a}')`)}
function setAvatar(a){avatarStored=a;avatar.innerText=a;localStorage.setItem('avatar',a)}
function setTheme(t){themeStored=t;document.documentElement.style.setProperty('--bg',t);localStorage.setItem('theme',t)}
function addCoins(c){coins+=c;coinDisplay.innerText=coins;localStorage.setItem('coins',coins)}
setInterval(()=>time.innerText=new Date().toLocaleTimeString('de-DE'),1000);