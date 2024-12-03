// Create stars dynamically
const starContainer = document.createElement('div');
starContainer.className = 'stars';
document.querySelector('.animated-bg').appendChild(starContainer);

for (let i = 0; i < 100; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = Math.random() * 100 + 'vw';
    star.style.top = Math.random() * 100 + 'vh';
    star.style.animationDuration = Math.random() * 3 + 2 + 's';
    starContainer.appendChild(star);
}

// Create magic particles dynamically
for (let i = 0; i < 20; i++) {
    const magic = document.createElement('div');
    magic.className = 'magic';
    magic.style.left = Math.random() * 100 + 'vw';
    magic.style.top = Math.random() * 100 + 'vh';
    magic.style.animationDuration = Math.random() * 3 + 2 + 's';
    document.querySelector('.animated-bg').appendChild(magic);
}
