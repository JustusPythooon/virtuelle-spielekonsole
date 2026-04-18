class VirtualConsole:
    def open_app(self,app,coins,owned):
        if app=='settings':
            return 
            <h2>⚙️ Einstellungen</h2>
            <p>Design:</p>
            <button onclick="setTheme('#1a1e3f')">Dunkel Blau</button>
            <button onclick="setTheme('#2b1a1a')">Dunkel Rot</button>
            <button onclick="setTheme('#1a2b1a')">Dunkel Grün</button>
            
        if app=='profile':
            return 
            <h2>👤 Profil</h2>
            <p>Avatar wählen:</p>
            <button onclick="setAvatar('🤖')">🤖</button>
            <button onclick="setAvatar('🧙‍♂️')">🧙‍♂️</button>
            <button onclick="setAvatar('🎮')">🎮</button>
            <button onclick="setAvatar('🐱')">🐱</button>
            
        if app=='shop':
            return 
            <h2>🛒 eShop</h2>
            <p>Kart Racer – 100 Coins</p>
            <button onclick='buy()'>Kaufen</button>
            
        if app=='games':
            if 'kart' in owned:
                return 
                <h2>🎮 Kart Racer</h2>
                <canvas id='game' width='400' height='300'></canvas>
                <script>
                const c=game.getContext('2d');let x=180;
                document.onkeydown=e=>{if(e.key==='ArrowLeft')x-=10;if(e.key==='ArrowRight')x+=10;c.clearRect(0,0,400,300);c.fillStyle='red';c.fillRect(x,240,40,40)}
                setTimeout(()=>unlock(),5000)
                </script>
                
            return '<p>Keine Spiele installiert</p>'
        if app=='achievements':
            return '<h2>🏆 Erfolge</h2><p>🏁 Erste Fahrt – 50 Coins</p>'
console=VirtualConsole()