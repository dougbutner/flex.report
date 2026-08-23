#!/usr/bin/env node
/**
 * Rasterize Lucide + crypto SVGs in image-elements to yellow PNGs via @resvg/resvg-js.
 *
 * Setup (once):
 *   cd .cursor/skills/make-hero-image/scripts/.resvg-tools && npm install @resvg/resvg-js
 *
 * Run from repo root:
 *   node .cursor/skills/make-hero-image/scripts/rasterize_svgs.mjs
 */
const fs = require('fs');
const path = require('path');

const toolsDir = path.join(__dirname, '.resvg-tools');
const resvgPath = path.join(toolsDir, 'node_modules', '@resvg', 'resvg-js');
if (!fs.existsSync(resvgPath)) {
  console.error('Install first: cd', toolsDir, '&& npm install @resvg/resvg-js');
  process.exit(1);
}
const { Resvg } = require(resvgPath);

const elems = path.join(__dirname, '..', 'image-elements');
const folders = [
  path.join(elems, 'icons', 'lucide'),
  path.join(elems, 'icons', 'crypto'),
];

let ok = 0;
for (const folder of folders) {
  if (!fs.existsSync(folder)) continue;
  for (const name of fs.readdirSync(folder)) {
    if (!name.endsWith('.svg')) continue;
    let svg = fs.readFileSync(path.join(folder, name), 'utf8');
    svg = svg.replace(/currentColor/g, 'rgb(255,214,0)');
    svg = svg.replace(/#fff|#FFFFFF|#ffffff/gi, 'rgb(255,214,0)');
    if (!/stroke-width=/.test(svg)) {
      svg = svg.replace('<svg ', '<svg stroke-width="2.25" ');
    }
    try {
      const resvg = new Resvg(svg, {
        fitTo: { mode: 'width', value: 256 },
        background: 'rgba(0,0,0,0)',
      });
      const out = path.join(folder, name.replace(/\.svg$/, '.png'));
      fs.writeFileSync(out, resvg.render().asPng());
      ok += 1;
    } catch (e) {
      console.error('fail', name, e.message);
    }
  }
}
console.log('rasterized', ok);
