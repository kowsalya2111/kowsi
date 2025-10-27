const scrapeBtn = document.getElementById('scrapeBtn');
const consoleEl = document.getElementById('console');
const jobsEl = document.getElementById('jobs');
const simulateTotal = document.getElementById('simulateTotal');


function logLine(text){
consoleEl.textContent += text + '\n';
consoleEl.scrollTop = consoleEl.scrollHeight;
}


async function fetchJobs(){
consoleEl.textContent = '';
jobsEl.innerHTML = '';


logLine('🔄 Fetching Indeed jobs...');
for(let i=0;i<3;i++){
logLine('.');
await new Promise(r=>setTimeout(r, 400 + Math.random()*300));
}
logLine('Parsing job listings with BeautifulSoup...');
await new Promise(r=>setTimeout(r, 800 + Math.random()*400));


const res = await fetch('/scrape');
const data = await res.json();
const printedTotal = simulateTotal.checked ? 20 : data.count;
logLine(`✅ ${printedTotal} jobs fetched!\n`);


data.jobs.forEach((j, idx)=>{
setTimeout(()=>{
logLine(`${idx+1}. ${j.title} | ${j.company} | ${j.link}`);
const div = document.createElement('div');
div.className = 'job-card';
div.innerHTML = `<h3>${j.title}</h3><p>${j.company}</p><a href='${j.link}' target='_blank'>Apply</a>`;
jobsEl.appendChild(div);
}, idx * 240);
});
}


scrapeBtn.addEventListener('click', fetchJobs);