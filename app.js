let pyodide,ready=false;
let coins=localStorage.getItem('coins')||100;
let owned=JSON.parse(localStorage.getItem('owned')||'[]');
let avatarStored=localStorage.getItem('avatar')||'🤖';
document.addEventListener('DOMContentLoaded',()=>{coinDisplay.innerText=coins;avatar.innerText=avatarStored});

async function init(){pyodide=await loadPyodide();await pyodide.runPythonAsync(await (await fetch('main.py')).text());ready=true;}init();

function boot(){const ctx=new AudioContext();const o=ctx.createOscillator();o.frequency.value=220;o.connect(ctx.destination);o.start();setTimeout(()=>{o.stop();document.getElementById('boot-screen').hidden=true;document.getElementById('main-ui').hidden=false;menu.hidden=false},600)}

function openApp(app){if(!ready)return;let res=pyodide.runPython(`console.open_app('${app}', ${coins}, ${JSON.stringify(owned)})`);document.getElementById('app-view').innerHTML=res;}
function setAvatar(e){avatarStored=e;avatar.innerText=e;localStorage.setItem('avatar',e)}
function setTheme(c){document.documentElement.style.setProperty('--bg',c)}
function buy(){if(coins<100)return alert('Nicht genug Coins');coins-=100;owned.push('kart');save();openApp('games')}
function save(){localStorage.setItem('coins',coins);localStorage.setItem('owned',JSON.stringify(owned));coinDisplay.innerText=coins}
function unlock(){coins+=50;save();alert('🏆 Erfolg freigeschaltet: +50 Coins')}
setInterval(()=>time.innerText=new Date().toLocaleTimeString('de-DE'),1000);