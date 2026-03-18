const puppeteer = require('puppeteer');
const path = require('path');

const files = [
  { html: '01-dora-data.html', png: '01-dora-data.png', width: 1060, height: 560 },
  { html: '02-inequality.html', png: '02-inequality.png', width: 1060, height: 480 },
  { html: '03-l1l2l3.html', png: '03-l1l2l3.png', width: 1060, height: 520 },
  { html: '04-enterprises.html', png: '04-enterprises.png', width: 1060, height: 600 },
  { html: '05-trends.html', png: '05-trends.png', width: 1060, height: 520 }
];

(async () => {
  for (const file of files) {
    console.log(`📸 ${file.html}...`);
    const browser = await puppeteer.launch({
      headless: 'new',
      executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.setViewport({ width: file.width, height: file.height, deviceScaleFactor: 2 });
    await page.goto(`file://${path.resolve(__dirname, file.html)}`, { waitUntil: 'networkidle0', timeout: 30000 });
    await page.evaluate(() => document.fonts.ready);
    await new Promise(r => setTimeout(r, 500));
    await page.screenshot({ path: path.resolve(__dirname, file.png), clip: { x: 0, y: 0, width: file.width, height: file.height } });
    console.log(`  ✅ ${file.png}`);
    await page.close();
    await browser.close();
  }
  console.log('🎉 完成');
})();
