class VirtualConsole:
 def open_app(self,app):
  if app=='settings':
   return '''<h2>⚙️ Einstellungen</h2>
   <button onclick="setTheme('#1a1e3f')">Blau</button>
   <button onclick="setTheme('#2b1a1a')">Rot</button>
   <button onclick="setTheme('#1a2b1a')">Grün</button>'''

  if app=='games':
   return '''<h2>🎮 Kart Racer</h2>
   <p>Strecke auswählen:</p>
   <button onclick="startGame(1)">Wüste</button>
   <button onclick="startGame(2)">Stadt</button>
   <canvas id='game' width='520' height='320'></canvas>
   <script>
   let ctx=game.getContext('2d');
   let player={x:240,y:260,speed:5,shield:false};
   let enemies=[{x:80,y:80,s:2},{x:220,y:120,s:3},{x:380,y:60,s:4}];
   let paused=false;
   let turbo=0;

   function startGame(t){player.speed= t==2?7:5;}

   document.onkeydown=e=>{
    if(e.key==='ArrowLeft')player.x-=player.speed;
    if(e.key==='ArrowRight')player.x+=player.speed;
    if(e.key==='t')turbo=100;
    if(e.key==='s')player.shield=true;
    if(e.key==='Escape')paused=!paused;
   };

   function loop(){
    if(!paused){
     ctx.clearRect(0,0,520,320);
     ctx.fillStyle='#555';ctx.fillRect(0,50,520,250);
     if(turbo>0){player.x+=2;turbo--}
     ctx.fillStyle=player.shield?'cyan':'red';
     ctx.fillRect(player.x,player.y,40,40);
     enemies.forEach(e=>{
      e.y+=e.s; if(e.y>320)e.y=50;
      ctx.fillStyle='yellow';ctx.fillRect(e.x,e.y,40,40);
     });
    }
    requestAnimationFrame(loop);
   }
   loop();
   </script>'''

console=VirtualConsole()