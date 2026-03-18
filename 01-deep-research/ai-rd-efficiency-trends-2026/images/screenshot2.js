const puppeteer = require('puppeteer');
const path = require('path');

const files = [
  { html: '03-l1l2l3.html', png: '03-l1l2l3.png', width: 1060, height: 520 },
  { html: '04-enterprises.html', png: '04-enterprises.png', width: 1060, height: 600 },
  { html: '05-trends.html', png: '05-trends.png', width: 1060, height: 520 }
];

(async () => {
  for (const file of files) {
    console.log(`📸 处理 ${file.html}...`);
    const browser = await puppeteer.launch({
      headless: 'new',
      executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.setViewport({ width: file.width, height: file.height, deviceScaleFactor: 2 });
    const htmlPath = path.resolve(__dirname, file.html);
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0', timeout: 30000 });
    await page.evaluate(() => document.fonts.ready);
    await new Promise(r => setTimeout(r, 500));
    await page.screenshot({ 
      path: path.resolve(__dirname, file.png),
      clip: { x: 0, y: 0, width: file.width, height: file.height }
    });
    console.log(`  ✅ ${file.png}`);
    await page.close();
    await browser.close();
  }
  console.log('🎉 完成');
})();
