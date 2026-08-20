// 테마 관리 (다크모드 / 라이트모드)
const themeToggleBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const themeText = document.getElementById('theme-text');

function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    if (theme === 'dark') {
        themeIcon.textContent = '☀️';
        themeText.textContent = '라이트모드';
    } else {
        themeIcon.textContent = '🌙';
        themeText.textContent = '다크모드';
    }
}

// 초기 테마 설정 (로컬 스토리지 또는 OS 기본 테마)
const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
applyTheme(initialTheme);

// 테마 토글 이벤트
themeToggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    applyTheme(newTheme);
});

// 로또 번호 추첨 로직
document.getElementById('draw-btn').addEventListener('click', () => {
    const container = document.getElementById('lotto-container');
    const numbers = generateLottoNumbers();
    
    // 기존 공 제거
    container.innerHTML = '';
    
    // 새로운 공 생성
    numbers.forEach((num, index) => {
        setTimeout(() => {
            const ball = document.createElement('div');
            ball.classList.add('ball');
            ball.classList.add(getBallColorClass(num));
            ball.textContent = num;
            container.appendChild(ball);
        }, index * 100); // 0.1초 간격으로 순차 등장
    });
});

function generateLottoNumbers() {
    const numbers = [];
    while (numbers.length < 6) {
        const rand = Math.floor(Math.random() * 45) + 1;
        if (!numbers.includes(rand)) {
            numbers.push(rand);
        }
    }
    return numbers.sort((a, b) => a - b);
}

function getBallColorClass(num) {
    if (num <= 10) return 'ball-yellow';
    if (num <= 20) return 'ball-blue';
    if (num <= 30) return 'ball-red';
    if (num <= 40) return 'ball-gray';
    return 'ball-green';
}

