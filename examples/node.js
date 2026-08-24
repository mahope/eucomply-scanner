#!/usr/bin/env node
/**
 * Scan a website using the EUComply Scanner library.
 */

import { runScan } from '../engine/index.js';

const target = process.argv[2] || 'https://example.com';

try {
  const report = await runScan(target);
  
  console.log(`\n🔍 EUComply Scan: ${report.url}`);
  console.log(`   Score: ${report.score.passed}/${report.score.total} (${report.score.pct}%)`);
  console.log(`   Platform: ${report.platform}\n`);
  
  for (const [name, check] of Object.entries(report.checks)) {
    const icon = check.pass ? '✅' : check.warn ? '⚠️' : '❌';
    console.log(` ${icon} ${check.label}`);
  }
  
  console.log(`\n${report.disclaimer}`);
} catch (e) {
  console.error('❌ Error:', e.message);
  process.exit(1);
}